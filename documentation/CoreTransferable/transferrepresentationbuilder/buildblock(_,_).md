# buildBlock(_:_:)

**Framework**: Core Transferable  
**Kind**: method  
**Role**: Type Method

Combines multiple transfer representations into a single transfer representation.

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
static func buildBlock<C1, C2>(_ content1: C1, _ content2: C2) -> TupleTransferRepresentation<Item, (C1, C2)> where Item == C1.Item, C1 : TransferRepresentation, C2 : TransferRepresentation, C1.Item == C2.Item
```

## See Also

### Combining transfer representations
- [static func buildBlock<C1, C2, C3>(C1, C2, C3) -> TupleTransferRepresentation<Item, (C1, C2, C3)>](./buildblock%28_,_,_%29.md)
  Combines multiple transfer representations into a single transfer representation.
- [static func buildBlock<C1, C2, C3, C4>(C1, C2, C3, C4) -> TupleTransferRepresentation<Item, (C1, C2, C3, C4)>](./buildblock%28_,_,_,_%29.md)
  Combines multiple transfer representations into a single transfer representation.
- [static func buildBlock<C1, C2, C3, C4, C5>(C1, C2, C3, C4, C5) -> TupleTransferRepresentation<Item, (C1, C2, C3, C4, C5)>](./buildblock%28_,_,_,_,_%29.md)
  Combines multiple transfer representations into a single transfer representation.
- [static func buildBlock<C1, C2, C3, C4, C5, C6>(C1, C2, C3, C4, C5, C6) -> TupleTransferRepresentation<Item, (C1, C2, C3, C4, C5, C6)>](./buildblock%28_,_,_,_,_,_%29.md)
  Combines multiple transfer representations into a single transfer representation.
- [static func buildBlock<C1, C2, C3, C4, C5, C6, C7>(C1, C2, C3, C4, C5, C6, C7) -> TupleTransferRepresentation<Item, (C1, C2, C3, C4, C5, C6, C7)>](./buildblock%28_,_,_,_,_,_,_%29.md)
  Combines multiple transfer representations into a single transfer representation.
- [static func buildBlock<C1, C2, C3, C4, C5, C6, C7, C8>(C1, C2, C3, C4, C5, C6, C7, C8) -> TupleTransferRepresentation<Item, (C1, C2, C3, C4, C5, C6, C7, C8)>](./buildblock%28_,_,_,_,_,_,_,_%29.md)
  Combines multiple transfer representations into a single transfer representation.
- [static func buildBlock<C1, C2, C3, C4, C5, C6, C7, C8, C9>(C1, C2, C3, C4, C5, C6, C7, C8, C9) -> TupleTransferRepresentation<Item, (C1, C2, C3, C4, C5, C6, C7, C8, C9)>](./buildblock%28_,_,_,_,_,_,_,_,_%29.md)
  Combines multiple transfer representations into a single transfer representation.
- [static func buildBlock<C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(C1, C2, C3, C4, C5, C6, C7, C8, C9, C10) -> TupleTransferRepresentation<Item, (C1, C2, C3, C4, C5, C6, C7, C8, C9, C10)>](./buildblock%28_,_,_,_,_,_,_,_,_,_%29.md)
  Combines multiple transfer representations into a single transfer representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/transferrepresentationbuilder/buildblock(_:_:))*