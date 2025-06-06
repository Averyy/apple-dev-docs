# init(bigEndian:)

**Framework**: Swift  
**Kind**: init

Creates an integer from its big-endian representation, changing the byte order if necessary.

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
init(bigEndian value: Self)
```

## Parameters

- `value`: A value to use as the big-endian representation of the   new integer.

## See Also

- [var byteSwapped: Int](int/byteswapped.md)
  A representation of this integer with the byte order swapped.
- [var littleEndian: Self](int/littleendian.md)
  The little-endian representation of this integer.
- [var bigEndian: Self](int/bigendian.md)
  The big-endian representation of this integer.
- [init(littleEndian: Self)](int/init(littleendian:).md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/init(bigendian:))*