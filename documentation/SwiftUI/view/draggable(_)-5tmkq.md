# draggable(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Activates this view as the source of a drag and drop operation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func draggable<T>(_ payload: @autoclosure @escaping () -> T) -> some View where T : Transferable
```

**Other overloads**:

```swift
nonisolated
func draggable<Item>(_ item: @autoclosure @escaping () -> Item) -> some View where Item : Transferable, Item : Identifiable, Item.ID : Sendable
```

## Return Value

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

## Discussion

Applying the `draggable(_:)` modifier adds the appropriate gestures for drag and drop to this view. When a drag operation begins, a rendering of this view is generated and used as the preview image.

To customize the default preview, apply a [`contentShape(_:_:eoFill:)`](./contentshape%28_,_,eofill%29.md) with a [`dragPreview`](../contentshapekinds/dragpreview.md) kind. For example, you can change the preview’s corner radius or use a nested view as the preview.

> ❗ **Important**: Don’t perform work on the main actor while exporting the item. Doing so isn’t supported and might cause a hang. Make sure `T`‘s exporting closure doesn’t dispatch to the main actor.

## Parameters

- `payload`: A closure that returns a single instance or a value conforming to [`Transferable`](../../CoreTransferable/transferable.md) that represents the draggable data from this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/draggable(_:)-5tmkq)*