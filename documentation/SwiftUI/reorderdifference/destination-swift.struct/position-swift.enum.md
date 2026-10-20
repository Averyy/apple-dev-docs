# ReorderDifference.Destination.Position

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

The position within the destination collection.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@frozen
enum Position
```

## Topics

### Destination positions
- [ReorderDifference.Destination.Position.before(_:)](./position-swift.enum/before%28_%29.md)
  The position of the item with the associated identifier in its collection. Move source items to the index of this item.
- [ReorderDifference.Destination.Position.end](./position-swift.enum/end.md)
  The end of the collection. Append source items to the end of the collection.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting destination details
- [var collectionID: CollectionID](./collectionid.md)
  The collection that contains the destination’s position.
- [var position: ReorderDifference<ItemID, CollectionID>.Destination.Position](./position-swift.property.md)
  The identifier position in the collection where the sources should be moved to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/reorderdifference/destination-swift.struct/position-swift.enum)*