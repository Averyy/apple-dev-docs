# gss_userok(_:_:)

**Framework**: GSS  
**Kind**: func

Returns a flag that indicates if a given user is authorized.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
func gss_userok(_ name: gss_name_t, _ user: UnsafePointer<CChar>) -> Int32
```

#### Return Value

A non-zero integer when the user is authorized and zero otherwise.

## Parameters

- `name`: A name object.
- `user`: A C string that is first imported as a name object with name type   and then authorized against the name object given by the first parameter.

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
- [func gss_aapl_change_password(gss_name_t, gss_const_OID, CFDictionary, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OM_uint32](gss_aapl_change_password(_:_:_:_:).md)
  Changes the password associated with a name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_userok(_:_:))*