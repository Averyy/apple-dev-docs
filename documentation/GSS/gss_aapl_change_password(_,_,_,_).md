# gss_aapl_change_password(_:_:_:_:)

**Framework**: GSS  
**Kind**: func  
**Role**: Function

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

```c
OM_uint32 gss_aapl_change_password(gss_name_t const name, gss_const_OID mech, CFDictionaryRef attributes, CFErrorRef*error);
```

#### Return Value

A major status code set to [`GSS_S_COMPLETE`](./gss_s_complete.md) if the call succeeds, or some other value indicating the reason for failure if not.

## Parameters

- `name`: The GSS name for which you want to change the password.
- `mech`: The underlying mechanism in use. For example, use [`GSS_KRB5_MECHANISM`](./gss_krb5_mechanism.md) for Kerberos.
- `attributes`: A dictionary that you use to specify the old and new passwords as string values. Use the keys [`kGSSChangePasswordOldPassword`](./kgsschangepasswordoldpassword.md) and [`kGSSChangePasswordNewPassword`](./kgsschangepasswordnewpassword.md) for the old and new passwords, respectively.
- `error`: A `CFErrorRef` pointer that the function sets to point at a new error object if the function call fails. Pass `NULL` to ignore this error. When an error does exist, it describes the reason for the failure, and you are responsible for releasing it with `CFRelease`.

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
- [func gss_duplicate_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, UnsafeMutablePointer<gss_name_t?>) -> OM_uint32](./gss_duplicate_name%28_,_,_%29.md)
  Returns a copy of an internal name.
- [func gss_userok(gss_name_t, UnsafePointer<CChar>) -> Int32](./gss_userok%28_,_%29.md)
  Returns a flag that indicates if a given user is authorized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_aapl_change_password(_:_:_:_:))*