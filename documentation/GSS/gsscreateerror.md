# GSSCreateError(_:_:_:)

**Framework**: GSS  
**Kind**: func

Returns an error object based on GSS-API major and minor status codes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
func GSSCreateError(_ mech: gss_const_OID, _ major_status: OM_uint32, _ minor_status: OM_uint32) -> Unmanaged<CFError>?
```

#### Return Value

A [`CFError`](https://developer.apple.com/documentation/CoreFoundation/CFError) instance that corresponds to the failure described by the inputs. Release the error with [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) when you are done with it.

## Parameters

- `mech`: The underlying mechanism in use. For example, use   for Kerberos. Use   if none is available.
- `major_status`: Major status code from a failed GSS-API function call.
- `minor_status`: Minor status code from a failed GSS-API function call.

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
- [func gss_display_status(UnsafeMutablePointer<OM_uint32>, OM_uint32, Int32, gss_OID?, UnsafeMutablePointer<OM_uint32>, gss_buffer_t) -> OM_uint32](gss_display_status(_:_:_:_:_:_:).md)
  Returns a human readable string for a status code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gsscreateerror(_:_:_:))*