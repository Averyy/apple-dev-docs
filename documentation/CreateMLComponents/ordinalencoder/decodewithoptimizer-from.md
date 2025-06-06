# decodeWithOptimizer(from:)

**Framework**: Create ML Components  
**Kind**: method

Reads the encoded transformer with a decoder.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func decodeWithOptimizer(from decoder: inout any EstimatorDecoder) throws -> OrdinalEncoder<Category>.Transformer
```

#### Return Value

The decoded transformer.

## Parameters

- `decoder`: A decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/ordinalencoder/decodewithoptimizer(from:))*