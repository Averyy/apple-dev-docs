# draggable(_:)

**Framework**: SwiftUI  
**Kind**: method

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

## Mentions

- [Making a view into a drag source](making-a-view-into-a-drag-source.md)

#### Return Value

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

#### Discussion

Applying the `draggable(_:)` modifier adds the appropriate gestures for drag and drop to this view. When a drag operation begins, a rendering of this view is generated and used as the preview image.

To customize the default preview, apply a [`contentShape(_:_:eoFill:)`](view/contentshape(_:_:eofill:).md) with a [`dragPreview`](contentshapekinds/dragpreview.md) kind. For example, you can change the preview’s corner radius or use a nested view as the preview.

## Parameters

- `payload`: A closure that returns a single   instance or a value conforming to   that   represents the draggable data from this view.

## See Also

- [func draggable<V, T>(@autoclosure () -> T, preview: () -> V) -> some View](view/draggable(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool, isTargeted: (Bool) -> Void) -> some View](view/dropdestination(for:action:istargeted:).md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/draggable(_:))*