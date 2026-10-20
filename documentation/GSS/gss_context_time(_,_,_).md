# gss_context_time(_:_:_:)

**Framework**: GSS  
**Kind**: func  
**Role**: Function

Returns the amount of time remaining before a context expires.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_context_time(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ time_rec: UnsafeMutablePointer<OM_uint32>) -> OM_uint32
```

```c
OM_uint32 gss_context_time(OM_uint32 *minor_status, gss_ctx_id_t const context_handle, OM_uint32 *time_rec);
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](./gss_s_complete.md) on success. See [Function Status](./function-status.md) for a description of other status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `context_handle`: The context to examine.
- `time_rec`: A pointer the function uses to return the number of seconds for which the context is valid. Returns 0 if the context is already expired.

## See Also

### Inquiry and Limits
- [func gss_inquire_context(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<gss_OID?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<Int32>?, UnsafeMutablePointer<Int32>?) -> OM_uint32](./gss_inquire_context%28_,_,_,_,_,_,_,_,_%29.md)
  Returns information about a security context.
- [func gss_inquire_sec_context_by_oid(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_OID, UnsafeMutablePointer<gss_buffer_set_t>?) -> OM_uint32](./gss_inquire_sec_context_by_oid%28_,_,_,_%29.md)
  Returns information about a particular part of a context.
- [func gss_wrap_size_limit(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_qop_t, OM_uint32, UnsafeMutablePointer<OM_uint32>) -> OM_uint32](./gss_wrap_size_limit%28_,_,_,_,_,_%29.md)
  Returns the largest allowable wrap size for a given set of constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_context_time(_:_:_:))*