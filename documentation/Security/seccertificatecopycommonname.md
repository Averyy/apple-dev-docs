# SecCertificateCopyCommonName(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the common name of the subject of a certificate.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
func SecCertificateCopyCommonName(_ certificate: SecCertificate, _ commonName: UnsafeMutablePointer<CFString?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `certificate`: The certificate object from which to retrieve the common name.
- `commonName`: On return, points to the common name. In Objective-C, call the   function to release this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecopycommonname(_:_:))*