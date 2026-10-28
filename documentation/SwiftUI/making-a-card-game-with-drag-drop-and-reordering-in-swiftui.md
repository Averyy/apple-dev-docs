# Making a card game with drag, drop, and reordering in SwiftUI

**Framework**: SwiftUI  
**Role**: Sample Code  
**Download**: [MakingACardGameWithDragDropAndReorderingInSwiftUI.zip](https://docs-assets.developer.apple.com/published/97ac6f9aaef0/MakingACardGameWithDragDropAndReorderingInSwiftUI.zip)

Move cards between positions in a card game using drag, drop, and reordering modifiers.

**Availability**:
- macOS 27.0+
- Xcode 27.0+

## Overview

> **Note**: This sample code project is associated with WWDC26 session 271: [Code-along: Build powerful drag and drop in SwiftUI](http://developer.apple.com/videos/play/wwdc2026/271/).

## See Also

### Reordering items
- [func reorderable() -> some DynamicViewContent<Self.Data>
](./dynamicviewcontent/reorderable%28%29.md)
  Enables reordering of views from this content inside the scope of a reorderable container modifier.
- [func reorderable(collectionID: some Hashable & Sendable) -> some DynamicViewContent<Self.Data>
](./dynamicviewcontent/reorderable%28collectionid%29.md)
  Enables reordering views from this content within and between sections in the scope of a reorderable container modifier.
- [struct ReorderableSingleCollectionIdentifier](./reorderablesinglecollectionidentifier.md)
  An opaque, empty type used to identify reorderable containers and modifiers with only a single collection.
- [func reorderContainer<Item>(for: Item.Type, isEnabled: Bool, move: (ReorderDifference<Item.ID, ReorderableSingleCollectionIdentifier>) -> ()) -> some View](./view/reordercontainer%28for,isenabled,move%29.md)
  Defines a container of reorderable views.
- [func reorderContainer<Item, CollectionID>(for: Item.Type, in: CollectionID.Type, isEnabled: Bool, move: (ReorderDifference<Item.ID, CollectionID>) -> ()) -> some View](./view/reordercontainer%28for,in,isenabled,move%29.md)
  Defines a container of reorderable views, with a type you specify to identify sections.
- [func reorderContainer<Item, ItemID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, isEnabled: Bool, move: (ReorderDifference<ItemID, ReorderableSingleCollectionIdentifier>) -> ()) -> some View](./view/reordercontainer%28for,itemid,isenabled,move%29.md)
  Defines a container of reorderable views, with a type and keypath you specify to identify items.
- [func reorderContainer<Item, ItemID, CollectionID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, in: CollectionID.Type, isEnabled: Bool, move: (ReorderDifference<ItemID, CollectionID>) -> ()) -> some View](./view/reordercontainer%28for,itemid,in,isenabled,move%29.md)
  Defines a container of reorderable views, with a type and keypath you use to identify items and a type you use to identify collections.
- [func reorderDestination<Item, CollectionID>(for: Item.Type, in: CollectionID.Type) -> ReorderDifference<Item.ID, CollectionID>.Destination?](./dropsession/reorderdestination%28for,in%29.md)
  Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier.
- [func reorderDestination<Item, ItemID, CollectionID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, in: CollectionID.Type) -> ReorderDifference<ItemID, CollectionID>.Destination?](./dropsession/reorderdestination%28for,itemid,in%29.md)
  Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier.
- [struct ReorderDifference](./reorderdifference.md)
  The difference that a reordering operation produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/making-a-card-game-with-drag-drop-and-reordering-in-swiftui)*