# SecCertificateCopyNormalizedSubjectContent(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns a normalized copy of the distinguished name (DN) of the subject of a certificate.

**Availability**:
- macOS 10.7+ - Deprecated in 10.12.4

> **Deprecated**: SecCertificateCopyNormalizedSubjectContent is deprecated. Use SecCertificateCopyNormalizedSubjectSequence instead.

## Declaration

```swift
func SecCertificateCopyNormalizedSubjectContent(_ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

```c
CFDataRefSecCertificateCopyNormalizedSubjectContent(SecCertificateRef certificate, CFErrorRef*error);
```

#### Return Value

A data object containing a DER-encoded X.509 distinguished name suitable for use with [`SecItemCopyMatching(_:_:)`](./secitemcopymatching%28_,_%29.md). Returns `NULL` if an error occurred. In Objective-C, free this object with a call to the [`CFRelease`](../CoreFoundation/cfrelease.md) function when you are done with it.

#### Discussion

To obtain a copy of the subject’s distinguished name in a format suitable for display purposes, call [`SecCertificateCopyValues(_:_:_:)`](./seccertificatecopyvalues%28_,_,_%29.md) instead.

## Parameters

- `certificate`: The certificate from which the subject’s distinguished name should be copied.
- `error`: A pointer to a [`CFError`](../CoreFoundation/cferror.md) variable where an error object is stored upon failure. If not `NULL`, the caller is responsible for checking this variable and releasing the resulting object if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecopynormalizedsubjectcontent(_:_:))*