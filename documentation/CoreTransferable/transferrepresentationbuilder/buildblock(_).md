# buildBlock(_:)

**Framework**: Core Transferable  
**Kind**: method  
**Role**: Type Method

Passes a single transfer representation to the builder unmodified.

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
static func buildBlock<Content>(_ content: Content) -> Content where Item == Content.Item, Content : TransferRepresentation
```

## See Also

### Building a transfer representation
- [static func buildExpression<R>(R) -> R](./buildexpression%28_%29-3z8sl.md)
  Builds a transfer representation from an expression.
- [static func buildExpression<Encoder, Decoder>(CodableRepresentation<Item, Encoder, Decoder>) -> CodableRepresentation<Item, Encoder, Decoder>](./buildexpression%28_%29-6qtdp.md)
  Builds an encodable and decodable transfer representation from an expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/transferrepresentationbuilder/buildblock(_:))*