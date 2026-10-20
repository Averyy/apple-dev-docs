# TransferRepresentationBuilder

**Framework**: Core Transferable  
**Kind**: struct  
**Role**: Structure

Creates a transfer representation by composing existing transfer representations.

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
@resultBuilder
struct TransferRepresentationBuilder<Item> where Item : Transferable
```

## Topics

### Building a transfer representation
- [static func buildBlock<Content>(Content) -> Content](./transferrepresentationbuilder/buildblock%28_%29.md)
  Passes a single transfer representation to the builder unmodified.
- [static func buildExpression<R>(R) -> R](./transferrepresentationbuilder/buildexpression%28_%29-3z8sl.md)
  Builds a transfer representation from an expression.
- [static func buildExpression<Encoder, Decoder>(CodableRepresentation<Item, Encoder, Decoder>) -> CodableRepresentation<Item, Encoder, Decoder>](./transferrepresentationbuilder/buildexpression%28_%29-6qtdp.md)
  Builds an encodable and decodable transfer representation from an expression.
### Combining transfer representations
- [static func buildBlock<C1, C2>(C1, C2) -> TupleTransferRepresentation<Item, (C1, C2)>](./transferrepresentationbuilder/buildblock%28_,_%29.md)
  Combines multiple transfer representations into a single transfer representation.
- [static func buildBlock<C1, C2, C3>(C1, C2, C3) -> TupleTransferRepresentation<Item, (C1, C2, C3)>](./transferrepresentationbuilder/buildblock%28_,_,_%29.md)
  Combines multiple transfer representations into a single transfer representation.
- [static func buildBlock<C1, C2, C3, C4>(C1, C2, C3, C4) -> TupleTransferRepresentation<Item, (C1, C2, C3, C4)>](./transferrepresentationbuilder/buildblock%28_,_,_,_%29.md)
  Combines multiple transfer representations into a single transfer representation.
- [static func buildBlock<C1, C2, C3, C4, C5>(C1, C2, C3, C4, C5) -> TupleTransferRepresentation<Item, (C1, C2, C3, C4, C5)>](./transferrepresentationbuilder/buildblock%28_,_,_,_,_%29.md)
  Combines multiple transfer representations into a single transfer representation.
- [static func buildBlock<C1, C2, C3, C4, C5, C6>(C1, C2, C3, C4, C5, C6) -> TupleTransferRepresentation<Item, (C1, C2, C3, C4, C5, C6)>](./transferrepresentationbuilder/buildblock%28_,_,_,_,_,_%29.md)
  Combines multiple transfer representations into a single transfer representation.
- [static func buildBlock<C1, C2, C3, C4, C5, C6, C7>(C1, C2, C3, C4, C5, C6, C7) -> TupleTransferRepresentation<Item, (C1, C2, C3, C4, C5, C6, C7)>](./transferrepresentationbuilder/buildblock%28_,_,_,_,_,_,_%29.md)
  Combines multiple transfer representations into a single transfer representation.
- [static func buildBlock<C1, C2, C3, C4, C5, C6, C7, C8>(C1, C2, C3, C4, C5, C6, C7, C8) -> TupleTransferRepresentation<Item, (C1, C2, C3, C4, C5, C6, C7, C8)>](./transferrepresentationbuilder/buildblock%28_,_,_,_,_,_,_,_%29.md)
  Combines multiple transfer representations into a single transfer representation.
- [static func buildBlock<C1, C2, C3, C4, C5, C6, C7, C8, C9>(C1, C2, C3, C4, C5, C6, C7, C8, C9) -> TupleTransferRepresentation<Item, (C1, C2, C3, C4, C5, C6, C7, C8, C9)>](./transferrepresentationbuilder/buildblock%28_,_,_,_,_,_,_,_,_%29.md)
  Combines multiple transfer representations into a single transfer representation.
- [static func buildBlock<C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(C1, C2, C3, C4, C5, C6, C7, C8, C9, C10) -> TupleTransferRepresentation<Item, (C1, C2, C3, C4, C5, C6, C7, C8, C9, C10)>](./transferrepresentationbuilder/buildblock%28_,_,_,_,_,_,_,_,_,_%29.md)
  Combines multiple transfer representations into a single transfer representation.

## See Also

### Supporting types
- [struct TupleTransferRepresentation](./tupletransferrepresentation.md)
  A wrapper type for tuples that contain transfer representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/transferrepresentationbuilder)*