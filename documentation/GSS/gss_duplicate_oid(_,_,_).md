# gss_duplicate_oid(_:_:_:)

**Framework**: GSS  
**Kind**: func  
**Role**: Function

Copies an OID into a new object.

**Availability**:
- iOS 5.0+ - Deprecated in 7.0
- iPadOS 5.0+ - Deprecated in 7.0
- Mac Catalyst 5.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: You never need to call this function. Because OIDs are generally passed around as static objects in memory, there is never a need to create your own, or to release them.

## Declaration

```swift
func gss_duplicate_oid(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ src_oid: gss_OID, _ dest_oid: UnsafeMutablePointer<gss_OID?>) -> OM_uint32
```

```c
OM_uint32 gss_duplicate_oid(OM_uint32 *minor_status, gss_OID src_oid, gss_OID*dest_oid);
```

## Mentions

- [Allocating and Releasing Objects](./allocating-and-releasing-objects.md)

#### Return Value

A status code set to [`GSS_S_COMPLETE`](./gss_s_complete.md) on success. See [Function Status](./function-status.md) for a complete enumeration of status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `src_oid`: The OID to copy.
- `dest_oid`: A pointer the function uses to return a copy of the OID. Use [`gss_release_oid(_:_:)`](./gss_release_oid%28_,_%29.md) to release this object’s memory when you are done with it.

## See Also

### Conversion and Duplication
- [func gss_oid_to_str(UnsafeMutablePointer<OM_uint32>, gss_OID, gss_buffer_t) -> OM_uint32](./gss_oid_to_str%28_,_,_%29.md)
  Converts an OID object to a human-readable string.
- [func gss_test_oid_set_member(UnsafeMutablePointer<OM_uint32>, gss_const_OID, gss_OID_set, UnsafeMutablePointer<Int32>) -> OM_uint32](./gss_test_oid_set_member%28_,_,_,_%29.md)
  Returns a flag that indicates if an OID is present in an OID set.
- [func gss_oid_equal(gss_const_OID?, gss_const_OID?) -> Int32](./gss_oid_equal%28_,_%29.md)
  Returns a flag that indicates whether two object identifiers are the same.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_duplicate_oid(_:_:_:))*