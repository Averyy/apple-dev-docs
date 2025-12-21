# TupleTransferRepresentation

**Framework**: Core Transferable  
**Kind**: struct

A wrapper type for tuples that contain transfer representations.

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
struct TupleTransferRepresentation<Item, Value> where Item : Transferable, Value : Sendable
```

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TransferRepresentation](transferrepresentation.md)

## See Also

- [struct TransferRepresentationBuilder](transferrepresentationbuilder.md)
  Creates a transfer representation by composing existing transfer representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/tupletransferrepresentation)*