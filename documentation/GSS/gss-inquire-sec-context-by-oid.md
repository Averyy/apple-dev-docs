# gss_inquire_sec_context_by_oid(_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Returns information about a particular part of a context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_inquire_sec_context_by_oid(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ desired_object: gss_OID, _ data_set: UnsafeMutablePointer<gss_buffer_set_t>?) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a description of other status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `context_handle`: The context to inquire about.
- `desired_object`: The object identifier naming the aspect of the context to examine.
- `data_set`: A pointer to a buffer set that includes the reference objects. Free this buffer set with   when you are done with it.

## See Also

- [func gss_context_time(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, UnsafeMutablePointer<OM_uint32>) -> OM_uint32](gss_context_time(_:_:_:).md)
  Returns the amount of time remaining before a context expires.
- [func gss_inquire_context(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<gss_OID?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<Int32>?, UnsafeMutablePointer<Int32>?) -> OM_uint32](gss_inquire_context(_:_:_:_:_:_:_:_:_:).md)
  Returns information about a security context.
- [func gss_wrap_size_limit(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_qop_t, OM_uint32, UnsafeMutablePointer<OM_uint32>) -> OM_uint32](gss_wrap_size_limit(_:_:_:_:_:_:).md)
  Returns the largest allowable wrap size for a given set of constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_inquire_sec_context_by_oid(_:_:_:_:))*