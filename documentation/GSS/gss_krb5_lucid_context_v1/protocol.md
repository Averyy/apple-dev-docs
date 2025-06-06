# protocol

**Framework**: GSS  
**Kind**: property

The protocol to use.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.14+

## Declaration

```swift
var `protocol`: OM_uint32
```

#### Discussion

If this value is 0, then the protocol under RFC-1964 is used. If the value is 1, then the protocol under draft-ietf-krb-wg-gssapi-cfx-07 is used.

## See Also

- [var cfx_kd: gss_krb5_cfx_keydata_t](gss_krb5_lucid_context_v1/cfx_kd.md)
  The key data structure for Kerberos 5.
- [var endtime: OM_uint32](gss_krb5_lucid_context_v1/endtime.md)
  The expiration time of the context.
- [var initiate: OM_uint32](gss_krb5_lucid_context_v1/initiate.md)
  The flag indicating if the role is initiator.
- [var recv_seq: OM_uint64](gss_krb5_lucid_context_v1/recv_seq.md)
  The receive sequence number.
- [var rfc1964_kd: gss_krb5_rfc1964_keydata_t](gss_krb5_lucid_context_v1/rfc1964_kd.md)
  The RFC-1964 key data.
- [var send_seq: OM_uint64](gss_krb5_lucid_context_v1/send_seq.md)
  The send sequence number.
- [var version: OM_uint32](gss_krb5_lucid_context_v1/version.md)
  The structure version number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_krb5_lucid_context_v1/protocol)*