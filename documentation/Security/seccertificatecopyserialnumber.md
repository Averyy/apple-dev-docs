# SecCertificateCopySerialNumber(_:)

**Framework**: Security  
**Kind**: func

Returns a copy of a certificate’s serial number.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- macOS 10.7+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
func SecCertificateCopySerialNumber(_ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

#### Return Value

A data instance containing a DER-encoded integer for the certificate’s serial number (without the tag and length fields) or `nil` if an error occurred. In Objective-C, free this object with a call to [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) when you are done with it.

## Parameters

- `certificate`: The certificate from which the serial number should be copied.
- `error`: A pointer to a  doc://com.apple.documentation/documentation/corefoundation/cferror-ru8  variable where an error object is stored upon failure. If not  , the caller is responsible for checking this variable and releasing the resulting object if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecopyserialnumber(_:_:))*