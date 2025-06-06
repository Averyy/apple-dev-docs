# gss_OID_set_desc_struct

**Framework**: GSS  
**Kind**: struct

The structure for an OID set descriptor that manages an array of OID descriptors.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
struct gss_OID_set_desc_struct
```

## Topics

### Instance Properties
- [var count: Int](gss_oid_set_desc_struct/count.md)
  The number of OID descriptors in the array.
- [var elements: gss_OID!](gss_oid_set_desc_struct/elements.md)
  A pointer to the array of OID descriptors.
### Initialization
- [init()](gss_oid_set_desc_struct/init.md)
  Initialize a new, empty object identifier set.
- [init(count: Int, elements: gss_OID!)](gss_oid_set_desc_struct/init(count:elements:).md)
  Initialize a new object identifier set with the given identifiers.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [typealias gss_OID](gss_oid.md)
  A pointer to the OID descriptor that exchanges object identifiers with many GSS-API functions.
- [typealias gss_OID_set](gss_oid_set.md)
  A pointer to a descriptor that manages an array of OID descriptors.
- [typealias gss_OID_desc](gss_oid_desc.md)
  The OID descriptor that exchanges object identifiers with many GSS-API functions.
- [typealias gss_const_OID](gss_const_oid.md)
  A pointer to an immutable OID descriptor exchanges object identifiers with many GSS-API functions.
- [typealias gss_const_OID_set](gss_const_oid_set.md)
  A pointer to an immutable descriptor manages an array of OID descriptors.
- [struct gss_OID_desc_struct](gss_oid_desc_struct.md)
  The structure for an OID descriptor that exchanges object identifiers with many GSS-API functions.
- [typealias gss_OID_set_desc](gss_oid_set_desc.md)
  The descriptor that manages an array of OID descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_oid_set_desc_struct)*