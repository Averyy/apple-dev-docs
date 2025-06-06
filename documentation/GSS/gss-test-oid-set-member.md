# gss_test_oid_set_member(_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Returns a flag that indicates if an OID is present in an OID set.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_test_oid_set_member(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ member: gss_const_OID, _ set: gss_OID_set, _ present: UnsafeMutablePointer<Int32>) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a complete enumeration of status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `member`: The OID to search for.
- `set`: The set of OIDs to search in.
- `present`: A pointer that the function uses to indicate whether or not the member is present in the set. The value is non-zero if the member is present, and zero otherwise.

## See Also

- [func gss_oid_to_str(UnsafeMutablePointer<OM_uint32>, gss_OID, gss_buffer_t) -> OM_uint32](gss_oid_to_str(_:_:_:).md)
  Converts an OID object to a human-readable string.
- [func gss_oid_equal(gss_const_OID?, gss_const_OID?) -> Int32](gss_oid_equal(_:_:).md)
  Returns a flag that indicates whether two object identifiers are the same.
- [func gss_duplicate_oid(UnsafeMutablePointer<OM_uint32>, gss_OID, UnsafeMutablePointer<gss_OID?>) -> OM_uint32](gss_duplicate_oid(_:_:_:).md)
  Copies an OID into a new object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_test_oid_set_member(_:_:_:_:))*