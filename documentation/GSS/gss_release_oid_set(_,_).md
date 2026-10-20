# gss_release_oid_set(_:_:)

**Framework**: GSS  
**Kind**: func  
**Role**: Function

Releases the memory associated with an OID set.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_release_oid_set(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ set: UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32
```

```c
OM_uint32 gss_release_oid_set(OM_uint32 *minor_status, gss_OID_set*set);
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](./gss_s_complete.md) on completion. See [Function Status](./function-status.md) for a complete enumeration of status outputs.

#### Discussion

Use this function to free the memory associated with an OID set that you created with [`gss_create_empty_oid_set(_:_:)`](./gss_create_empty_oid_set%28_,_%29.md), or that was created on your behalf this way. The contents of the set don’t need to be freed individually. OIDs are typically static objects that don’t require memory management.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `set`: The OID set to be released.

## See Also

### Creation and Release
- [func gss_create_empty_oid_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](./gss_create_empty_oid_set%28_,_%29.md)
  Allocates a new, empty set to hold object identifiers.
- [func gss_add_oid_set_member(UnsafeMutablePointer<OM_uint32>, gss_const_OID, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32](./gss_add_oid_set_member%28_,_,_%29.md)
  Adds an object identifier into an OID set.
- [func gss_release_oid(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID?>) -> OM_uint32](./gss_release_oid%28_,_%29.md)
  Releases the memory associated with an object identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_release_oid_set(_:_:))*