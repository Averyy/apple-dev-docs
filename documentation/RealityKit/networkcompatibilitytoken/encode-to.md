# encode(to:)

**Framework**: RealityKit  
**Kind**: method

Writes the token’s data into an encoder.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
final func encode(to encoder: any Encoder) throws
```

#### Discussion

If the value fails to encode anything, `encoder` will encode an empty keyed container. This function throws an [`Error`](https://developer.apple.com/documentation/Swift/Error) if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.

## See Also

- [init(from: any Decoder) throws](networkcompatibilitytoken/init(from:).md)
  Creates a new instance from a decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/networkcompatibilitytoken/encode(to:))*