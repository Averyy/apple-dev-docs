# buildExpression(_:)

**Framework**: Core Transferable  
**Kind**: method

Builds a transfer representation from an expression.

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
static func buildExpression<R>(_ content: R) -> R where Item == R.Item, R : TransferRepresentation
```

## See Also

- [static func buildBlock<Content>(Content) -> Content](transferrepresentationbuilder/buildblock(_:).md)
  Passes a single transfer representation to the builder unmodified.
- [static func buildExpression<Encoder, Decoder>(CodableRepresentation<Item, Encoder, Decoder>) -> CodableRepresentation<Item, Encoder, Decoder>](transferrepresentationbuilder/buildexpression(_:)-6qtdp.md)
  Builds an encodable and decodable transfer representation from an expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/transferrepresentationbuilder/buildexpression(_:)-3z8sl)*