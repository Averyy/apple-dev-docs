# DropConfiguration

**Framework**: SwiftUI  
**Kind**: struct

Describes the behavior of the drop.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DropConfiguration
```

## Topics

### Initializers
- [init(operation: DropOperation)](dropconfiguration/init(operation:).md)
  Creates a configuration value with the operation chosen by the drop destination.
- [init<ItemID, CollectionID>(operation: DropOperation, destination: ReorderDifference<ItemID, CollectionID>.Destination)](dropconfiguration/init(operation:destination:).md)
  Creates a drop configuration with the provided operation and reorder destination.
### Instance Properties
- [var acceptedItemCount: Int?](dropconfiguration/accepteditemcount.md)
  Specifies the number of items that the drop side wants to accept.
- [var operation: DropOperation](dropconfiguration/operation.md)
  The drop operation that the drop chooses to perform.

## See Also

- [func dragConfiguration(DragConfiguration) -> some View](view/dragconfiguration(_:).md)
  Configures a drag session.
- [struct DragConfiguration](dragconfiguration.md)
  The behavior of the drag, proposed by the dragging source. A value that describes the drag operations a drag source supports.
- [func dropConfiguration((DropSession) -> DropConfiguration) -> some View](view/dropconfiguration(_:).md)
  Configures a drop session.
- [func dragContainer(for:in:_:)](view/dragcontainer(for:in:_:).md)
  A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [func dragContainer(for:itemID:in:_:)](view/dragcontainer(for:itemid:in:_:).md)
  A container with draggable views.
- [func dragContainerSelection<ItemID>(@autoclosure () -> Array<ItemID>, containerNamespace: Namespace.ID?) -> some View](view/dragcontainerselection(_:containernamespace:).md)
  Provides multiple item selection support for drag containers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropconfiguration)*