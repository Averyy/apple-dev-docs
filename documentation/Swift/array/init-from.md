# init(from:)

**Framework**: Swift  
**Kind**: init

Creates a new array by decoding from the given decoder.

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
init(from decoder: any Decoder) throws
```

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.

## See Also

- [func encode(to: any Encoder) throws](array/encode(to:).md)
  Encodes the elements of this array into the given encoder in an unkeyed container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/init(from:))*