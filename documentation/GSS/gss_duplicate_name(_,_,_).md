# gss_duplicate_name(_:_:_:)

**Framework**: GSS  
**Kind**: func  
**Role**: Function

Returns a copy of an internal name.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_duplicate_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ src_name: gss_name_t, _ dest_name: UnsafeMutablePointer<gss_name_t?>) -> OM_uint32
```

```c
OM_uint32 gss_duplicate_name(OM_uint32 *minor_status, gss_name_t const src_name, gss_name_t*dest_name);
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](./gss_s_complete.md) on success. See [Function Status](./function-status.md) for a complete enumeration of status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `src_name`: The name to duplicate.
- `dest_name`: A pointer the function uses to return the copied name. Release the name using a call to the [`gss_release_name(_:_:)`](./gss_release_name%28_,_%29.md) function when you are done with it.

## See Also

### Inquiries
- [func gss_display_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_buffer_t, UnsafeMutablePointer<gss_OID?>?) -> OM_uint32](./gss_display_name%28_,_,_,_%29.md)
  Converts a name in the internal format to an octet string and the associated name type.
- [func gss_compare_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_name_t, UnsafeMutablePointer<Int32>) -> OM_uint32](./gss_compare_name%28_,_,_,_%29.md)
  Returns a flag that indicates if two names in internal name format refer to the same entity.
- [func gss_inquire_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<gss_OID?>?, UnsafeMutablePointer<gss_buffer_set_t?>?) -> OM_uint32](./gss_inquire_name%28_,_,_,_,_%29.md)
  Returns information about a name.
- [func gss_inquire_mechs_for_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](./gss_inquire_mechs_for_name%28_,_,_%29.md)
  Returns a list of mechanisms that support a particular name type.
- [func gss_inquire_names_for_mech(UnsafeMutablePointer<OM_uint32>, gss_const_OID, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](./gss_inquire_names_for_mech%28_,_,_%29.md)
  Returns a list of name types that a given mechanism supports.
- [func gss_aapl_change_password(gss_name_t, gss_const_OID, CFDictionary, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OM_uint32](./gss_aapl_change_password%28_,_,_,_%29.md)
  Changes the password associated with a name.
- [func gss_userok(gss_name_t, UnsafePointer<CChar>) -> Int32](./gss_userok%28_,_%29.md)
  Returns a flag that indicates if a given user is authorized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_duplicate_name(_:_:_:))*