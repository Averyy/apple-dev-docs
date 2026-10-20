# byteSwapped

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

A representation of this integer with the byte order swapped.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var byteSwapped: Int { get }
```

## See Also

### Working with Byte Order
- [var littleEndian: Self](./littleendian.md)
  The little-endian representation of this integer.
- [var bigEndian: Self](./bigendian.md)
  The big-endian representation of this integer.
- [init(littleEndian: Self)](./init%28littleendian%29.md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.
- [init(bigEndian: Self)](./init%28bigendian%29.md)
  Creates an integer from its big-endian representation, changing the byte order if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/byteswapped)*