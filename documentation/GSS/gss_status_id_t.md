# gss_status_id_t

**Framework**: GSS  
**Kind**: typealias  
**Role**: Type Alias

A pointer to a status result.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
typealias gss_status_id_t = UnsafeMutablePointer<OM_uint32>
```

```c
typedef OM_uint32 * gss_status_id_t;
```

## Discussion

See [Function Status](./function-status.md) for valid status values.

## See Also

### Status and Error Creation
- [typealias OM_uint32](./om_uint32.md)
  A 32-bit unsigned integer.
- [typealias OM_uint64](./om_uint64.md)
  A 64-bit unsigned integer.
- [typealias gss_uint32](./gss_uint32.md)
  A 32-bit unsigned integer.
- [var GSS_C_MECH_CODE: Int32](./gss_c_mech_code.md)
  A flag that indicates the status code comes from a call to an underlying mechanism, such as Kerberos.
- [var GSS_C_GSS_CODE: Int32](./gss_c_gss_code.md)
  A flag that indicates the named status code comes from a GSS-API call.
- [var GSS_S_COMPLETE: Int32](./gss_s_complete.md)
  The operation completed without error.
- [func gss_display_status(UnsafeMutablePointer<OM_uint32>, OM_uint32, Int32, gss_OID?, UnsafeMutablePointer<OM_uint32>, gss_buffer_t) -> OM_uint32](./gss_display_status%28_,_,_,_,_,_%29.md)
  Returns a human readable string for a status code.
- [func GSSCreateError(gss_const_OID, OM_uint32, OM_uint32) -> Unmanaged<CFError>?](./gsscreateerror%28_,_,_%29.md)
  Returns an error object based on GSS-API major and minor status codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_status_id_t)*