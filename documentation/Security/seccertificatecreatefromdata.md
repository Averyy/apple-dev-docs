# SecCertificateCreateFromData

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates a certificate object based on the specified data, type, and encoding.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Use [`SecCertificateCreateWithData(_:_:)`](./seccertificatecreatewithdata%28_,_%29.md) instead.

## Declaration

```c
OSStatus SecCertificateCreateFromData(const SecAsn1Item *data, CSSM_CERT_TYPE type, CSSM_CERT_ENCODING encoding, SecCertificateRef*certificate);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

> ❗ **Important**:  This function is deprecated. Use [`SecCertificateCreateWithData(_:_:)`](./seccertificatecreatewithdata%28_,_%29.md) instead.

The certificate object returned by this function is used as input to several other functions in the API.

## Parameters

- `data`: A pointer to the certificate data. The data must be an X509 certificate in binary format.
- `type`: The certificate type as defined in `Security.framework/cssmtype.h`. Permissible values are `CSSM_CERT_X_509v1`, `CSSM_CERT_X_509v2`, and `CSSM_CERT_X_509v3`. If you are unsure of the certificate type, use `CSSM_CERT_X_509v3`.
- `encoding`: The certificate encoding as defined in `Security.framework/cssmtype.h`. Permissible values are `CSSM_CERT_ENCODING_BER` and `CSSM_CERT_ENCODING_DER`. If you are unsure of the encoding, use `CSSM_CERT_ENCODING_BER`.
- `certificate`: On return, points to the newly created certificate object. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecreatefromdata)*