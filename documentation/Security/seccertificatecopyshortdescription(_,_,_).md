# SecCertificateCopyShortDescription(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns a copy of the short description of a certificate.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecCertificateCopyShortDescription(_ alloc: CFAllocator?, _ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFString?
```

```c
CFStringRefSecCertificateCopyShortDescription(CFAllocatorRef alloc, SecCertificateRef certificate, CFErrorRef*error);
```

## Return Value

A string object containing the short description, or `NULL` if an error occurred. In Objective-C, free this object with [`CFRelease`](../CoreFoundation/cfrelease.md) when you are done with it.

## Discussion

The format of this string is not guaranteed to be consistent across different operating systems or versions. Do not attempt to parse it programmatically.

## Parameters

- `alloc`: The allocator that should be used. Pass `NULL` or [`kCFAllocatorDefault`](../CoreFoundation/kcfallocatordefault.md) to use the default allocator.
- `certificate`: The certificate from which the short description should be copied.
- `error`: A pointer to a [`CFError`](../CoreFoundation/cferror.md) variable where an error object is stored upon failure. If not `NULL`, the caller is responsible for checking this variable and releasing the resulting object if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecopyshortdescription(_:_:_:))*