# decode(from:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Decodes a previously fitted decodable transformer.

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

Available when `Transformer` conforms to `Decodable`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedtabularestimator/decode(from:)-2pr7t)*