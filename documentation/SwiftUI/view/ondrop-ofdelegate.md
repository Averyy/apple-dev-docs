# onDrop(of:delegate:)

**Framework**: SwiftUI  
**Kind**: method

Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

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

- [func itemProvider(Optional<() -> NSItemProvider?>) -> some View](view/itemprovider(_:).md)
  Provides a closure that vends the drag representation to be used for a particular data element.
- [func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View](view/ondrag(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrag(() -> NSItemProvider) -> some View](view/ondrag(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrop(of:isTargeted:perform:)](view/ondrop(of:istargeted:perform:).md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [protocol DropDelegate](dropdelegate.md)
  An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [struct DropProposal](dropproposal.md)
  The behavior of a drop.
- [enum DropOperation](dropoperation.md)
  Operation types that determine how a drag and drop session resolves when the user drops a drag item.
- [struct DropInfo](dropinfo.md)
  The current state of a drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/ondrop(of:delegate:))*