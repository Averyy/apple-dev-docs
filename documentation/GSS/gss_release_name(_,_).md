# gss_release_name(_:_:)

**Framework**: GSS  
**Kind**: func  
**Role**: Function

Frees the resources associated with a name object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_release_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name: UnsafeMutablePointer<gss_name_t?>) -> OM_uint32
```

```c
OM_uint32 gss_release_name(OM_uint32 *minor_status, gss_name_t*input_name);
```

## Return Value

A status code set to [`GSS_S_COMPLETE`](./gss_s_complete.md) on success. See [Function Status](./function-status.md) for a complete enumeration of status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `input_name`: A pointer to the name that should be freed. The name is set to [`GSS_C_NO_NAME`](./gss_c_no_name.md) when the function returns successfully.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_release_name(_:_:))*