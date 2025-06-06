# bigEndian

**Framework**: Swift  
**Kind**: property

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

#### Discussion

If necessary, the byte order of this value is reversed from the typical byte order of this integer type. On a big-endian platform, for any integer `x`, `x == x.bigEndian`.

## See Also

- [var byteSwapped: Int](int/byteswapped.md)
  A representation of this integer with the byte order swapped.
- [var littleEndian: Self](int/littleendian.md)
  The little-endian representation of this integer.
- [init(littleEndian: Self)](int/init(littleendian:).md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.
- [init(bigEndian: Self)](int/init(bigendian:).md)
  Creates an integer from its big-endian representation, changing the byte order if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/bigendian)*