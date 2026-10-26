# SecCertificateGetData

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the data for a certificate.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecCertificateGetData(SecCertificateRef certificate, CSSM_DATA_PTR data);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

This function requires a certificate object, which can, for example, be created with the [`SecCertificateCreateFromData`](./seccertificatecreatefromdata.md) function, obtained from an identity with the [`SecIdentityCopyCertificate(_:_:)`](./secidentitycopycertificate%28_,_%29.md) function, or obtained over a network (see [Secure Transport](./secure-transport.md)).

## Parameters

- `certificate`: A certificate object for the certificate from which to retrieve the data.
- `data`: On return, points to the data for the certificate specified. You must allocate the space for a `CSSM_DATA` structure before calling this function. This data pointer is only guaranteed to remain valid as long as the certificate remains unchanged and valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificategetdata)*