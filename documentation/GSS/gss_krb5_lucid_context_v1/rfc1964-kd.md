# rfc1964_kd

**Framework**: GSS  
**Kind**: property

The RFC-1964 key data.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.14+

## Declaration

```swift
var rfc1964_kd: gss_krb5_rfc1964_keydata_t
```

#### Discussion

Use this structure only if the `protocol` member is set to 0. In that case, the `ctx_kd` member contents are invalid and should be zero.

## See Also

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
- [var send_seq: OM_uint64](gss_krb5_lucid_context_v1/send_seq.md)
  The send sequence number.
- [var version: OM_uint32](gss_krb5_lucid_context_v1/version.md)
  The structure version number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_krb5_lucid_context_v1/rfc1964_kd)*