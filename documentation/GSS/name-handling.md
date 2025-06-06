# Name Handling

**Framework**: GSS

Manage names for GSS-API principals such as a person, a machine, or an application.

## Topics

### Creation and Destruction
- [typealias gss_name_t](gss_name_t.md)
  A pointer to an opaque type that you use to communicate name objects with GSS-API functions.
- [typealias gss_const_name_t](gss_const_name_t.md)
  A pointer to an immutable version of the opaque descriptor used to exchange name objects with GSS-API functions.
- [func gss_canonicalize_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_OID, UnsafeMutablePointer<gss_name_t?>) -> OM_uint32](gss_canonicalize_name(_:_:_:_:).md)
  Converts an internal name into a mechanism name.
- [func GSSNameCreateDisplayString(gss_name_t) -> Unmanaged<CFString>?](gssnamecreatedisplaystring(_:).md)
  Returns a string suitable for displaying to the user from a GSS name.
- [func GSSCreateName(CFTypeRef, gss_const_OID, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> gss_name_t?](gsscreatename(_:_:_:).md)
  Returns a GSS name given a buffer and a type.
- [func gss_release_name(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_name_t?>) -> OM_uint32](gss_release_name(_:_:).md)
  Frees the resources associated with a name object.
### Inquiries
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
- [func gss_userok(gss_name_t, UnsafePointer<CChar>) -> Int32](gss_userok(_:_:).md)
  Returns a flag that indicates if a given user is authorized.
### Imports and Exports
- [func gss_export_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_buffer_t) -> OM_uint32](gss_export_name(_:_:_:).md)
  Returns a mechanism name in contiguous octet format.
- [func gss_import_name(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, gss_const_OID?, UnsafeMutablePointer<gss_name_t?>) -> OM_uint32](gss_import_name(_:_:_:_:).md)
  Converts a name in contiguous octet format to the internal name format.

## See Also

- [Object Identifiers](object-identifiers.md)
  Store security mechanisms, QOPs (Quality of Protection values), and name types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/name-handling)*