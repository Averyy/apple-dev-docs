# gss_inquire_context(_:_:_:_:_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Returns information about a security context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_inquire_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ src_name: UnsafeMutablePointer<gss_name_t?>?, _ targ_name: UnsafeMutablePointer<gss_name_t?>?, _ lifetime_rec: UnsafeMutablePointer<OM_uint32>?, _ mech_type: UnsafeMutablePointer<gss_OID?>?, _ ctx_flags: UnsafeMutablePointer<OM_uint32>?, _ locally_initiated: UnsafeMutablePointer<Int32>?, _ xopen: UnsafeMutablePointer<Int32>?) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a description of other status outputs.

#### Discussion

The context must exist but need not be fully established for the inquiry to succeed.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `context_handle`: The context to obtain information about.
- `src_name`: A pointer the function uses to return the name of the initiator. Free the name object’s memory with a call to   when you are done with it. Specify   to ignore this output.
- `targ_name`: A pointer the function uses to return the name of the acceptor. Free the name object’s memory with a call to   when you are done with it. Specify   to ignore this output.
- `lifetime_rec`: A pointer the function uses to return the number of seconds before the context expires, or zero if it has already expired. If the context does not support expiration, it returns  . Specify   to ignore this output.
- `mech_type`: A pointer the function uses to return the mechanism providing the context. Do not release the OID object, because it is held in static memory. Specify   to ignore this output.
- `ctx_flags`: A pointer the function uses to return the flags associated with the context. See   for a description of available flags. Specify NULL to ignore this output.
- `locally_initiated`: A pointer the function uses to return an indicator of the context’s point of origin. The value is zero when the function is called by context’s acceptor and non-zero otherwise. Specify NULL to ignore this output.
- `xopen`: A pointer the function uses to return an indicator of the context’s current state. The value is non-zero when the context if fully established and zero otherwise. Specify NULL to ignore this output.

## See Also

- [func gss_context_time(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, UnsafeMutablePointer<OM_uint32>) -> OM_uint32](gss_context_time(_:_:_:).md)
  Returns the amount of time remaining before a context expires.
- [func gss_inquire_sec_context_by_oid(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_OID, UnsafeMutablePointer<gss_buffer_set_t>?) -> OM_uint32](gss_inquire_sec_context_by_oid(_:_:_:_:).md)
  Returns information about a particular part of a context.
- [func gss_wrap_size_limit(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_qop_t, OM_uint32, UnsafeMutablePointer<OM_uint32>) -> OM_uint32](gss_wrap_size_limit(_:_:_:_:_:_:).md)
  Returns the largest allowable wrap size for a given set of constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_inquire_context(_:_:_:_:_:_:_:_:_:))*