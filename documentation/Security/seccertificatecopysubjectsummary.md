# SecCertificateCopySubjectSummary(_:)

**Framework**: Security  
**Kind**: func

Returns a human-readable summary of a certificate.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecCertificateCopySubjectSummary(_ certificate: SecCertificate) -> CFString?
```

## Mentions

- [Examining a Certificate](examining-a-certificate.md)
- [Importing an Identity](importing-an-identity.md)

#### Return Value

A string that contains a human-readable summary of the contents of the certificate. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to release this object when you are finished with it. Returns `NULL` if the data passed in the `certificate` parameter is not a valid certificate object.

#### Discussion

Because all the data in the string comes from the certificate, the string is in whatever language is used in the certificate.

## Parameters

- `certificate`: The certificate object for which you wish to return a summary string.

## See Also

- [func SecCertificateCreateWithData(CFAllocator?, CFData) -> SecCertificate?](seccertificatecreatewithdata(_:_:).md)
  Creates a certificate object from a DER representation of a certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecopysubjectsummary(_:))*