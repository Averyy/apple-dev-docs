# gss_oid_equal(_:_:)

**Framework**: GSS  
**Kind**: func

Returns a flag that indicates whether two object identifiers are the same.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_oid_equal(_ a: gss_const_OID?, _ b: gss_const_OID?) -> Int32
```

#### Return Value

A non-zero value if the objects are the same, or zero if they are different.

## Parameters

- `a`: The first object identifier to examine.
- `b`: The second object identifier to examine.

## See Also

- [func gss_oid_to_str(UnsafeMutablePointer<OM_uint32>, gss_OID, gss_buffer_t) -> OM_uint32](gss_oid_to_str(_:_:_:).md)
  Converts an OID object to a human-readable string.
- [func gss_test_oid_set_member(UnsafeMutablePointer<OM_uint32>, gss_const_OID, gss_OID_set, UnsafeMutablePointer<Int32>) -> OM_uint32](gss_test_oid_set_member(_:_:_:_:).md)
  Returns a flag that indicates if an OID is present in an OID set.
- [func gss_duplicate_oid(UnsafeMutablePointer<OM_uint32>, gss_OID, UnsafeMutablePointer<gss_OID?>) -> OM_uint32](gss_duplicate_oid(_:_:_:).md)
  Copies an OID into a new object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_oid_equal(_:_:))*