# gss_krb5_lucid_context_v1_t

**Framework**: GSS  
**Kind**: typealias

The structure of a Kerberos context.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.14+

## Declaration

```swift
typealias gss_krb5_lucid_context_v1_t = gss_krb5_lucid_context_v1
```

## Topics

### Context Members
- [var cfx_kd: gss_krb5_cfx_keydata_t](gss_krb5_lucid_context_v1/cfx_kd.md)
  The key data structure for Kerberos 5.
- [var endtime: OM_uint32](gss_krb5_lucid_context_v1/endtime.md)
  The expiration time of the context.
- [var initiate: OM_uint32](gss_krb5_lucid_context_v1/initiate.md)
  The flag indicating if the role is initiator.
- [var `protocol`: OM_uint32](gss_krb5_lucid_context_v1/protocol.md)
  The protocol to use.
- [var recv_seq: OM_uint64](gss_krb5_lucid_context_v1/recv_seq.md)
  The receive sequence number.
- [var rfc1964_kd: gss_krb5_rfc1964_keydata_t](gss_krb5_lucid_context_v1/rfc1964_kd.md)
  The RFC-1964 key data.
- [var send_seq: OM_uint64](gss_krb5_lucid_context_v1/send_seq.md)
  The send sequence number.
- [var version: OM_uint32](gss_krb5_lucid_context_v1/version.md)
  The structure version number.

## See Also

- [typealias gss_krb5_cfx_keydata_t](gss_krb5_cfx_keydata_t.md)
  The structure of a Kerberos context and acceptor-asserted key.
- [typealias gss_krb5_lucid_context_version_t](gss_krb5_lucid_context_version_t.md)
  The structure for determining the returned Kerberos lucid context structure version.
- [typealias gss_krb5_lucid_key_t](gss_krb5_lucid_key_t.md)
  The structure for a Kerberos encryption key.
- [typealias gss_krb5_rfc1964_keydata_t](gss_krb5_rfc1964_keydata_t.md)
  The structure for an RFC 1964-compliant Kerberos encryption key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_krb5_lucid_context_v1_t)*