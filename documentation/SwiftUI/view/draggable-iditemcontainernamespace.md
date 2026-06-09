# draggable(_:id:item:containerNamespace:)

**Framework**: SwiftUI  
**Kind**: method

Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 26.0+
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func draggable<Item, ItemID>(_ itemType: Item.Type = Item.self, id: KeyPath<Item, ItemID>, item: @autoclosure @escaping () -> Item?, containerNamespace: Namespace.ID? = nil) -> some View where Item : Transferable, ItemID : Hashable, ItemID : Sendable
```

#### Return Value

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

#### Discussion

Applying the `draggable(_:containerNamespace_:)` modifier adds the appropriate gestures for drag and drop to this view. When a drag operation begins, a rendering of this view is generated and used as the preview image.

To customize the default preview, apply a [`contentShape(_:_:eoFill:)`](view/contentshape(_:_:eofill:).md) with a [`dragPreview`](contentshapekinds/dragpreview.md) kind. For example, you can change the preview’s corner radius or use a nested view as the preview.

## Parameters

- `itemType`: A type of the dragged item.
- `id`: An identifier of an item.
- `item`: A closure that returns a single instance or a value conforming to [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable) that represents the draggable data from this view.
- `containerNamespace`: A namespace of the associated drag container.

## See Also

- [func draggable<T>(@autoclosure () -> T) -> some View](view/draggable(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<V, T>(@autoclosure () -> T, preview: () -> V) -> some View](view/draggable(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<Item>(Item.Type, containerNamespace: Namespace.ID?, () -> Item?) -> some View](view/draggable(_:containernamespace:_:).md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [func draggable<Item, ItemID>(Item.Type, id: KeyPath<Item, ItemID>, containerNamespace: Namespace.ID?, () -> Item?) -> some View](view/draggable(_:id:containernamespace:_:).md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [func draggable<Item>(Item.Type, item: @autoclosure () -> Item?, containerNamespace: Namespace.ID?) -> some View](view/draggable(_:item:containernamespace:).md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [func draggable<ItemID>(containerItemID: ItemID, containerNamespace: Namespace.ID?) -> some View](view/draggable(containeritemid:containernamespace:).md)
  Inside a drag container, activates this view as the source of a drag and drop operation. Supports lazy drag containers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/draggable(_:id:item:containernamespace:))*