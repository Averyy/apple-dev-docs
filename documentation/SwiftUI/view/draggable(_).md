# draggable(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Activates this view as the source of a drag and drop operation, preserving the identifier of the dragged item.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
nonisolated
func draggable<Item>(_ item: @autoclosure @escaping () -> Item) -> some View where Item : Transferable, Item : Identifiable, Item.ID : Sendable
```

**Other overloads**:

```swift
nonisolated
func draggable<T>(_ payload: @autoclosure @escaping () -> T) -> some View where T : Transferable
```

## Mentions

- [Making a view into a drag source](../making-a-view-into-a-drag-source.md)

## Return Value

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

## Discussion

Applying the `draggable(_:)` modifier adds the appropriate gestures for drag and drop to this view. When a drag operation begins, a rendering of this view is generated and used as the preview image.

Because the item conforms to `Identifiable`, SwiftUI stores its identifier in the drag session. Drop destinations in the same app read it through [`draggedItemIDs(for:)`](../dropsession/localsession-swift.struct/draggeditemids%28for%29.md), and an enclosing [`dragContainer(for:in:_:)`](./dragcontainer%28for,in,_%29.md) uses it to identify this item.

```swift
ForEach(books) { book in
    BookRow(book)
        .draggable(book)
}
```

## Parameters

- `item`: The item to drag.

## See Also

### Moving transferable items
- [func draggable(_:preview:)](./draggable%28_,preview%29.md)
  Activates this view as the source of a drag and drop operation with a custom preview, preserving the identifier of the dragged item.
- [func draggable<Item>(Item.Type, containerNamespace: Namespace.ID?, () -> Item?) -> some View](./draggable%28_,containernamespace,_%29.md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [func draggable<Item, ItemID>(Item.Type, id: KeyPath<Item, ItemID>, containerNamespace: Namespace.ID?, () -> Item?) -> some View](./draggable%28_,id,containernamespace,_%29.md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [func draggable<Item, ItemID>(Item.Type, id: KeyPath<Item, ItemID>, item: @autoclosure () -> Item?, containerNamespace: Namespace.ID?) -> some View](./draggable%28_,id,item,containernamespace%29.md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [func draggable<Item>(Item.Type, item: @autoclosure () -> Item?, containerNamespace: Namespace.ID?) -> some View](./draggable%28_,item,containernamespace%29.md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [func draggable<ItemID>(containerItemID: ItemID, containerNamespace: Namespace.ID?) -> some View](./draggable%28containeritemid,containernamespace%29.md)
  Inside a drag container, activates this view as the source of a drag and drop operation. Supports lazy drag containers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/draggable(_:))*