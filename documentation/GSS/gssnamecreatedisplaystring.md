# GSSNameCreateDisplayString(_:)

**Framework**: GSS  
**Kind**: func

Returns a string suitable for displaying to the user from a GSS name.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
func GSSNameCreateDisplayString(_ name: gss_name_t) -> Unmanaged<CFString>?
```

#### Return Value

A `CFString` object that contains a string suitable for display to the user. Use `CFRelease` to free this object’s memory when you are done with it.

#### Discussion

Do not use the result of this function call to verify ACL subjects.

## Parameters

- `name`: The GSS name from which to get the display string.

## See Also

- [typealias gss_name_t](gss_name_t.md)
  A pointer to an opaque type that you use to communicate name objects with GSS-API functions.
- [typealias gss_const_name_t](gss_const_name_t.md)
  A pointer to an immutable version of the opaque descriptor used to exchange name objects with GSS-API functions.
- [func gss_canonicalize_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_OID, UnsafeMutablePointer<gss_name_t?>) -> OM_uint32](gss_canonicalize_name(_:_:_:_:).md)
  Converts an internal name into a mechanism name.
- [func GSSCreateName(CFTypeRef, gss_const_OID, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> gss_name_t?](gsscreatename(_:_:_:).md)
  Returns a GSS name given a buffer and a type.
- [func gss_release_name(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_name_t?>) -> OM_uint32](gss_release_name(_:_:).md)
  Frees the resources associated with a name object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gssnamecreatedisplaystring(_:))*