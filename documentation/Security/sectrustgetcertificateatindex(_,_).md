# SecTrustGetCertificateAtIndex(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns a specific certificate from the certificate chain used to evaluate trust.

**Availability**:
- iOS 2.0+ - Deprecated in 15.0 (renamed: SecTrustCopyCertificateChain(_:))
- iPadOS 2.0+ - Deprecated in 15.0 (renamed: SecTrustCopyCertificateChain(_:))
- Mac Catalyst 13.1+ - Deprecated in 15.0 (renamed: SecTrustCopyCertificateChain(_:))
- macOS 10.7+ - Deprecated in 12.0 (renamed: SecTrustCopyCertificateChain(_:))
- tvOS 9.0+ - Deprecated in 15.0 (renamed: SecTrustCopyCertificateChain(_:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: SecTrustCopyCertificateChain(_:))
- watchOS 1.0+ - Deprecated in 8.0 (renamed: SecTrustCopyCertificateChain(_:))

## Declaration

```swift
func SecTrustGetCertificateAtIndex(_ trust: SecTrust, _ ix: CFIndex) -> SecCertificate?
```

```c
SecCertificateRefSecTrustGetCertificateAtIndex(SecTrustRef trust, CFIndex ix);
```

## Return Value

A certificate object for the requested certificate.

## Discussion

Call the [`SecTrustEvaluateWithError(_:_:)`](./sectrustevaluatewitherror%28_,_%29.md) function before calling this function.

## Parameters

- `trust`: The trust management object for the certificate that has been evaluated.  Use the [`SecTrustCreateWithCertificates(_:_:_:)`](./sectrustcreatewithcertificates%28_,_,_%29.md) function to create a trust management object and the [`SecTrustEvaluateWithError(_:_:)`](./sectrustevaluatewitherror%28_,_%29.md) function to evaluate the certificate chain.
- `ix`: The index number of the requested certificate. Index numbers start at 0 for the leaf certificate and end at the anchor (or the last certificate if no anchor was found). Use the [`SecTrustGetCertificateCount(_:)`](./sectrustgetcertificatecount%28_%29.md) function to get the total number of certificates in the chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustgetcertificateatindex(_:_:))*