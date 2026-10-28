# SecCertificateCopySerialNumber(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns a copy of a certificate’s serial number.

**Availability**:
- iOS 10.3+ - Deprecated in 11.0 (renamed: SecCertificateCopySerialNumberData(_:_:))
- iPadOS 10.3+ - Deprecated in 11.0 (renamed: SecCertificateCopySerialNumberData(_:_:))
- Mac Catalyst 10.3+ - Deprecated in 11.0 (renamed: SecCertificateCopySerialNumberData(_:_:))
- macOS 10.7+ - Deprecated in 10.13 (renamed: SecCertificateCopySerialNumberData(_:_:))
- tvOS 10.2+ - Deprecated in 11.0 (renamed: SecCertificateCopySerialNumberData(_:_:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: SecCertificateCopySerialNumberData(_:_:))
- watchOS 3.2+ - Deprecated in 4.0 (renamed: SecCertificateCopySerialNumberData(_:_:))

> **Deprecated**: Use [`SecCertificateCopySerialNumberData(_:_:)`](./seccertificatecopyserialnumberdata%28_,_%29.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
func SecCertificateCopySerialNumber(_ certificate: SecCertificate) -> CFData?
```

*macOS*

```swift
func SecCertificateCopySerialNumber(_ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```c
CFDataRefSecCertificateCopySerialNumber(SecCertificateRef certificate);
```

*macOS*

```c
CFDataRefSecCertificateCopySerialNumber(SecCertificateRef certificate, CFErrorRef*error);
```

## Return Value

A data instance containing a DER-encoded integer for the certificate’s serial number (without the tag and length fields) or `nil` if an error occurred. In Objective-C, free this object with a call to [`CFRelease`](../CoreFoundation/cfrelease.md) when you are done with it.

## Parameters

- `certificate`: The certificate from which the serial number should be copied.
- `error`: A pointer to a [`CFError`](../CoreFoundation/cferror.md) variable where an error object is stored upon failure. If not `NULL`, the caller is responsible for checking this variable and releasing the resulting object if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecopyserialnumber(_:))*