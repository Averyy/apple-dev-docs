# rfc1964_kd

**Framework**: GSS  
**Kind**: property  
**Role**: Instance Property

The RFC-1964 key data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var rfc1964_kd: gss_krb5_rfc1964_keydata_t
```

```c
gss_krb5_rfc1964_keydata_t rfc1964_kd;
```

## Discussion

Use this structure only if the `protocol` member is set to 0. In that case, the `ctx_kd` member contents are invalid and should be zero.

## See Also

### Context Members
- [var cfx_kd: gss_krb5_cfx_keydata_t](./cfx_kd.md)
  The key data structure for Kerberos 5.
- [var endtime: OM_uint32](./endtime.md)
  The expiration time of the context.
- [var initiate: OM_uint32](./initiate.md)
  The flag indicating if the role is initiator.
- [var `protocol`: OM_uint32](./protocol.md)
  The protocol to use.
- [var recv_seq: OM_uint64](./recv_seq.md)
  The receive sequence number.
- [var send_seq: OM_uint64](./send_seq.md)
  The send sequence number.
- [var version: OM_uint32](./version.md)
  The structure version number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_krb5_lucid_context_v1/rfc1964_kd)*