# SecTrustEvaluateWithError(_:_:)

**Framework**: Security  
**Kind**: func

Evaluates trust for the specified certificate and policies.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func SecTrustEvaluateWithError(_ trust: SecTrust, _ error: UnsafeMutablePointer<CFError?>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the certificate is trusted; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method evaluates a certificate’s validity to establish trust for a particular use—for example, in creating a digital signature or to establish a Secure Sockets Layer connection. The method validates a certificate by verifying its signature plus the signatures of the certificates in its certificate chain, up to the anchor certificate, according to the policy or policies included in the trust management object.

If the trust management instance lacks some of the certificates needed to verify the leaf certificate, [`SecTrustEvaluateWithError(_:_:)`](sectrustevaluatewitherror(_:_:).md) searches for certificates:

- In the user’s keychain.
- Among any certificates you previously provided by calling [`SecTrustSetAnchorCertificates(_:_:)`](sectrustsetanchorcertificates(_:_:).md).
- In a system-provided set of keychains provided for this purpose.
- Over the network, if certain extensions are present in the certificate used to build the chain.

> **Note**:  Although this method searches the keychain for intermediate certificates, it does not search the keychain for anchor (root) certificates. To add an anchor certificate, you must call [`SecTrustSetAnchorCertificates(_:_:)`](sectrustsetanchorcertificates(_:_:).md).

Before calling [`SecTrustEvaluateWithError(_:_:)`](sectrustevaluatewitherror(_:_:).md), you can optionally call any of the methods that start with `SecTrustSet` to manage the evaluation. For example, you can verify the validity of the certificates in a trust at a particular date and time, rather than using the current date and time, by first calling the [`SecTrustSetVerifyDate(_:_:)`](sectrustsetverifydate(_:_:).md) method.

The [`SecTrustEvaluateWithError(_:_:)`](sectrustevaluatewitherror(_:_:).md)  method returns a pass or fail indicator and an error describing the reason for any failure. In the case of multiple certificate failures, the error contains a code from [`Security Framework Result Codes`](security-framework-result-codes.md) representing the most serious. The localized description indicates the certificate with the most serious problem and the type of error. The underlying error, located in the error’s [`userInfo`](https://developer.apple.com/documentation/Foundation/NSError/userInfo) dictionary as the value for the [`NSUnderlyingErrorKey`](https://developer.apple.com/documentation/Foundation/NSUnderlyingErrorKey) key, contains a localized description of each certificate in the chain that had an error and all errors found with that certificate.

To find out if you can recover from a trust failure, call the [`SecTrustGetTrustResult(_:_:)`](sectrustgettrustresult(_:_:).md) method. See the [`SecTrustResultType`](sectrustresulttype.md) constants to learn how to interpret the value returned by that call.

Don’t call [`SecTrustEvaluateWithError(_:_:)`](sectrustevaluatewitherror(_:_:).md) from your app’s main run loop because it might require network access to fetch intermediate certificates, or to perform revocation checking. To perform evaluation asynchronously, use [`SecTrustEvaluateAsyncWithError(_:_:_:)`](sectrustevaluateasyncwitherror(_:_:_:).md) instead.

## Parameters

- `trust`: The trust management object to evaluate. A trust management object includes the certificate to be verified plus the policy or policies to be used in evaluating trust. It can optionally also include other certificates to be used in verifying the first certificate. Use the   function to create a trust management object.
- `error`: An error pointer the method uses to return an error when trust evaluation fails. Set to   to ignore the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustevaluatewitherror(_:_:))*