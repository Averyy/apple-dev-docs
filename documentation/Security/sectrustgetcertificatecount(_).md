# SecTrustGetCertificateCount(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the number of certificates in an evaluated certificate chain.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecTrustGetCertificateCount(_ trust: SecTrust) -> CFIndex
```

```c
CFIndex SecTrustGetCertificateCount(SecTrustRef trust);
```

#### Return Value

The number of certificates in the certificate chain.

#### Discussion

Call the [`SecTrustEvaluateWithError(_:_:)`](./sectrustevaluatewitherror%28_,_%29.md) function before calling this function.

## Parameters

- `trust`: The trust management object for the certificate that has been evaluated.  Use the [`SecTrustCreateWithCertificates(_:_:_:)`](./sectrustcreatewithcertificates%28_,_,_%29.md) function to create a trust management object and the [`SecTrustEvaluateWithError(_:_:)`](./sectrustevaluatewitherror%28_,_%29.md) function to evaluate the certificate chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustgetcertificatecount(_:))*