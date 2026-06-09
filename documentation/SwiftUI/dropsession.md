# DropSession

**Framework**: SwiftUI  
**Kind**: struct

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DropSession
```

## Topics

### Getting drop session details
- [var id: DropSession.ID](dropsession/id-swift.property.md)
  The unique identifier of the drop session.
- [DropSession.ID](dropsession/id-swift.struct.md)
  The identifier of a drag session.
- [var localSession: DropSession.LocalSession?](dropsession/localsession-swift.property.md)
  Provides additional information about a session if it originated within the app.
- [DropSession.LocalSession](dropsession/localsession-swift.struct.md)
  Describes the session originated within the app.
- [var phase: DropSession.Phase](dropsession/phase-swift.property.md)
  The phase of the current drop session.
- [DropSession.Phase](dropsession/phase-swift.enum.md)
  The phase of the current drop session.
- [var suggestedOperations: DropOperation.Set](dropsession/suggestedoperations.md)
  Operations suggested by the drag source.
### Getting drop details
- [var itemsCount: Int](dropsession/itemscount.md)
  Number of items for the drop.
- [var location: CGPoint](dropsession/location.md)
  Location of drop in the local coordinate space
- [var size: CGSize](dropsession/size.md)
  Size of the drop destination view.
### Supporting reordering
- [func reorderDestination<Item, CollectionID>(for: Item.Type, in: CollectionID.Type) -> ReorderDifference<Item.ID, CollectionID>.Destination?](dropsession/reorderdestination(for:in:).md)
  Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier.
- [func reorderDestination<Item, ItemID, CollectionID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, in: CollectionID.Type) -> ReorderDifference<ItemID, CollectionID>.Destination?](dropsession/reorderdestination(for:itemid:in:).md)
  Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Escapable](../Swift/Escapable.md)
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [struct DragSession](dragsession.md)
  Describes the ongoing dragging session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropsession)*