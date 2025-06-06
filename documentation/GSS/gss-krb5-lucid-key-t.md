# gss_krb5_lucid_key_t

**Framework**: GSS  
**Kind**: typealias

The structure for a Kerberos encryption key.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.14+

## Declaration

```swift
typealias gss_krb5_lucid_key_t = gss_krb5_lucid_key
```

## Topics

### Key Members
- [var data: UnsafeMutableRawPointer?](gss_krb5_lucid_key/data.md)
  The actual key data.
- [var length: OM_uint32](gss_krb5_lucid_key/length.md)
  The length of the key data.
- [var type: OM_uint32](gss_krb5_lucid_key/type.md)
  The key encryption type.

## See Also

- [typealias gss_krb5_cfx_keydata_t](gss_krb5_cfx_keydata_t.md)
  The structure of a Kerberos context and acceptor-asserted key.
- [typealias gss_krb5_lucid_context_v1_t](gss_krb5_lucid_context_v1_t.md)
  The structure of a Kerberos context.
- [typealias gss_krb5_lucid_context_version_t](gss_krb5_lucid_context_version_t.md)
  The structure for determining the returned Kerberos lucid context structure version.
- [typealias gss_krb5_rfc1964_keydata_t](gss_krb5_rfc1964_keydata_t.md)
  The structure for an RFC 1964-compliant Kerberos encryption key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_krb5_lucid_key_t)*