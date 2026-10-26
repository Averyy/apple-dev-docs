# Name Handling

**Framework**: GSS  
**Role**: API Collection

Manage names for GSS-API principals such as a person, a machine, or an application.

## Topics

### Creation and Destruction
- [typealias gss_name_t](./gss_name_t.md)
  A pointer to an opaque type that you use to communicate name objects with GSS-API functions.
- [typealias gss_const_name_t](./gss_const_name_t.md)
  A pointer to an immutable version of the opaque descriptor used to exchange name objects with GSS-API functions.
- [func gss_canonicalize_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_OID, UnsafeMutablePointer<gss_name_t?>) -> OM_uint32](./gss_canonicalize_name%28_,_,_,_%29.md)
  Converts an internal name into a mechanism name.
- [func GSSNameCreateDisplayString(gss_name_t) -> Unmanaged<CFString>?](./gssnamecreatedisplaystring%28_%29.md)
  Returns a string suitable for displaying to the user from a GSS name.
- [func GSSCreateName(CFTypeRef, gss_const_OID, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> gss_name_t?](./gsscreatename%28_,_,_%29.md)
  Returns a GSS name given a buffer and a type.
- [func gss_release_name(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_name_t?>) -> OM_uint32](./gss_release_name%28_,_%29.md)
  Frees the resources associated with a name object.
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
- [func gss_duplicate_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, UnsafeMutablePointer<gss_name_t?>) -> OM_uint32](./gss_duplicate_name%28_,_,_%29.md)
  Returns a copy of an internal name.
- [func gss_aapl_change_password(gss_name_t, gss_const_OID, CFDictionary, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OM_uint32](./gss_aapl_change_password%28_,_,_,_%29.md)
  Changes the password associated with a name.
- [func gss_userok(gss_name_t, UnsafePointer<CChar>) -> Int32](./gss_userok%28_,_%29.md)
  Returns a flag that indicates if a given user is authorized.
### Imports and Exports
- [func gss_export_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_buffer_t) -> OM_uint32](./gss_export_name%28_,_,_%29.md)
  Returns a mechanism name in contiguous octet format.
- [func gss_import_name(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, gss_const_OID?, UnsafeMutablePointer<gss_name_t?>) -> OM_uint32](./gss_import_name%28_,_,_,_%29.md)
  Converts a name in contiguous octet format to the internal name format.
### Name Types
- [GSS_C_NO_NAME](./gss_c_no_name.md)
  An empty name object.
- [GSS_C_NT_USER_NAME](./gss_c_nt_user_name.md)
  A name that specifies a user on a local system in the username format.
- [GSS_C_NT_MACHINE_UID_NAME](./gss_c_nt_machine_uid_name.md)
  A name used to specify a user on the local system by way of a numeric identifier.
- [GSS_C_NT_STRING_UID_NAME](./gss_c_nt_string_uid_name.md)
  A name that specifies a user on the local system by way of a string representation of a numeric identifier.
- [GSS_C_NT_HOSTBASED_SERVICE_X](./gss_c_nt_hostbased_service_x.md)
  A service that is related to a particular host.
- [GSS_C_NT_HOSTBASED_SERVICE](./gss_c_nt_hostbased_service.md)
  A name used to specify services provided by host computers in the service/hostname format.
- [GSS_C_NT_ANONYMOUS](./gss_c_nt_anonymous.md)
  A name that refers to an anonymous principal.
- [GSS_C_NT_EXPORT_NAME](./gss_c_nt_export_name.md)
  A name of the type exported by the export name function.
- [GSS_KRB5_NT_PRINCIPAL_NAME](./gss_krb5_nt_principal_name.md)
  A name composed as a single-string representation of a Kerberos name.
- [GSS_KRB5_NT_PRINCIPAL](./gss_krb5_nt_principal.md)
  A name composed as a single-string representation of a Kerberos name.

## See Also

### Names and Object Identifiers
- [Object Identifiers](./object-identifiers.md)
  Store security mechanisms, QOPs (Quality of Protection values), and name types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/name-handling)*