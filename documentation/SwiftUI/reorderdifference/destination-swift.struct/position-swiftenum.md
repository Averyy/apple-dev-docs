# ReorderDifference.Destination.Position

**Framework**: SwiftUI  
**Kind**: enum

The position within the destination collection.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@frozen
enum Position
```

## Topics

### Destination positions
- [ReorderDifference.Destination.Position.before(_:)](reorderdifference/destination-swift.struct/position-swift.enum/before(_:).md)
  The position of the item with the associated identifier in its collection. Source items should be moved to the index of this item.
- [ReorderDifference.Destination.Position.end](reorderdifference/destination-swift.struct/position-swift.enum/end.md)
  The end of the collection. Source items should be appended to the end of the collection.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var collectionID: CollectionID](reorderdifference/destination-swift.struct/collectionid.md)
  The collection that contains the destination’s position.
- [var position: ReorderDifference<ItemID, CollectionID>.Destination.Position](reorderdifference/destination-swift.struct/position-swift.property.md)
  The identifier position in the collection where the sources should be moved to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/reorderdifference/destination-swift.struct/position-swift.enum)*