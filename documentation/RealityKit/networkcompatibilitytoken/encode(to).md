# encode(to:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Writes the token’s data into an encoder.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- visionOS

## Declaration

```swift
final func encode(to encoder: any Encoder) throws
```

## Discussion

If the value fails to encode anything, `encoder` will encode an empty keyed container. This function throws an [`Error`](../../Swift/error.md) if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.

## See Also

### Serializing tokens
- [init(from: any Decoder) throws](./init%28from%29.md)
  Creates a new instance from a decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/networkcompatibilitytoken/encode(to:))*