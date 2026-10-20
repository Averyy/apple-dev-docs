# gss_release_oid(_:_:)

**Framework**: GSS  
**Kind**: func  
**Role**: Function

Releases the memory associated with an object identifier.

**Availability**:
- iOS 5.0+ - Deprecated in 7.0
- iPadOS 5.0+ - Deprecated in 7.0
- Mac Catalyst 5.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: You never need to call this function. Because OIDs are generally passed around as static objects in memory, there is never a need to create your own, or to release them.

## Declaration

```swift
func gss_release_oid(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ oid: UnsafeMutablePointer<gss_OID?>) -> OM_uint32
```

```c
OM_uint32 gss_release_oid(OM_uint32 *minor_status, gss_OID*oid);
```

## Mentions

- [Allocating and Releasing Objects](./allocating-and-releasing-objects.md)

#### Return Value

A status code set to [`GSS_S_COMPLETE`](./gss_s_complete.md) on success. See [Function Status](./function-status.md) for a complete enumeration of status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `oid`: The object identifier to release.

## See Also

### Creation and Release
- [func gss_create_empty_oid_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](./gss_create_empty_oid_set%28_,_%29.md)
  Allocates a new, empty set to hold object identifiers.
- [func gss_add_oid_set_member(UnsafeMutablePointer<OM_uint32>, gss_const_OID, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32](./gss_add_oid_set_member%28_,_,_%29.md)
  Adds an object identifier into an OID set.
- [func gss_release_oid_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](./gss_release_oid_set%28_,_%29.md)
  Releases the memory associated with an OID set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_release_oid(_:_:))*