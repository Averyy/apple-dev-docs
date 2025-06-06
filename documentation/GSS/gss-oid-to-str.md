# gss_oid_to_str(_:_:_:)

**Framework**: GSS  
**Kind**: func

Converts an OID object to a human-readable string.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_oid_to_str(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ oid: gss_OID, _ oid_str: gss_buffer_t) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a complete enumeration of status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `oid`: The object identifier to be converted.
- `oid_str`: A buffer the function fills with the OID converted to a human readable string.

## See Also

- [func gss_test_oid_set_member(UnsafeMutablePointer<OM_uint32>, gss_const_OID, gss_OID_set, UnsafeMutablePointer<Int32>) -> OM_uint32](gss_test_oid_set_member(_:_:_:_:).md)
  Returns a flag that indicates if an OID is present in an OID set.
- [func gss_oid_equal(gss_const_OID?, gss_const_OID?) -> Int32](gss_oid_equal(_:_:).md)
  Returns a flag that indicates whether two object identifiers are the same.
- [func gss_duplicate_oid(UnsafeMutablePointer<OM_uint32>, gss_OID, UnsafeMutablePointer<gss_OID?>) -> OM_uint32](gss_duplicate_oid(_:_:_:).md)
  Copies an OID into a new object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_oid_to_str(_:_:_:))*