# Drag and drop

**Framework**: SwiftUI

Enable people to move or duplicate items by dragging them from one location to another.

#### Overview

Drag and drop offers people a convenient way to move content from one part of your app to another, from one app to another, or to reorder content using an intuitive dragging gesture. Support this feature in your app by adding view modifiers to potential source and destination views within your app’s interface.

![None](https://docs-assets.developer.apple.com/published/389cb904528e698574c83a1ccfbb85d9/drag-and-drop-hero%402x.png)

In your modifiers, provide or accept types that conform to the [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable) protocol, or that conform to [`NSItemProviderReading`](https://developer.apple.com/documentation/Foundation/NSItemProviderReading) and/or [`NSItemProviderWriting`](https://developer.apple.com/documentation/Foundation/NSItemProviderWriting). In Swift, prefer using transferable items.

For design guidance, see [`Drag and drop`](https://developer.apple.com/design/Human-Interface-Guidelines/drag-and-drop) in the Human Interface Guidelines.

## Topics

### Essentials
- [Adopting drag and drop using SwiftUI](adopting-drag-and-drop-using-swiftui.md)
  Enable drag-and-drop interactions in lists, tables and custom views.
- [Making a view into a drag source](making-a-view-into-a-drag-source.md)
  Adopt draggable API to provide items for drag-and-drop operations.
- [Reordering items in lists, stacks, grids, and custom layouts](reordering-items-in-lists-stacks-grids-and-custom-layouts.md)
  Add drag-to-reorder interactions to SwiftUI layouts using reordering modifiers.
### Configuring drag-and-drop behavior
- [func dragConfiguration(DragConfiguration) -> some View](view/dragconfiguration(_:).md)
  Configures a drag session.
- [struct DragConfiguration](dragconfiguration.md)
  The behavior of the drag, proposed by the dragging source. A value that describes the drag operations a drag source supports.
- [func dropConfiguration((DropSession) -> DropConfiguration) -> some View](view/dropconfiguration(_:).md)
  Configures a drop session.
- [struct DropConfiguration](dropconfiguration.md)
  Describes the behavior of the drop.
- [func dragContainer(for:in:_:)](view/dragcontainer(for:in:_:).md)
  A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [func dragContainer(for:itemID:in:_:)](view/dragcontainer(for:itemid:in:_:).md)
  A container with draggable views.
- [func dragContainerSelection<ItemID>(@autoclosure () -> Array<ItemID>, containerNamespace: Namespace.ID?) -> some View](view/dragcontainerselection(_:containernamespace:).md)
  Provides multiple item selection support for drag containers.
### Moving items
- [struct DragSession](dragsession.md)
  Describes the ongoing dragging session.
- [struct DropSession](dropsession.md)
### Moving transferable items
- [func draggable<T>(@autoclosure () -> T) -> some View](view/draggable(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<V, T>(@autoclosure () -> T, preview: () -> V) -> some View](view/draggable(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<Item>(Item.Type, containerNamespace: Namespace.ID?, () -> Item?) -> some View](view/draggable(_:containernamespace:_:).md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [func draggable<Item, ItemID>(Item.Type, id: KeyPath<Item, ItemID>, containerNamespace: Namespace.ID?, () -> Item?) -> some View](view/draggable(_:id:containernamespace:_:).md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [func draggable<Item, ItemID>(Item.Type, id: KeyPath<Item, ItemID>, item: @autoclosure () -> Item?, containerNamespace: Namespace.ID?) -> some View](view/draggable(_:id:item:containernamespace:).md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [func draggable<Item>(Item.Type, item: @autoclosure () -> Item?, containerNamespace: Namespace.ID?) -> some View](view/draggable(_:item:containernamespace:).md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [func draggable<ItemID>(containerItemID: ItemID, containerNamespace: Namespace.ID?) -> some View](view/draggable(containeritemid:containernamespace:).md)
  Inside a drag container, activates this view as the source of a drag and drop operation. Supports lazy drag containers.
### Moving items using item providers
- [func itemProvider(Optional<() -> NSItemProvider?>) -> some View](view/itemprovider(_:).md)
  Provides a closure that vends the drag representation to be used for a particular data element.
- [func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View](view/ondrag(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrag(() -> NSItemProvider) -> some View](view/ondrag(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrop(of:isTargeted:perform:)](view/ondrop(of:istargeted:perform:).md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [func onDrop(of:delegate:)](view/ondrop(of:delegate:).md)
  Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [protocol DropDelegate](dropdelegate.md)
  An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [struct DropProposal](dropproposal.md)
  The behavior of a drop.
- [enum DropOperation](dropoperation.md)
  Operation types that determine how a drag and drop session resolves when the user drops a drag item.
- [struct DropInfo](dropinfo.md)
  The current state of a drop.
### Reordering items
- [Making a card game with drag, drop, and reordering in SwiftUI](making-a-card-game-with-drag-drop-and-reordering-in-swiftui.md)
  Move cards between positions in a card game using drag, drop, and reordering modifiers.
- [func reorderable() -> some DynamicViewContent<Self.Data>
](dynamicviewcontent/reorderable.md)
  Enables reordering of views from this content inside the scope of a reorderable container modifier.
- [func reorderable(collectionID: some Hashable & Sendable) -> some DynamicViewContent<Self.Data>
](dynamicviewcontent/reorderable(collectionid:).md)
  Enables reordering views from this content within and between sections in the scope of a reorderable container modifier.
- [struct ReorderableSingleCollectionIdentifier](reorderablesinglecollectionidentifier.md)
  An opaque, empty type used to identify reorderable containers and modifiers with only a single collection.
- [func reorderContainer<Item>(for: Item.Type, isEnabled: Bool, move: (ReorderDifference<Item.ID, ReorderableSingleCollectionIdentifier>) -> ()) -> some View](view/reordercontainer(for:isenabled:move:).md)
  Defines a container of reorderable views.
- [func reorderContainer<Item, CollectionID>(for: Item.Type, in: CollectionID.Type, isEnabled: Bool, move: (ReorderDifference<Item.ID, CollectionID>) -> ()) -> some View](view/reordercontainer(for:in:isenabled:move:).md)
  Defines a container of reorderable views, with a type you specify to identify sections.
- [func reorderContainer<Item, ItemID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, isEnabled: Bool, move: (ReorderDifference<ItemID, ReorderableSingleCollectionIdentifier>) -> ()) -> some View](view/reordercontainer(for:itemid:isenabled:move:).md)
  Defines a container of reorderable views, with a type and keypath you specify to identify items.
- [func reorderContainer<Item, ItemID, CollectionID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, in: CollectionID.Type, isEnabled: Bool, move: (ReorderDifference<ItemID, CollectionID>) -> ()) -> some View](view/reordercontainer(for:itemid:in:isenabled:move:).md)
  Defines a container of reorderable views, with a type and keypath you use to identify items and a type you use to identify collections.
- [func reorderDestination<Item, CollectionID>(for: Item.Type, in: CollectionID.Type) -> ReorderDifference<Item.ID, CollectionID>.Destination?](dropsession/reorderdestination(for:in:).md)
  Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier.
- [func reorderDestination<Item, ItemID, CollectionID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, in: CollectionID.Type) -> ReorderDifference<ItemID, CollectionID>.Destination?](dropsession/reorderdestination(for:itemid:in:).md)
  Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier.
- [struct ReorderDifference](reorderdifference.md)
  The difference that a reordering operation produces.
### Describing preview formations
- [func dragPreviewsFormation(DragDropPreviewsFormation) -> some View](view/dragpreviewsformation(_:).md)
  Describes the way dragged previews are visually composed.
- [func dropPreviewsFormation(DragDropPreviewsFormation) -> some View](view/droppreviewsformation(_:).md)
  Describes the way previews for a drop are composed.
- [struct DragDropPreviewsFormation](dragdroppreviewsformation.md)
  On macOS, describes the way the dragged previews are visually composed. Both drag sources and drop destination can specify their desired preview formation.
### Configuring spring loading
- [func springLoadingBehavior(SpringLoadingBehavior) -> some View](view/springloadingbehavior(_:).md)
  Sets the spring loading behavior this view.
- [var springLoadingBehavior: SpringLoadingBehavior](environmentvalues/springloadingbehavior.md)
  The behavior of spring loaded interactions for the views associated with this environment.
- [struct SpringLoadingBehavior](springloadingbehavior.md)
  The options for controlling the spring loading behavior of views.

## See Also

- [Gestures](gestures.md)
  Define interactions from taps, clicks, and swipes to fine-grained gestures.
- [Input events](input-events.md)
  Respond to input from a hardware device, like a keyboard or a Touch Bar.
- [Clipboard](clipboard.md)
  Enable people to move or duplicate items by issuing Copy and Paste commands.
- [Focus](focus.md)
  Identify and control which visible object responds to user interaction.
- [System events](system-events.md)
  React to system events, like opening a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/drag-and-drop)*