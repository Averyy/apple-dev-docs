# gss_const_ctx_id_t

**Framework**: GSS  
**Kind**: typealias  
**Role**: Type Alias

A pointer to an immutable opaque type that you use to communicate context pointers with GSS-API functions.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```c
typedef const struct gss_ctx_id_t_desc_struct gss_const_ctx_id_t;
```

## See Also

### Channel Bindings
- [GSS_C_NO_CHANNEL_BINDINGS](./gss_c_no_channel_bindings.md)
  Indicates a `NULL` [`gss_channel_bindings_t`](./gss_channel_bindings_t.md) object.
- [GSS_C_NO_CONTEXT](./gss_c_no_context.md)
  A macro that indicates an empty context id object.
- [typealias gss_ctx_id_t](./gss_ctx_id_t.md)
  A pointer to an opaque type that you use to communicate context pointers with GSS-API functions.
- [struct gss_channel_bindings_struct](./gss_channel_bindings_struct.md)
  The structure defining a channel bindings descriptor that specifies the communications channel used to carry a context.
- [typealias gss_channel_bindings_t](./gss_channel_bindings_t.md)
  A pointer to a channel bindings descriptor that specifies the communications channel used to carry a context.
- [typealias gss_const_channel_bindings_t](./gss_const_channel_bindings_t.md)
  A pointer to an immutable channel bindings descriptor that you use to specify the communications channel used to carry a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_const_ctx_id_t)*