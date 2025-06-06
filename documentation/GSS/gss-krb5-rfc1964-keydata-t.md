# gss_krb5_rfc1964_keydata_t

**Framework**: GSS  
**Kind**: typealias

The structure for an RFC 1964-compliant Kerberos encryption key.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.14+

## Declaration

```swift
typealias gss_krb5_rfc1964_keydata_t = gss_krb5_rfc1964_keydata
```

## Topics

### Key Data Members
- [var ctx_key: gss_krb5_lucid_key_t](gss_krb5_rfc1964_keydata/ctx_key.md)
  The context key (Kerberos session key or subkey).
- [var seal_alg: OM_uint32](gss_krb5_rfc1964_keydata/seal_alg.md)
  The seal/encrypt algorithm.
- [var sign_alg: OM_uint32](gss_krb5_rfc1964_keydata/sign_alg.md)
  The signing algorithm.

## See Also

- [typealias gss_krb5_cfx_keydata_t](gss_krb5_cfx_keydata_t.md)
  The structure of a Kerberos context and acceptor-asserted key.
- [typealias gss_krb5_lucid_context_v1_t](gss_krb5_lucid_context_v1_t.md)
  The structure of a Kerberos context.
- [typealias gss_krb5_lucid_context_version_t](gss_krb5_lucid_context_version_t.md)
  The structure for determining the returned Kerberos lucid context structure version.
- [typealias gss_krb5_lucid_key_t](gss_krb5_lucid_key_t.md)
  The structure for a Kerberos encryption key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_krb5_rfc1964_keydata_t)*