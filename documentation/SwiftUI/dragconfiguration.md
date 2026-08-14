# DragConfiguration

**Framework**: SwiftUI  
**Kind**: struct

The behavior of the drag, proposed by the dragging source. A value that describes the drag operations a drag source supports.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DragConfiguration
```

#### Overview

Pass a `DragConfiguration` to the [`dragConfiguration(_:)`](view/dragconfiguration(_:).md) modifier to declare which operations — copy, move, or delete — a view supports when it is dragged.

##### Opting in to Move

By default, only copy is allowed. To support drag-to-move, where the source item is removed after a successful drop, initialize with `allowMove: true`:

```swift
.dragConfiguration(DragConfiguration(allowMove: true))
```

On macOS, users can override the proposed operation during a drag by holding modifier keys:

- **⌥ (Option)** proposes copy.
- **⌘ (Command)** proposes move.
- **⌥ + ⌘** proposes alias.

Modifier keys only take effect when the source supports the corresponding operation. For example, holding ⌘ has no effect unless `allowMove` is `true`.

##### Responding to the Performed Operation

`DragConfiguration` communicates *suggested* operations to drop destinations, but each destination chooses which operation to perform. To detect which operation was ultimately performed — for example, to remove the source item after a successful move — observe the drag session using [`onDragSessionUpdated(_:)`](view/ondragsessionupdated(_:).md):

```swift
.dragConfiguration(DragConfiguration(allowMove: true))
.onDragSessionUpdated { session in
    if session.phase == .ended(.move) {
        removeItem()
    }
}
```

> **Note**: [`dragConfiguration(_:)`](view/dragconfiguration(_:).md), [`onDragSessionUpdated(_:)`](view/ondragsessionupdated(_:).md), [`suggestedOperations`](dropsession/suggestedoperations.md)

## Topics

### Structures
- [DragConfiguration.OperationsOutsideApp](dragconfiguration/operationsoutsideapp-swift.struct.md)
  Describes the suggested drag operations to other applications.
- [DragConfiguration.OperationsWithinApp](dragconfiguration/operationswithinapp-swift.struct.md)
  Describes the drag operations suggested to destinations within the app.
### Initializers
- [init(allowMove: Bool)](dragconfiguration/init(allowmove:).md)
  Creates a drag configuration that can support drag-to-move in addition to drag-to-copy.
- [init(allowMove: Bool, allowDelete: Bool)](dragconfiguration/init(allowmove:allowdelete:).md)
  Creates a drag configuration that can support drag-to-move and drag-to-delete in addition to drag-to-copy.
- [init(operationsWithinApp: DragConfiguration.OperationsWithinApp, operationsOutsideApp: DragConfiguration.OperationsOutsideApp)](dragconfiguration/init(operationswithinapp:operationsoutsideapp:).md)
  Creates a default drag configuration with operation `.copy` support for drags within the application and to other applications.
### Instance Properties
- [var operationsOutsideApp: DragConfiguration.OperationsOutsideApp](dragconfiguration/operationsoutsideapp-swift.property.md)
  The operations suggested by the drag source for drags to other applications.
- [var operationsWithinApp: DragConfiguration.OperationsWithinApp](dragconfiguration/operationswithinapp-swift.property.md)
  The operations suggested by the drag source for drags within the application.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [Escapable](../swift/escapable.md)

## See Also

- [func dragConfiguration(DragConfiguration) -> some View](view/dragconfiguration(_:).md)
  Configures a drag session.
- [func dropConfiguration((DropSession) -> DropConfiguration) -> some View](view/dropconfiguration(_:).md)
  Configures a drop session.
- [struct DropConfiguration](dropconfiguration.md)
  Describes the behavior of the drop.
- [func dragContainer(for:in:_:)](view/dragcontainer(for:in:_:).md)
  A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [func dragContainer(for:itemID:in:_:)](view/dragcontainer(for:itemid:in:_:).md)
  A container with draggable views.
- [func dragContainerSelection<ItemID>(@autoclosure () -> Array<ItemID>, containerNamespace: Namespace.ID?) -> some View](view/dragcontainerselection(_:containernamespace:).md)
  Provides multiple item selection support for drag containers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dragconfiguration)*