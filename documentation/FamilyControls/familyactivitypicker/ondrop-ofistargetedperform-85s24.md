# onDrop(of:isTargeted:perform:)

**Framework**: FamilyControls  
**Kind**: method

Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+

## Declaration

```swift
nonisolated
func onDrop(of supportedContentTypes: [UTType], isTargeted: Binding<Bool>?, perform action: @escaping ([NSItemProvider], CGPoint) -> Bool) -> some View
```

#### Return Value

A view that provides a drop destination for a drag operation of the specified types.

#### Discussion

The drop destination is the same size and position as this view.

Make sure to start loading the contents of `NSItemProvider` instances within the scope of the `action` closure. Do not perform loading asynchronously on a different actor. Loading the contents may finish later, but it must start here. For security reasons, the drop receiver can access the dropped payload only before this closure returns.

## Parameters

- `supportedContentTypes`: The uniform type identifiers that describe   the types of content this view can accept through drag and drop.   If the drag and drop operation doesn’t contain any of the supported   types, then this drop destination doesn’t activate and    doesn’t update.
- `isTargeted`: A binding that updates when a drag and drop operation   enters or exits the drop target area. The binding’s value is   when   the cursor is inside the area, and   when the cursor is outside.
- `action`: A closure that takes the dropped content and responds   appropriately. The first parameter to   contains the dropped   items, with types specified by  . The second   parameter contains the drop location in this view’s coordinate   space. Return   if the drop operation was successful;   otherwise, return  .

## See Also

- [func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View](familyactivitypicker/ondrag(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrag(() -> NSItemProvider) -> some View](familyactivitypicker/ondrag(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func itemProvider(Optional<() -> NSItemProvider?>) -> some View](familyactivitypicker/itemprovider(_:).md)
  Provides a closure that vends the drag representation to be used for a particular data element.
- [func onDrop(of: [UTType], delegate: any DropDelegate) -> some View](familyactivitypicker/ondrop(of:delegate:)-3ufe4.md)
  Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform: ([NSItemProvider]) -> Bool) -> some View](familyactivitypicker/ondrop(of:istargeted:perform:)-5tsvq.md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/ondrop(of:istargeted:perform:)-85s24)*