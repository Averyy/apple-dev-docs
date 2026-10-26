# gss_krb5_cfx_keydata

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
struct gss_krb5_cfx_keydata
```

```c
struct gss_krb5_cfx_keydata;
```

## Topics

### Initializers
- [init()](./gss_krb5_cfx_keydata/init%28%29.md)
- [init(have_acceptor_subkey: OM_uint32, ctx_key: gss_krb5_lucid_key_t, acceptor_subkey: gss_krb5_lucid_key_t)](./gss_krb5_cfx_keydata/init%28have_acceptor_subkey,ctx_key,acceptor_subkey%29.md)
### Instance Properties
- [var acceptor_subkey: gss_krb5_lucid_key_t](./gss_krb5_cfx_keydata/acceptor_subkey.md)
  The Kerberos session acceptor subkey.
- [var ctx_key: gss_krb5_lucid_key_t](./gss_krb5_cfx_keydata/ctx_key.md)
  The Kerberos session context key.
- [var have_acceptor_subkey: OM_uint32](./gss_krb5_cfx_keydata/have_acceptor_subkey.md)
  The flag that indicates if the Kerberos session acceptor subkey is available.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Structures
- [struct gss_krb5_lucid_context_v1](./gss_krb5_lucid_context_v1.md)
- [struct gss_krb5_lucid_context_version](./gss_krb5_lucid_context_version.md)
- [struct gss_krb5_lucid_key](./gss_krb5_lucid_key.md)
- [struct gss_krb5_rfc1964_keydata](./gss_krb5_rfc1964_keydata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_krb5_cfx_keydata)*