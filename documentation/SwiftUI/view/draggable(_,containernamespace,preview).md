# draggable(_:containerNamespace:preview:)

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
func draggable<Item, Preview>(_ item: @autoclosure @escaping () -> Item, containerNamespace: Namespace.ID, @ContentBuilder preview: () -> Preview) -> some View where Item : Transferable, Item : Identifiable, Preview : View, Item.ID : Sendable
```

## Return Value

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

## Discussion

This modifier behaves like [`draggable(_:containerNamespace:)`](./draggable%28_,containernamespace%29.md), except that a rendering of `preview` is used as the preview image instead of a rendering of this view. The preview is centered over the source view.

```swift
@Namespace private var bookshelf

ForEach(books) { book in
    BookRow(book)
        .draggable(book, containerNamespace: bookshelf) {
            BookCover(book)
        }
}
```

## Parameters

- `item`: The item to drag.
- `containerNamespace`: A namespace of the associated drag container. Use it to distinguish between multiple drag containers.
- `preview`: A view to use as the source for the dragging preview, after the drag operation begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/draggable(_:containernamespace:preview:))*