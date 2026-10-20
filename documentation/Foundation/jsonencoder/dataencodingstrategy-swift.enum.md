# JSONEncoder.DataEncodingStrategy

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

The strategies for encoding raw data.

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
enum DataEncodingStrategy
```

## Topics

### Base64 Encoding
- [JSONEncoder.DataEncodingStrategy.base64](./dataencodingstrategy-swift.enum/base64.md)
  The strategy that encodes data using Base 64 encoding.
### Custom Encoding
- [case custom((Data, any Encoder) throws -> Void)](./dataencodingstrategy-swift.enum/custom%28_%29.md)
  The strategy that encodes data using a user-defined function.
### Data Encoding
- [JSONEncoder.DataEncodingStrategy.deferredToData](./dataencodingstrategy-swift.enum/deferredtodata.md)
  The strategy that encodes data using the encoding specified by the data instance itself.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Encoding Raw Data
- [var dataEncodingStrategy: JSONEncoder.DataEncodingStrategy](./dataencodingstrategy-swift.property.md)
  The strategy that an encoder uses to encode raw data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonencoder/dataencodingstrategy-swift.enum)*