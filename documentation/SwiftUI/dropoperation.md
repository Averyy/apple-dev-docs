# DropOperation

**Framework**: SwiftUI  
**Kind**: enum

Operation types that determine how a drag and drop session resolves when the user drops a drag item.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
enum DropOperation
```

## Topics

### Getting operation types
- [DropOperation.cancel](dropoperation/cancel.md)
  Cancel the drag operation and transfer no data.
- [DropOperation.copy](dropoperation/copy.md)
  Copy the data to the modified view.
- [DropOperation.forbidden](dropoperation/forbidden.md)
  The drop activity is not allowed at this time or location.
- [DropOperation.move](dropoperation/move.md)
  Move the data represented by the drag items instead of copying it.
### Structures
- [DropOperation.Set](dropoperation/set.md)
  A set of drop operations, corresponding to matching cases in `DropOperation`.
### Enumeration Cases
- [DropOperation.alias](dropoperation/alias.md)
- [DropOperation.delete](dropoperation/delete.md)
  Delete the data. The item was dragged to Trash or to another destination that semantically represents deletion.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func itemProvider(Optional<() -> NSItemProvider?>) -> some View](view/itemprovider(_:).md)
  Provides a closure that vends the drag representation to be used for a particular data element.
- [func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View](view/ondrag(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrag(() -> NSItemProvider) -> some View](view/ondrag(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrop(of:isTargeted:perform:)](view/ondrop(of:istargeted:perform:).md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [func onDrop(of:delegate:)](view/ondrop(of:delegate:).md)
  Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [protocol DropDelegate](dropdelegate.md)
  An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [struct DropProposal](dropproposal.md)
  The behavior of a drop.
- [struct DropInfo](dropinfo.md)
  The current state of a drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropoperation)*