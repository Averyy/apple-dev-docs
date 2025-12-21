# SecCertificateCopyNormalizedSubjectSequence(_:)

**Framework**: Security  
**Kind**: func

Retrieves the normalized subject sequence from a certificate.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.12.4+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
func SecCertificateCopyNormalizedSubjectSequence(_ certificate: SecCertificate) -> CFData?
```

#### Return Value

A data object containing the sequence or `NULL` on error. In Objective-C, free this object with a call to the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function when you are done with it.

## Parameters

- `certificate`: The certificate from which to retrieve the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecopynormalizedsubjectsequence(_:))*