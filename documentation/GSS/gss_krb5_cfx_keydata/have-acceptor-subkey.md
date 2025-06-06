# have_acceptor_subkey

**Framework**: GSS  
**Kind**: property

The flag that indicates if the Kerberos session acceptor subkey is available.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.14+

## Declaration

```swift
var have_acceptor_subkey: OM_uint32
```

#### Discussion

This flag is set to 1 if the Kerberos session acceptor subkey is available; otherwise, it is set to 0.

## See Also

- [var acceptor_subkey: gss_krb5_lucid_key_t](gss_krb5_cfx_keydata/acceptor_subkey.md)
  The Kerberos session acceptor subkey.
- [var ctx_key: gss_krb5_lucid_key_t](gss_krb5_cfx_keydata/ctx_key.md)
  The Kerberos session context key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_krb5_cfx_keydata/have_acceptor_subkey)*