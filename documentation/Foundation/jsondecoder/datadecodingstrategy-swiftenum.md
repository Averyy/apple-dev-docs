# JSONDecoder.DataDecodingStrategy

**Framework**: Foundation  
**Kind**: enum

The strategies for decoding raw data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum DataDecodingStrategy
```

## Topics

### Base64 Decoding
- [JSONDecoder.DataDecodingStrategy.base64](jsondecoder/datadecodingstrategy-swift.enum/base64.md)
  The strategy that decodes data using Base 64 decoding.
### Custom Decoding
- [JSONDecoder.DataDecodingStrategy.custom(_:)](jsondecoder/datadecodingstrategy-swift.enum/custom(_:).md)
  The strategy that decodes data using a user-defined function.
### Data Decoding
- [JSONDecoder.DataDecodingStrategy.deferredToData](jsondecoder/datadecodingstrategy-swift.enum/deferredtodata.md)
  The strategy that encodes data using the encoding specified by the data instance itself.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var dataDecodingStrategy: JSONDecoder.DataDecodingStrategy](jsondecoder/datadecodingstrategy-swift.property.md)
  The strategy that a decoder uses to decode raw data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsondecoder/datadecodingstrategy-swift.enum)*