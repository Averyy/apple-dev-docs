# decode(from:)

**Framework**: Create ML Components  
**Kind**: method  
**Required**: Yes

Decodes a previously fitted transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func decode(from decoder: inout any EstimatorDecoder) throws -> Self.Transformer
```

## See Also

- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](supervisedestimator/encode(_:to:).md)
  Encodes a fitted transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedestimator/decode(from:))*