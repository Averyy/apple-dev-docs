# onDrop(of:delegate:)

**Framework**: FamilyControls  
**Kind**: method

Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+

## Declaration

```swift
nonisolated
func onDrop(of supportedContentTypes: [UTType], delegate: any DropDelegate) -> some View
```

#### Return Value

A view that provides a drop destination for a drag operation of the specified types.

## Parameters

- `supportedContentTypes`: The uniform type identifiers that describe the   types of content this view can accept through drag and drop.   If the drag and drop operation doesn’t contain any of the supported   types, then this drop destination doesn’t activate and    doesn’t update.
- `delegate`: A type that conforms to the   protocol. You   have comprehensive control over drop behavior when you use a   delegate.

## See Also

- [func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View](familyactivitypicker/ondrag(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrag(() -> NSItemProvider) -> some View](familyactivitypicker/ondrag(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func itemProvider(Optional<() -> NSItemProvider?>) -> some View](familyactivitypicker/itemprovider(_:).md)
  Provides a closure that vends the drag representation to be used for a particular data element.
- [func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform: ([NSItemProvider]) -> Bool) -> some View](familyactivitypicker/ondrop(of:istargeted:perform:)-5tsvq.md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform: ([NSItemProvider], CGPoint) -> Bool) -> some View](familyactivitypicker/ondrop(of:istargeted:perform:)-85s24.md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/ondrop(of:delegate:)-3ufe4)*