# SecCertificateCopyData(_:)

**Framework**: Security  
**Kind**: func

Returns a DER representation of a certificate given a certificate object.

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
func SecCertificateCopyData(_ certificate: SecCertificate) -> CFData
```

## Mentions

- [Storing a DER-Encoded X.509 Certificate](storing-a-der-encoded-x-509-certificate.md)

#### Return Value

The DER representation of the certificate. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to release this object when you are finished with it. Returns `nil` if the data passed in the `certificate` parameter is not a valid certificate object.

## Parameters

- `certificate`: The certificate object for which you wish to return the DER (Distinguished Encoding Rules) representation of the X.509 certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecopydata(_:))*