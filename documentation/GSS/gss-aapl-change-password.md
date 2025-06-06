# gss_aapl_change_password(_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Changes the password associated with a name.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
func gss_aapl_change_password(_ name: gss_name_t, _ mech: gss_const_OID, _ attributes: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OM_uint32
```

#### Return Value

A major status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) if the call succeeds, or some other value indicating the reason for failure if not.

## Parameters

- `name`: The GSS name for which you want to change the password.
- `mech`: The underlying mechanism in use. For example, use   for Kerberos.
- `attributes`: A dictionary that you use to specify the old and new passwords as string values. Use the keys   and   for the old and new passwords, respectively.
- `error`: A   pointer that the function sets to point at a new error object if the function call fails. Pass   to ignore this error. When an error does exist, it describes the reason for the failure, and you are responsible for releasing it with  .

## See Also

- [func gss_display_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_buffer_t, UnsafeMutablePointer<gss_OID?>?) -> OM_uint32](gss_display_name(_:_:_:_:).md)
  Converts a name in the internal format to an octet string and the associated name type.
- [func gss_compare_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_name_t, UnsafeMutablePointer<Int32>) -> OM_uint32](gss_compare_name(_:_:_:_:).md)
  Returns a flag that indicates if two names in internal name format refer to the same entity.
- [func gss_inquire_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<gss_OID?>?, UnsafeMutablePointer<gss_buffer_set_t?>?) -> OM_uint32](gss_inquire_name(_:_:_:_:_:).md)
  Returns information about a name.
- [func gss_inquire_mechs_for_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](gss_inquire_mechs_for_name(_:_:_:).md)
  Returns a list of mechanisms that support a particular name type.
- [func gss_inquire_names_for_mech(UnsafeMutablePointer<OM_uint32>, gss_const_OID, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](gss_inquire_names_for_mech(_:_:_:).md)
  Returns a list of name types that a given mechanism supports.
- [func gss_duplicate_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, UnsafeMutablePointer<gss_name_t?>) -> OM_uint32](gss_duplicate_name(_:_:_:).md)
  Returns a copy of an internal name.
- [func gss_userok(gss_name_t, UnsafePointer<CChar>) -> Int32](gss_userok(_:_:).md)
  Returns a flag that indicates if a given user is authorized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_aapl_change_password(_:_:_:_:))*