# SecTrustGetCertificateAtIndex(_:_:)

**Framework**: Security  
**Kind**: func

Returns a specific certificate from the certificate chain used to evaluate trust.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func SecTrustGetCertificateAtIndex(_ trust: SecTrust, _ ix: CFIndex) -> SecCertificate?
```

#### Return Value

A certificate object for the requested certificate.

#### Discussion

Call the [`SecTrustEvaluateWithError(_:_:)`](sectrustevaluatewitherror(_:_:).md) function before calling this function.

## Parameters

- `trust`: The trust management object for the certificate that has been evaluated.  Use the   function to create a trust management object and the   function to evaluate the certificate chain.
- `ix`: The index number of the requested certificate. Index numbers start at 0 for the leaf certificate and end at the anchor (or the last certificate if no anchor was found). Use the   function to get the total number of certificates in the chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustgetcertificateatindex(_:_:))*