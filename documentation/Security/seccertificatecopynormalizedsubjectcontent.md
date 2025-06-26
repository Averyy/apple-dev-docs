# SecCertificateCopyNormalizedSubjectContent(_:_:)

**Framework**: Security  
**Kind**: func

Returns a normalized copy of the distinguished name (DN) of the subject of a certificate.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecCertificateCopyNormalizedSubjectContent(_ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

#### Return Value

A data object containing a DER-encoded X.509 distinguished name suitable for use with [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md). Returns `NULL` if an error occurred. In Objective-C, free this object with a call to the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function when you are done with it.

#### Discussion

To obtain a copy of the subject’s distinguished name in a format suitable for display purposes, call [`SecCertificateCopyValues(_:_:_:)`](seccertificatecopyvalues(_:_:_:).md) instead.

## Parameters

- `certificate`: The certificate from which the subject’s distinguished name should be copied.
- `error`: A pointer to a   variable where an error object is stored upon failure. If not  , the caller is responsible for checking this variable and releasing the resulting object if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecopynormalizedsubjectcontent(_:_:))*