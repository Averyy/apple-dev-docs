# SecCertificateGetType

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the type of a specified certificate.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecCertificateGetType(SecCertificateRef certificate, CSSM_CERT_TYPE *certificateType);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Parameters

- `certificate`: A certificate object for the certificate for which to obtain the type.
- `certificateType`: On return, points to the type of the specified certificate. Certificate types are defined in `Security.framework/cssmtype.h`. You must allocate the space for a `CSSM_CERT_TYPE` structure before calling this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificategettype)*