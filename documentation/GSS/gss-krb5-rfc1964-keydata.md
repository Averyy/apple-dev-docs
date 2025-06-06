# gss_krb5_rfc1964_keydata

**Framework**: GSS  
**Kind**: struct

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.14+

## Declaration

```swift
struct gss_krb5_rfc1964_keydata
```

## Topics

### Initializers
- [init()](gss_krb5_rfc1964_keydata/init.md)
- [init(sign_alg: OM_uint32, seal_alg: OM_uint32, ctx_key: gss_krb5_lucid_key_t)](gss_krb5_rfc1964_keydata/init(sign_alg:seal_alg:ctx_key:).md)
### Instance Properties
- [var ctx_key: gss_krb5_lucid_key_t](gss_krb5_rfc1964_keydata/ctx_key.md)
  The context key (Kerberos session key or subkey).
- [var seal_alg: OM_uint32](gss_krb5_rfc1964_keydata/seal_alg.md)
  The seal/encrypt algorithm.
- [var sign_alg: OM_uint32](gss_krb5_rfc1964_keydata/sign_alg.md)
  The signing algorithm.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct gss_krb5_cfx_keydata](gss_krb5_cfx_keydata.md)
- [struct gss_krb5_lucid_context_v1](gss_krb5_lucid_context_v1.md)
- [struct gss_krb5_lucid_context_version](gss_krb5_lucid_context_version.md)
- [struct gss_krb5_lucid_key](gss_krb5_lucid_key.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_krb5_rfc1964_keydata)*