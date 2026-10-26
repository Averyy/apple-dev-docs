# gss_krb5_rfc1964_keydata

**Framework**: GSS  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
struct gss_krb5_rfc1964_keydata
```

```c
struct gss_krb5_rfc1964_keydata;
```

## Topics

### Initializers
- [init()](./gss_krb5_rfc1964_keydata/init%28%29.md)
- [init(sign_alg: OM_uint32, seal_alg: OM_uint32, ctx_key: gss_krb5_lucid_key_t)](./gss_krb5_rfc1964_keydata/init%28sign_alg,seal_alg,ctx_key%29.md)
### Instance Properties
- [var ctx_key: gss_krb5_lucid_key_t](./gss_krb5_rfc1964_keydata/ctx_key.md)
  The context key (Kerberos session key or subkey).
- [var seal_alg: OM_uint32](./gss_krb5_rfc1964_keydata/seal_alg.md)
  The seal/encrypt algorithm.
- [var sign_alg: OM_uint32](./gss_krb5_rfc1964_keydata/sign_alg.md)
  The signing algorithm.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Structures
- [struct gss_krb5_cfx_keydata](./gss_krb5_cfx_keydata.md)
- [struct gss_krb5_lucid_context_v1](./gss_krb5_lucid_context_v1.md)
- [struct gss_krb5_lucid_context_version](./gss_krb5_lucid_context_version.md)
- [struct gss_krb5_lucid_key](./gss_krb5_lucid_key.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_krb5_rfc1964_keydata)*