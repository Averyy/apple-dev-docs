# SecTrustCreateWithCertificates(_:_:_:)

**Framework**: Security  
**Kind**: func

Creates a trust management object based on certificates and policies.

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
func SecTrustCreateWithCertificates(_ certificates: CFTypeRef, _ policies: CFTypeRef?, _ trust: UnsafeMutablePointer<SecTrust?>) -> OSStatus
```

## Mentions

- [Configuring a Trust](configuring-a-trust.md)
- [Creating a Trust Object](creating-a-trust-object.md)

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

The trust management object includes a reference to the certificate to be verified, plus pointers to the policies to be evaluated for those certificates. You can optionally include references to other certificates, including anchor certificates, that you think might be in the certificate chain needed to verify the first (leaf) certificate. Any input certificates that turn out to be irrelevant are harmlessly ignored. Call the [`SecTrustEvaluateWithError(_:_:)`](sectrustevaluatewitherror(_:_:).md) function to evaluate the trust management object.

If you omit needed intermediate certificates from the `certificates` parameter, [`SecTrustEvaluateWithError(_:_:)`](sectrustevaluatewitherror(_:_:).md) searches for certificates in the user’s keychain and in the system’s store of anchor certificates (see [`SecTrustSetAnchorCertificates(_:_:)`](sectrustsetanchorcertificates(_:_:).md)). You gain a significant performance benefit by passing in the entire certificate chain, in order, in the `certificates` parameter.

## Parameters

- `certificates`: The certificate to be verified, plus any other certificates you think might be useful for verifying the certificate. The certificate to be verified must be the first in the array. If you want to specify only one certificate, you can pass a   object; otherwise, pass an array of   objects.
- `policies`: References to one or more policies to be evaluated. You can pass a single   object, or an array of one or more   objects. If you pass in multiple policies, all policies must verify for the certificate chain to be considered valid. You typically use one of the standard policies, like the one returned by  .
- `trust`: On return, points to the newly created trust management object. In Objective-C, call the   function to release this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustcreatewithcertificates(_:_:_:))*