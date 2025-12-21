# draggable(_:id:item:containerNamespace:)

**Framework**: SwiftUI  
**Kind**: method

Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.

**Availability**:
- macOS 26.0+

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
- `containerNamespace`: A namespace of the associated drag container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/draggable(_:id:item:containernamespace:))*