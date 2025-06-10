# JSONEncoder.DataEncodingStrategy

**Framework**: Foundation  
**Kind**: enum

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
- [JSONEncoder.DataEncodingStrategy.base64](jsonencoder/dataencodingstrategy-swift.enum/base64.md)
  The strategy that encodes data using Base 64 encoding.
### Custom Encoding
- [case custom((Data, any Encoder) throws -> Void)](jsonencoder/dataencodingstrategy-swift.enum/custom(_:).md)
  The strategy that encodes data using a user-defined function.
### Data Encoding
- [JSONEncoder.DataEncodingStrategy.deferredToData](jsonencoder/dataencodingstrategy-swift.enum/deferredtodata.md)
  The strategy that encodes data using the encoding specified by the data instance itself.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var dataEncodingStrategy: JSONEncoder.DataEncodingStrategy](jsonencoder/dataencodingstrategy-swift.property.md)
  The strategy that an encoder uses to encode raw data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonencoder/dataencodingstrategy-swift.enum)*