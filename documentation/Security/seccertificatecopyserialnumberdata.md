# SecCertificateCopySerialNumberData(_:_:)

**Framework**: Security  
**Kind**: func

Returns the certificate’s serial number.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func SecCertificateCopySerialNumberData(_ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

#### Return Value

The content of a DER-encoded integer (without the tag and length fields) for this certificate’s serial number.

#### Discussion

In Objective-C, if the function returns an error free it with a call to [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) when you are done with it. If it returns data, you must free that as well.

## Parameters

- `certificate`: The certificate from which to copy the serial number.
- `error`: A   pointer the function uses to return an error instance on failure. Set to   to ignore any error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecopyserialnumberdata(_:_:))*