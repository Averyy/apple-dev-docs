# gss_krb5_lucid_context_v1

**Framework**: GSS  
**Kind**: struct

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.14+

## Declaration

```swift
struct gss_krb5_lucid_context_v1
```

## Topics

### Initializers
- [init()](gss_krb5_lucid_context_v1/init.md)
- [init(version: OM_uint32, initiate: OM_uint32, endtime: OM_uint32, send_seq: OM_uint64, recv_seq: OM_uint64, protocol: OM_uint32, rfc1964_kd: gss_krb5_rfc1964_keydata_t, cfx_kd: gss_krb5_cfx_keydata_t)](gss_krb5_lucid_context_v1/init(version:initiate:endtime:send_seq:recv_seq:protocol:rfc1964_kd:cfx_kd:).md)
### Instance Properties
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

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct gss_krb5_cfx_keydata](gss_krb5_cfx_keydata.md)
- [struct gss_krb5_lucid_context_version](gss_krb5_lucid_context_version.md)
- [struct gss_krb5_lucid_key](gss_krb5_lucid_key.md)
- [struct gss_krb5_rfc1964_keydata](gss_krb5_rfc1964_keydata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_krb5_lucid_context_v1)*