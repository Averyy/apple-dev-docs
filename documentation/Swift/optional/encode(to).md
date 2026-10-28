# encode(to:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Encodes this optional value into the given encoder.

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
func encode(to encoder: any Encoder) throws
```

Available when `Wrapped` conforms to `Encodable`.

## Discussion

This function throws an error if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.

## See Also

### Encoding and Decoding
- [init(from: any Decoder) throws](./init%28from%29.md)
  Creates a new instance by decoding from the given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/encode(to:))*