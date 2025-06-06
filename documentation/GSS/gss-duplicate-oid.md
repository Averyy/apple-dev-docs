# gss_duplicate_oid(_:_:_:)

**Framework**: GSS  
**Kind**: func

Copies an OID into a new object.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func gss_duplicate_oid(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ src_oid: gss_OID, _ dest_oid: UnsafeMutablePointer<gss_OID?>) -> OM_uint32
```

## Mentions

- [Allocating and Releasing Objects](allocating-and-releasing-objects.md)

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a complete enumeration of status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `src_oid`: The OID to copy.
- `dest_oid`: A pointer the function uses to return a copy of the OID. Use   to release this object’s memory when you are done with it.

## See Also

- [func gss_oid_to_str(UnsafeMutablePointer<OM_uint32>, gss_OID, gss_buffer_t) -> OM_uint32](gss_oid_to_str(_:_:_:).md)
  Converts an OID object to a human-readable string.
- [func gss_test_oid_set_member(UnsafeMutablePointer<OM_uint32>, gss_const_OID, gss_OID_set, UnsafeMutablePointer<Int32>) -> OM_uint32](gss_test_oid_set_member(_:_:_:_:).md)
  Returns a flag that indicates if an OID is present in an OID set.
- [func gss_oid_equal(gss_const_OID?, gss_const_OID?) -> Int32](gss_oid_equal(_:_:).md)
  Returns a flag that indicates whether two object identifiers are the same.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_duplicate_oid(_:_:_:))*