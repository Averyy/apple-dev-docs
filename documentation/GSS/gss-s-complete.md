# GSS_S_COMPLETE

**Framework**: GSS  
**Kind**: var

The operation completed without error.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var GSS_S_COMPLETE: Int32 { get }
```

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
- [func gss_display_status(UnsafeMutablePointer<OM_uint32>, OM_uint32, Int32, gss_OID?, UnsafeMutablePointer<OM_uint32>, gss_buffer_t) -> OM_uint32](gss_display_status(_:_:_:_:_:_:).md)
  Returns a human readable string for a status code.
- [func GSSCreateError(gss_const_OID, OM_uint32, OM_uint32) -> Unmanaged<CFError>?](gsscreateerror(_:_:_:).md)
  Returns an error object based on GSS-API major and minor status codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_s_complete)*