# onDrop(of:isTargeted:perform:)

**Framework**: SwiftUI  
**Kind**: method

Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func onDrop(of supportedContentTypes: [UTType], isTargeted: Binding<Bool>?, perform action: @escaping ([NSItemProvider]) -> Bool) -> some View
```

#### Return Value

A view that provides a drop destination for a drag operation of the specified types.

#### Discussion

The drop destination is the same size and position as this view.

Make sure to start loading the contents of `NSItemProvider` instances within the scope of the `action` closure. Do not perform loading asynchronously on a different actor. Loading the contents may finish later, but it must start here. For security reasons, the drop receiver can access the dropped payload only before this closure returns.

## Parameters

- `supportedContentTypes`: The uniform type identifiers that describe the   types of content this view can accept through drag and drop.   If the drag-and-drop operation doesn’t contain any of the supported   types, then this drop destination doesn’t activate and    doesn’t update.
- `isTargeted`: A binding that updates when a drag and drop operation   enters or exits the drop target area. The binding’s value is   when   the cursor is inside the area, and   when the cursor is outside.
- `action`: A closure that takes the dropped content and responds   appropriately. The parameter to   contains the dropped   items, with types specified by  . Return    if the drop operation was successful; otherwise, return  .

## See Also

- [func itemProvider(Optional<() -> NSItemProvider?>) -> some View](view/itemprovider(_:).md)
  Provides a closure that vends the drag representation to be used for a particular data element.
- [func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View](view/ondrag(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrag(() -> NSItemProvider) -> some View](view/ondrag(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrop(of:delegate:)](view/ondrop(of:delegate:).md)
  Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [protocol DropDelegate](dropdelegate.md)
  An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [struct DropProposal](dropproposal.md)
  The behavior of a drop.
- [enum DropOperation](dropoperation.md)
  Operation types that determine how a drag and drop session resolves when the user drops a drag item.
- [struct DropInfo](dropinfo.md)
  The current state of a drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/ondrop(of:istargeted:perform:))*