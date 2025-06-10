# SecTrustSetAnchorCertificates(_:_:)

**Framework**: Security  
**Kind**: func

Sets the anchor certificates used when evaluating a trust management object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecTrustSetAnchorCertificates(_ trust: SecTrust, _ anchorCertificates: CFArray?) -> OSStatus
```

## Mentions

- [Configuring a Trust](configuring-a-trust.md)

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

The [`SecTrustEvaluateWithError(_:_:)`](sectrustevaluatewitherror(_:_:).md) function looks for an anchor certificate in the array of certificates specified by the [`SecTrustSetAnchorCertificates(_:_:)`](sectrustsetanchorcertificates(_:_:).md) function, or uses a default set provided by the system. In OS X 10.3, for example, the default set of anchors was in the keychain file /System/Library/Keychains/X509Anchors. If you want to create a set of anchor certificates by modifying the default set, call the [`SecTrustCopyAnchorCertificates(_:)`](sectrustcopyanchorcertificates(_:).md) function to obtain the current set of anchor certificates, modify that set as you wish, and create a new array of certificates. Then call [`SecTrustSetAnchorCertificates(_:_:)`](sectrustsetanchorcertificates(_:_:).md) with the modified array.

The list of custom anchor certificates is stored in the trust management object and can be retrieved with the [`SecTrustCopyCustomAnchorCertificates(_:_:)`](sectrustcopycustomanchorcertificates(_:_:).md) function.

Note that when you call the [`SecTrustSetAnchorCertificates(_:_:)`](sectrustsetanchorcertificates(_:_:).md) function, you are effectively telling the evaluation function to use the anchor certificates in the specified array to evaluate trust regardless of any user-specified trust settings for those certificates. Furthermore, any intermediate certificates based on those anchor certificates are also trusted without consulting user trust settings.

Use the [`SecTrustSetKeychains(_:_:)`](sectrustsetkeychains(_:_:).md) function to set the keychains searched for intermediate certificates in the certificate chain.

It is safe to call this function concurrently on two or more threads as long as it is not used to change the value of a trust management object that is simultaneously being used by another function. For example, you cannot call this function on one thread at the same time as you are calling the evaluation function for the same trust management object on another thread, but you can call this function and simultaneously evaluate a different trust management object on another thread. Similarly, calls to functions that return information about a trust management object (such as the [`SecTrustCopyCustomAnchorCertificates(_:_:)`](sectrustcopycustomanchorcertificates(_:_:).md) function) may fail or return an unexpected result if this function is simultaneously changing the same trust management object on another thread.

> ❗ **Important**:  Calling this function without also calling [`SecTrustSetAnchorCertificatesOnly(_:_:)`](sectrustsetanchorcertificatesonly(_:_:).md) disables the trusting of any anchors other than the ones specified by this function call.

## Parameters

- `trust`: The trust management object containing the certificate you want to evaluate. A trust management object includes the certificate to be verified plus the policy or policies to be used in evaluating trust. It can optionally also include other certificates to be used in verifying the first certificate. Use the   function to create a trust management object.
- `anchorCertificates`: A reference to an array of   objects representing the set of anchor certificates that are to be considered valid (trusted) anchors by the   function when verifying a certificate. Pass   to restore the default set of anchor certificates.

## See Also

- [func SecTrustCopyCustomAnchorCertificates(SecTrust, UnsafeMutablePointer<CFArray?>) -> OSStatus](sectrustcopycustomanchorcertificates(_:_:).md)
  Retrieves the custom anchor certificates, if any, used by a given trust.
- [func SecTrustCopyAnchorCertificates(UnsafeMutablePointer<CFArray?>) -> OSStatus](sectrustcopyanchorcertificates(_:).md)
  Retrieves the anchor (root) certificates stored by macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustsetanchorcertificates(_:_:))*