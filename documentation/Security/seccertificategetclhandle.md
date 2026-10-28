# SecCertificateGetCLHandle

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the certificate library handle from a certificate object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecCertificateGetCLHandle(SecCertificateRef certificate, CSSM_CL_HANDLE *clHandle);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

The certificate library handle is the CSSM identifier of the certificate library module that is managing the certificate. The certificate library handle is used as an input to a number of CSSM functions.

## Parameters

- `certificate`: The certificate object from which to obtain the certificate library handle.
- `clHandle`: On return, points to the certificate library handle of the specified certificate. This handle remains valid until the certificate object is released.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificategetclhandle)*