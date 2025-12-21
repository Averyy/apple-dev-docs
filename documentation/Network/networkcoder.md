# NetworkCoder

**Framework**: Network  
**Kind**: protocol

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
protocol NetworkCoder : Sendable
```

## Topics

### Associated Types
- [associatedtype Decoder : NetworkDecoder](networkcoder/decoder.md)
- [associatedtype Encoder : NetworkEncoder](networkcoder/encoder.md)
### Initializers
- [init()](networkcoder/init.md)
### Instance Methods
- [func makeDecoder() -> Self.Decoder](networkcoder/makedecoder.md)
  Returns an instance of NetworkDecoder
- [func makeEncoder() -> Self.Encoder](networkcoder/makeencoder.md)
  Returns an instance of NetworkEncoder
### Type Properties
- [static var json: NetworkJSONCoder](networkcoder/json.md)
- [static var propertyList: NetworkPropertyListCoder](networkcoder/propertylist.md)

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [NetworkJSONCoder](networkjsoncoder.md)
- [NetworkPropertyListCoder](networkpropertylistcoder.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkcoder)*