# ReorderDifference.Destination

**Framework**: SwiftUI  
**Kind**: struct

The destination value of a reordering operation.

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
struct Destination
```

## Topics

### Getting destination details
- [var collectionID: CollectionID](reorderdifference/destination-swift.struct/collectionid.md)
  The collection that contains the destination’s position.
- [var position: ReorderDifference<ItemID, CollectionID>.Destination.Position](reorderdifference/destination-swift.struct/position-swift.property.md)
  The identifier position in the collection where the sources should be moved to.
- [ReorderDifference.Destination.Position](reorderdifference/destination-swift.struct/position-swift.enum.md)
  The position within the destination collection.
### Initializers
- [init(position: ReorderDifference<ItemID, CollectionID>.Destination.Position)](reorderdifference/destination-swift.struct/init(position:).md)
  Initializes the destination value with the provided position and an instance of `ReorderableSingleCollectionIdentifier`.
- [init(position: ReorderDifference<ItemID, CollectionID>.Destination.Position, collectionID: CollectionID)](reorderdifference/destination-swift.struct/init(position:collectionid:).md)
  Initializes the destination value with the provided position and collectionID.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var destination: ReorderDifference<ItemID, CollectionID>.Destination](reorderdifference/destination-swift.property.md)
  The end position of items to move during a reordering operation.
- [var sources: [ItemID]](reorderdifference/sources.md)
  The identifiers of items to move during a reordering operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/reorderdifference/destination-swift.struct)*