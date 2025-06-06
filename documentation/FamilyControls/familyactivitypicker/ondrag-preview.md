# onDrag(_:preview:)

**Framework**: FamilyControls  
**Kind**: method

Activates this view as the source of a drag and drop operation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
nonisolated
func onDrag<V>(_ data: @escaping () -> NSItemProvider, @ViewBuilder preview: () -> V) -> some View where V : View
```

#### Return Value

A view that activates this view as the source of a drag-and- drop operation, beginning with user gesture input.

#### Discussion

Applying the `onDrag(_:preview:)` modifier adds the appropriate gestures for drag and drop to this view. When a drag operation begins, a rendering of `preview` is generated and used as the preview image.

To customize the lift preview, shown while the system transitions to show your custom `preview`, apply a `View/contentShape(_:_:eoFill:)` with a `ContentShapeKinds/dragPreview` kind. For example, you can change the preview’s corner radius or use a nested view as the preview.

## Parameters

- `data`: A closure that returns a single     that represents the draggable data from this view.
- `preview`: A   to use as the source for the dragging   preview, once the drag operation has begun. The preview is centered over   the source view.

## See Also

- [func onDrag(() -> NSItemProvider) -> some View](familyactivitypicker/ondrag(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func itemProvider(Optional<() -> NSItemProvider?>) -> some View](familyactivitypicker/itemprovider(_:).md)
  Provides a closure that vends the drag representation to be used for a particular data element.
- [func onDrop(of: [UTType], delegate: any DropDelegate) -> some View](familyactivitypicker/ondrop(of:delegate:)-3ufe4.md)
  Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform: ([NSItemProvider]) -> Bool) -> some View](familyactivitypicker/ondrop(of:istargeted:perform:)-5tsvq.md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform: ([NSItemProvider], CGPoint) -> Bool) -> some View](familyactivitypicker/ondrop(of:istargeted:perform:)-85s24.md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/ondrag(_:preview:))*