# GSSCreateName(_:_:_:)

**Framework**: GSS  
**Kind**: func

Returns a GSS name given a buffer and a type.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
func GSSCreateName(_ name: CFTypeRef, _ name_type: gss_const_OID, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> gss_name_t?
```

#### Return Value

A GSS name for the given buffer and type, or `NULL` on failure. Release this object with a call to [`gss_release_name(_:_:)`](gss_release_name(_:_:).md) when you are done with it.

## Parameters

- `name`: A name buffer describing the credential. The buffer is either a   or a   containing the name.
- `name_type`: An OID name type constant, such as  .
- `error`: A   pointer that the function sets to point at a new error object if the function call fails, or   to ignore the error. If the error exists, it describes the reason for the failure, and you are responsible for releasing it with  .

## See Also

- [typealias gss_name_t](gss_name_t.md)
  A pointer to an opaque type that you use to communicate name objects with GSS-API functions.
- [typealias gss_const_name_t](gss_const_name_t.md)
  A pointer to an immutable version of the opaque descriptor used to exchange name objects with GSS-API functions.
- [func gss_canonicalize_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_OID, UnsafeMutablePointer<gss_name_t?>) -> OM_uint32](gss_canonicalize_name(_:_:_:_:).md)
  Converts an internal name into a mechanism name.
- [func GSSNameCreateDisplayString(gss_name_t) -> Unmanaged<CFString>?](gssnamecreatedisplaystring(_:).md)
  Returns a string suitable for displaying to the user from a GSS name.
- [func gss_release_name(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_name_t?>) -> OM_uint32](gss_release_name(_:_:).md)
  Frees the resources associated with a name object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gsscreatename(_:_:_:))*