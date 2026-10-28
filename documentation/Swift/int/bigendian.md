# bigEndian

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

The big-endian representation of this integer.

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
var bigEndian: Self { get }
```

## Discussion

If necessary, the byte order of this value is reversed from the typical byte order of this integer type. On a big-endian platform, for any integer `x`, `x == x.bigEndian`.

## See Also

### Working with Byte Order
- [var byteSwapped: Int](./byteswapped.md)
  A representation of this integer with the byte order swapped.
- [var littleEndian: Self](./littleendian.md)
  The little-endian representation of this integer.
- [init(littleEndian: Self)](./init%28littleendian%29.md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.
- [init(bigEndian: Self)](./init%28bigendian%29.md)
  Creates an integer from its big-endian representation, changing the byte order if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/bigendian)*