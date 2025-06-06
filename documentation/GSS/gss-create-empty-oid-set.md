# gss_create_empty_oid_set(_:_:)

**Framework**: GSS  
**Kind**: func

Allocates a new, empty set to hold object identifiers.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_create_empty_oid_set(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ oid_set: UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a complete enumeration of status outputs.

#### Discussion

Use [`gss_add_oid_set_member(_:_:_:)`](gss_add_oid_set_member(_:_:_:).md) to add items to your newly created set. Use [`gss_release_oid_set(_:_:)`](gss_release_oid_set(_:_:).md) to free the memory associated with the set when you’re done with it.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `oid_set`: A pointer that the function uses to return the new set.

## See Also

- [func gss_add_oid_set_member(UnsafeMutablePointer<OM_uint32>, gss_const_OID, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32](gss_add_oid_set_member(_:_:_:).md)
  Adds an object identifier into an OID set.
- [func gss_release_oid_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](gss_release_oid_set(_:_:).md)
  Releases the memory associated with an OID set.
- [func gss_release_oid(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID?>) -> OM_uint32](gss_release_oid(_:_:).md)
  Releases the memory associated with an object identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_create_empty_oid_set(_:_:))*