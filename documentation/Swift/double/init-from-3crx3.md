# init(from:)

**Framework**: Swift  
**Kind**: init

Creates a new instance by decoding from the given decoder.

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

- [func encode(to: any Encoder) throws](double/encode(to:).md)
  Encodes this value into the given encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/init(from:)-3crx3)*