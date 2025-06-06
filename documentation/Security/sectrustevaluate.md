# SecTrustEvaluate(_:_:)

**Framework**: Security  
**Kind**: func

Evaluates trust for the specified certificate and policies.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 2.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func SecTrustEvaluate(_ trust: SecTrust, _ result: UnsafeMutablePointer<SecTrustResultType>) -> OSStatus
```

#### Return Value

A result code. See [`Certificate, Key, and Trust Services`](certificate-key-and-trust-services.md).

#### Discussion

This function evaluates a certificate’s validity to establish trust for a particular use—for example, in creating a digital signature or to establish a Secure Sockets Layer connection.

Before you call this function:

- You can call the [`SecTrustSetVerifyDate(_:_:)`](sectrustsetverifydate(_:_:).md) function before calling `SecTrustEvaluate` to set the date and time to use when verifying the certificate. By default, `SecTrustEvaluate` uses the current date and time. (Note that some APIs such as CMS may set the verification date for you based on a trusted time stamp.)
- In macOS, you can optionally call any of the `SecTrustSet...` functions (such as [`SecTrustSetParameters`](sectrustsetparameters.md) or [`SecTrustSetVerifyDate(_:_:)`](sectrustsetverifydate(_:_:).md)) to set values for parameters and options.

The `SecTrustEvaluate` function validates a certificate by verifying its signature plus the signatures of the certificates in its certificate chain, up to the anchor certificate, according to the policy or policies included in the trust management object.

For each policy, the function usually evaluates trust according to the user-specified trust setting (see [`SecTrustSettingsSetTrustSettings(_:_:_:)`](sectrustsettingssettrustsettings(_:_:_:).md) and [`SecTrustSettingsCopyTrustSettings(_:_:_:)`](sectrustsettingscopytrustsettings(_:_:_:).md)). For an example of user-specified trust settings, use the Keychain Access utility and look at any certificate. As an exception, if your app has previously called [`SecTrustSetAnchorCertificates(_:_:)`](sectrustsetanchorcertificates(_:_:).md), the user-specified trust settings are ignored, and the certificate’s chain must contain one of the specified anchor certificates.

For each policy, `SecTrustEvaluate` constructs a certificate chain based on the policies requested. It then starts with the leaf certificate and checks each certificate in the chain in turn until it either reaches a defective certificate, runs out of certificates, or reaches a certificate with a non-default trust setting—usually an anchor certificate or a certificate that the user has explicitly chosen to trust or distrust—and stores the result of this trust evaluation in the trust management object. This design means that an explicit user-trust setting for a certificate at or near the leaf can override the behavior of a certificate closer to the root, but otherwise a failure at any point in the chain results in a failure.

If some of the certificates needed to verify the leaf certificate are missing from the trust management object, then `SecTrustEvaluate` searches for certificates in the following locations:

- In any keychains currently on the caller’s keychain search list (see [`SecTrustSetKeychains(_:_:)`](sectrustsetkeychains(_:_:).md)).
- Any certificates previously provided by calling [`SecTrustSetAnchorCertificates(_:_:)`](sectrustsetanchorcertificates(_:_:).md).
- In a system-provided set of keychains provided for this purpose.
- Over the network if certain extensions are present in the certificate used to build the chain.

> **Note**:  Although this function searches the user’s keychain (or the application keychain in iOS) for intermediate certificates, it does not search those keychains for anchor (root) certificates. To add an anchor certificate, you must call [`SecTrustSetAnchorCertificates(_:_:)`](sectrustsetanchorcertificates(_:_:).md).

As a rule, you should handle the various return values as follows:

- [`SecTrustResultType.unspecified`](sectrustresulttype/unspecified.md)—Evaluation successfully reached an (implicitly trusted) anchor certificate without any evaluation failures, but never encountered any explicitly stated user-trust preference. This is the most common return value.

Most apps should, by default, trust the chain. If you ask the user what to do, in macOS, you should use the [`SFCertificateTrustPanel`](https://developer.apple.com/documentation/SecurityInterface/SFCertificateTrustPanel) class in the [`Security Interface`](https://developer.apple.com/documentation/SecurityInterface).

- [`SecTrustResultType.proceed`](sectrustresulttype/proceed.md)—The user explicitly chose to trust a certificate in the chain (usually by clicking a button in a certificate trust panel).

Your app should trust the chain.

- [`SecTrustResultType.deny`](sectrustresulttype/deny.md)—The user explicitly chose to  trust a certificate in the chain (usually by clicking the appropriate button in a certificate trust panel).

Your app should  trust the chain.

- [`SecTrustResultType.confirm`](sectrustresulttype/confirm.md)—The user previously chose to always ask for permission before accepting one of the certificates in the chain. This return value is no longer used, but may occur in older versions of macOS.

Either ask the user what to do or reject the certificate. If you ask the user what to do, in macOS, you should use the [`SFCertificateTrustPanel`](https://developer.apple.com/documentation/SecurityInterface/SFCertificateTrustPanel) class in the [`Security Interface`](https://developer.apple.com/documentation/SecurityInterface).

- [`SecTrustResultType.recoverableTrustFailure`](sectrustresulttype/recoverabletrustfailure.md)—This means that you should not trust the chain as-is, but that the chain could be trusted with some minor change to the evaluation context, such as ignoring expired certificates or adding an additional anchor to the set of trusted anchors.

The way you handle this depends on the OS.

In iOS, you should typically refuse the certificate. However, if you are performing signature validation and you know when the message was originally received, you should check again using that date to see if the message was valid when you originally received it.

In macOS, you can call the [`SecTrustCopyResult(_:)`](sectrustcopyresult(_:).md) function to get more information about the results of the trust evaluation, or the [`SecTrustGetCssmResult`](sectrustgetcssmresult.md) function to get information about the evaluation in a form that can be passed to CSSM functions.

Then, as appropriate, you can call one or more of the `SecTrustSet...` functions to correct or bypass the problem, or you can inform the user of the problem and call the `SFCertificateTrustPanel` class to let the user change the trust setting for the certificate.

When you think you have corrected the problem, call `SecTrustEvaluate` again. Each time you call `SecTrustEvaluate`, it discards the results of any previous evaluation and replaces them with the new results.

If the trust failure was caused by an untrusted root certificate and your app asks the user what to do, you should use the [`SFCertificateTrustPanel`](https://developer.apple.com/documentation/SecurityInterface/SFCertificateTrustPanel) class in the [`Security Interface`](https://developer.apple.com/documentation/SecurityInterface).

- [`SecTrustResultType.fatalTrustFailure`](sectrustresulttype/fataltrustfailure.md)—Evaluation failed because a certificate in the chain is defective. This usually represents a fundamental defect in the certificate data, such as an invalid encoding for a critical `subjectAltName` extension, an unsupported critical extension, or some other critical portion of the certificate that could not be successfully interpreted. Changing parameter values and calling `SecTrustEvaluate` again is unlikely to result in a successful reevaluation unless you provide different certificates.
- [`SecTrustResultType.otherError`](sectrustresulttype/othererror.md)—Evaluation failed for some other reason. This can be caused by either a revoked certificate or by OS-level errors that are unrelated to the certificates themselves.

##### Special Considerations

It is not safe to call this function concurrently with any other function that uses the same trust management object, or to re-enter this function for the same trust management object.

Because this function might look on the network for certificates in the certificate chain, the function might block while attempting network access. You should never call it from your main thread; call it only from within a function running on a dispatch queue or on a separate thread. Alternatively, in macOS, you can use [`SecTrustEvaluateAsync(_:_:_:)`](sectrustevaluateasync(_:_:_:).md) from your main thread. In iOS, you can do the same thing using [`dispatch_once`](https://developer.apple.com/documentation/dispatch/1447169-dispatch_once).

## Parameters

- `trust`: The trust management object to evaluate. A trust management object includes the certificate to be verified plus the policy or policies to be used in evaluating trust. It can optionally also include other certificates to be used in verifying the first certificate. Use the   function to create a trust management object.
- `result`: On return, points to a result type reflecting the result of this evaluation. See   for descriptions of possible values. See the discussion below for an explanation of how to handle specific values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustevaluate(_:_:))*