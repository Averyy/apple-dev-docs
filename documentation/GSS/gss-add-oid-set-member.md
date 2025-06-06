# gss_add_oid_set_member(_:_:_:)

**Framework**: GSS  
**Kind**: func

Adds an object identifier into an OID set.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_add_oid_set_member(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ member_oid: gss_const_OID, _ oid_set: UnsafeMutablePointer<gss_OID_set>) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a complete enumeration of status outputs.

#### Discussion

If the OID already exists in the set, there is no action taken. Otherwise, the function adds the OID to the end of the set. Because the function adds the OID doesn’t copy it, the `member_oid` pointer must remain stable while the `oid_set` is in use.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `member_oid`: The object identifier to be added.
- `oid_set`: A pointer to the set to which the new OID should be added. Use   to create a new set.

## See Also

- [func gss_create_empty_oid_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](gss_create_empty_oid_set(_:_:).md)
  Allocates a new, empty set to hold object identifiers.
- [func gss_release_oid_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](gss_release_oid_set(_:_:).md)
  Releases the memory associated with an OID set.
- [func gss_release_oid(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID?>) -> OM_uint32](gss_release_oid(_:_:).md)
  Releases the memory associated with an object identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_add_oid_set_member(_:_:_:))*