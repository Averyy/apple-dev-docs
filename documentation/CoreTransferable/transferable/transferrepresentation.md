# transferRepresentation

**Framework**: Core Transferable  
**Kind**: property  
**Role**: Type Property  
**Required**: Yes

The representation used to import and export the item.

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
@TransferRepresentationBuilder
<Self> static var transferRepresentation: Self.Representation { get }
```

## Mentions

- [Choosing a transfer representation for a model type](../choosing-a-transfer-representation-for-a-model-type.md)

#### Discussion

A [`transferRepresentation`](./transferrepresentation.md) can contain multiple representations for different content types.

## See Also

### Implementing a transfer representation
- [associatedtype Representation : TransferRepresentation](./representation.md)
  The type of the representation used to import and export the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/transferable/transferrepresentation)*