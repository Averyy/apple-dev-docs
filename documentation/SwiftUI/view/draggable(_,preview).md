# draggable(_:preview:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Activates this view as the source of a drag and drop operation with a custom preview, preserving the identifier of the dragged item.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
nonisolated
func draggable<Item, Preview>(_ item: @autoclosure @escaping () -> Item, @ContentBuilder preview: () -> Preview) -> some View where Item : Transferable, Item : Identifiable, Preview : View, Item.ID : Sendable
```

**Other overloads**:

```swift
nonisolated
func draggable<V, T>(_ payload: @autoclosure @escaping () -> T, @ContentBuilder preview: () -> V) -> some View where V : View, T : Transferable
```

## Mentions

- [Making a view into a drag source](../making-a-view-into-a-drag-source.md)

## Return Value

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

## Discussion

This modifier behaves like [`draggable(_:)`](./draggable%28_%29.md), except that a rendering of `preview` is used as the preview image instead of a rendering of this view. The preview is centered over the source view.

```swift
ForEach(books) { book in
    BookRow(book)
        .draggable(book) {
            BookCover(book)
        }
}
```

## Parameters

- `item`: The item to drag.
- `preview`: A view to use as the source for the dragging preview, after the drag operation begins.

## See Also

### Moving transferable items
- [func draggable(_:)](./draggable%28_%29.md)
  Activates this view as the source of a drag and drop operation, preserving the identifier of the dragged item.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/draggable(_:preview:))*