# init(length:elements:)

**Framework**: GSS  
**Kind**: init

Initialize a new object identifier with the given array of octets.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
init(length: OM_uint32, elements: UnsafeMutableRawPointer!)
```

## Parameters

- `length`: The number of octets in the   array.
- `elements`: A pointer to the beginning of an array of octets of the specified length that represent the object identifier.

## See Also

- [init()](gss_oid_desc_struct/init.md)
  Initialize a new, empty object identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_oid_desc_struct/init(length:elements:))*