# gss_wrap_size_limit(_:_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Returns the largest allowable wrap size for a given set of constraints.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_wrap_size_limit(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ conf_req_flag: Int32, _ qop_req: gss_qop_t, _ req_output_size: OM_uint32, _ max_input_size: UnsafeMutablePointer<OM_uint32>) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a description of other status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `context_handle`: The context used to transmit the data.
- `conf_req_flag`: A flag that you set to a non-zero value to indicate that wrapping function will apply confidentiality in addition to integrity protection or zero if only integrity protection is required.
- `qop_req`: The required quality of protection. See   for possible values.
- `req_output_size`: The maximum allowable output token size from the   function.
- `max_input_size`: A  pointer the function uses to return the maximum input size.

## See Also

- [func gss_context_time(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, UnsafeMutablePointer<OM_uint32>) -> OM_uint32](gss_context_time(_:_:_:).md)
  Returns the amount of time remaining before a context expires.
- [func gss_inquire_context(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<gss_OID?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<Int32>?, UnsafeMutablePointer<Int32>?) -> OM_uint32](gss_inquire_context(_:_:_:_:_:_:_:_:_:).md)
  Returns information about a security context.
- [func gss_inquire_sec_context_by_oid(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_OID, UnsafeMutablePointer<gss_buffer_set_t>?) -> OM_uint32](gss_inquire_sec_context_by_oid(_:_:_:_:).md)
  Returns information about a particular part of a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_wrap_size_limit(_:_:_:_:_:_:))*