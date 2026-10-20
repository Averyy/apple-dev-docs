# gss_const_name_t

**Framework**: GSS  
**Kind**: typealias  
**Role**: Type Alias

A pointer to an immutable version of the opaque descriptor used to exchange name objects with GSS-API functions.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
typealias gss_const_name_t = OpaquePointer
```

```c
typedef const struct gss_name_t_desc_struct * gss_const_name_t;
```

## See Also

### Creation and Destruction
- [typealias gss_name_t](./gss_name_t.md)
  A pointer to an opaque type that you use to communicate name objects with GSS-API functions.
- [func gss_canonicalize_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_OID, UnsafeMutablePointer<gss_name_t?>) -> OM_uint32](./gss_canonicalize_name%28_,_,_,_%29.md)
  Converts an internal name into a mechanism name.
- [func GSSNameCreateDisplayString(gss_name_t) -> Unmanaged<CFString>?](./gssnamecreatedisplaystring%28_%29.md)
  Returns a string suitable for displaying to the user from a GSS name.
- [func GSSCreateName(CFTypeRef, gss_const_OID, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> gss_name_t?](./gsscreatename%28_,_,_%29.md)
  Returns a GSS name given a buffer and a type.
- [func gss_release_name(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_name_t?>) -> OM_uint32](./gss_release_name%28_,_%29.md)
  Frees the resources associated with a name object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_const_name_t)*