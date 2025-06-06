# buildExpression(_:)

**Framework**: Core Transferable  
**Kind**: method

Builds an encodable and decodable transfer representation from an expression.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func buildExpression<Encoder, Decoder>(_ content: CodableRepresentation<Item, Encoder, Decoder>) -> CodableRepresentation<Item, Encoder, Decoder> where Item : Decodable, Item : Encodable, Encoder : TopLevelEncoder, Decoder : TopLevelDecoder, Encoder.Output == Data, Decoder.Input == Data
```

## See Also

- [static func buildBlock<Content>(Content) -> Content](transferrepresentationbuilder/buildblock(_:).md)
  Passes a single transfer representation to the builder unmodified.
- [static func buildExpression<R>(R) -> R](transferrepresentationbuilder/buildexpression(_:)-3z8sl.md)
  Builds a transfer representation from an expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/transferrepresentationbuilder/buildexpression(_:)-6qtdp)*