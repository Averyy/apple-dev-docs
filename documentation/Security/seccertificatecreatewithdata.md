# SecCertificateCreateWithData(_:_:)

**Framework**: Security  
**Kind**: func

Creates a certificate object from a DER representation of a certificate.

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
func SecCertificateCreateWithData(_ allocator: CFAllocator?, _ data: CFData) -> SecCertificate?
```

## Mentions

- [Storing a DER-Encoded X.509 Certificate](storing-a-der-encoded-x-509-certificate.md)

#### Return Value

The newly created certificate object. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function to release this object when you are finished with it. Returns `nil` if the data passed in the `data` parameter is not a valid DER-encoded X.509 certificate.

#### Discussion

The certificate object returned by this function is used as input to other functions in the API.

## Parameters

- `allocator`: The   object you wish to use to allocate the certificate object. Pass   to use the default allocator.
- `data`: A DER (Distinguished Encoding Rules) representation of an X.509 certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecreatewithdata(_:_:))*