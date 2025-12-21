# SecCertificateCopyLongDescription(_:_:_:)

**Framework**: Security  
**Kind**: func

Returns a copy of the long description of a certificate.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecCertificateCopyLongDescription(_ alloc: CFAllocator?, _ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFString?
```

#### Return Value

A string object containing the long description, or `NULL` if an error occurred. In Objective-C, free this object with a call to the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function when you are done with it.

#### Discussion

The format of this string is not guaranteed to be consistent across different operating systems or versions. Do not attempt to parse it programmatically.

## Parameters

- `alloc`: The allocator that should be used. Pass   or   to use the default allocator.
- `certificate`: The certificate from which the long description should be copied.
- `error`: A pointer to a   variable where an error object is stored upon failure. If not  , the caller is responsible for checking this variable and releasing the resulting object if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecopylongdescription(_:_:_:))*