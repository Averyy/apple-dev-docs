# gss_krb5_cfx_keydata_t

**Framework**: GSS  
**Kind**: typealias  
**Role**: Type Alias

The structure of a Kerberos context and acceptor-asserted key.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
typealias gss_krb5_cfx_keydata_t = gss_krb5_cfx_keydata
```

```c
typedef struct gss_krb5_cfx_keydata gss_krb5_cfx_keydata_t;
```

## Topics

### Key Properties
- [var acceptor_subkey: gss_krb5_lucid_key_t](./gss_krb5_cfx_keydata/acceptor_subkey.md)
  The Kerberos session acceptor subkey.
- [var ctx_key: gss_krb5_lucid_key_t](./gss_krb5_cfx_keydata/ctx_key.md)
  The Kerberos session context key.
- [var have_acceptor_subkey: OM_uint32](./gss_krb5_cfx_keydata/have_acceptor_subkey.md)
  The flag that indicates if the Kerberos session acceptor subkey is available.

## See Also

### Contexts and Keys
- [typealias gss_krb5_lucid_context_v1_t](./gss_krb5_lucid_context_v1_t.md)
  The structure of a Kerberos context.
- [typealias gss_krb5_lucid_context_version_t](./gss_krb5_lucid_context_version_t.md)
  The structure for determining the returned Kerberos lucid context structure version.
- [typealias gss_krb5_lucid_key_t](./gss_krb5_lucid_key_t.md)
  The structure for a Kerberos encryption key.
- [typealias gss_krb5_rfc1964_keydata_t](./gss_krb5_rfc1964_keydata_t.md)
  The structure for an RFC 1964-compliant Kerberos encryption key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_krb5_cfx_keydata_t)*