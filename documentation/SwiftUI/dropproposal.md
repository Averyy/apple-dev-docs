# DropProposal

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The behavior of a drop.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
struct DropProposal
```

## Topics

### Creating a drop proposal
- [init(operation: DropOperation)](./dropproposal/init%28operation%29.md)
- [let operation: DropOperation](./dropproposal/operation.md)
  The drop operation that the drop proposes to perform.
### Initializers
- [init(withinApplication: DropOperation, outsideApplication: DropOperation)](./dropproposal/init%28withinapplication,outsideapplication%29.md)
### Instance Properties
- [let operationOutsideApplication: DropOperation?](./dropproposal/operationoutsideapplication.md)
  The drop operation for drops outside the source application.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Moving items using item providers
- [func itemProvider(Optional<() -> NSItemProvider?>) -> some View](./view/itemprovider%28_%29.md)
  Provides a closure that vends the drag representation to be used for a particular data element.
- [func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View](./view/ondrag%28_,preview%29.md)
  Activates this view as the source of a drag and drop operation.
- [func onDrag(() -> NSItemProvider) -> some View](./view/ondrag%28_%29.md)
  Activates this view as the source of a drag and drop operation.
- [func onDrop(of:isTargeted:perform:)](./view/ondrop%28of,istargeted,perform%29.md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [func onDrop(of:delegate:)](./view/ondrop%28of,delegate%29.md)
  Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [protocol DropDelegate](./dropdelegate.md)
  An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [enum DropOperation](./dropoperation.md)
  Operation types that determine how a drag and drop session resolves when the user drops a drag item.
- [struct DropInfo](./dropinfo.md)
  The current state of a drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropproposal)*