# gss_display_status(_:_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Returns a human readable string for a status code.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_display_status(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ status_value: OM_uint32, _ status_type: Int32, _ mech_type: gss_OID?, _ message_content: UnsafeMutablePointer<OM_uint32>, _ status_string: gss_buffer_t) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a complete enumeration of status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `status_value`: The status to be examined.
- `status_type`: The kind of status to be examined. Set to   for a GSS status code, or to   for a mechanism status code.
- `mech_type`: The mechanism for which to interpret the status value. Set to   to indicate the system default.
- `message_content`: A pointer the function uses to return a context that is currently always set to zero.
- `status_string`: A buffer the function fills with the human readable string corresponding to the status code. Release this buffer with a call to   when you are done with it.

## See Also

- [typealias OM_uint32](om_uint32.md)
  A 32-bit unsigned integer.
- [typealias OM_uint64](om_uint64.md)
  A 64-bit unsigned integer.
- [typealias gss_uint32](gss_uint32.md)
  A 32-bit unsigned integer.
- [typealias gss_status_id_t](gss_status_id_t.md)
  A pointer to a status result.
- [var GSS_C_MECH_CODE: Int32](gss_c_mech_code.md)
  A flag that indicates the status code comes from a call to an underlying mechanism, such as Kerberos.
- [var GSS_C_GSS_CODE: Int32](gss_c_gss_code.md)
  A flag that indicates the named status code comes from a GSS-API call.
- [var GSS_S_COMPLETE: Int32](gss_s_complete.md)
  The operation completed without error.
- [func GSSCreateError(gss_const_OID, OM_uint32, OM_uint32) -> Unmanaged<CFError>?](gsscreateerror(_:_:_:).md)
  Returns an error object based on GSS-API major and minor status codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_display_status(_:_:_:_:_:_:))*