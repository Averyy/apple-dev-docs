# draggable(_:containerNamespace:)

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
func draggable<Item>(_ item: @autoclosure @escaping () -> Item, containerNamespace: Namespace.ID) -> some View where Item : Transferable, Item : Identifiable, Item.ID : Sendable
```

## Return Value

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

## Discussion

Applying the `draggable(_:containerNamespace:)` modifier adds the appropriate gestures for drag and drop to this view. When a drag operation begins, a rendering of this view is generated and used as the preview image.

Because the item conforms to `Identifiable`, SwiftUI stores its identifier in the drag session. Drop destinations in the same app read it through [`draggedItemIDs(for:)`](../dropsession/localsession-swift.struct/draggeditemids%28for%29.md), and an enclosing [`dragContainer(for:in:_:)`](./dragcontainer%28for,in,_%29.md) uses it to identify this item.

```swift
@Namespace private var bookshelf

ForEach(books) { book in
    BookRow(book)
        .draggable(book, containerNamespace: bookshelf)
}
```

## Parameters

- `item`: The item to drag.
- `containerNamespace`: A namespace of the associated drag container. Use it to distinguish between multiple drag containers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/draggable(_:containernamespace:))*