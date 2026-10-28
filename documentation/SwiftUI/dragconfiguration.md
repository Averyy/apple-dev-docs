# DragConfiguration

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

## Overview

Pass a `DragConfiguration` to the [`dragConfiguration(_:)`](./view/dragconfiguration%28_%29.md) modifier to declare which operations — copy, move, or delete — a view supports when it is dragged.

### Opting in to move

By default, only copy is allowed. To support drag-to-move, where the source item is removed after a successful drop, initialize with `allowMove: true`:

```swift
.dragConfiguration(DragConfiguration(allowMove: true))
```

On macOS, users can override the proposed operation during a drag by holding modifier keys:

- **⌥ (Option)** proposes copy.
- **⌘ (Command)** proposes move.
- **⌥ + ⌘** proposes alias.

Modifier keys only take effect when the source supports the corresponding operation. For example, holding ⌘ has no effect unless `allowMove` is `true`.

### Responding to the performed operation

`DragConfiguration` communicates *suggested* operations to drop destinations, but each destination chooses which operation to perform. To detect which operation was ultimately performed — for example, to remove the source item after a successful move — observe the drag session using [`onDragSessionUpdated(_:)`](./view/ondragsessionupdated%28_%29.md):

```swift
.dragConfiguration(DragConfiguration(allowMove: true))
.onDragSessionUpdated { session in
    if session.phase == .ended(.move) {
        removeItem()
    }
}
```

> **See Also**: [`dragConfiguration(_:)`](./view/dragconfiguration%28_%29.md), [`onDragSessionUpdated(_:)`](./view/ondragsessionupdated%28_%29.md), [`suggestedOperations`](./dropsession/suggestedoperations.md)

## Topics

### Structures
- [DragConfiguration.OperationsOutsideApp](./dragconfiguration/operationsoutsideapp-swift.struct.md)
  Describes the suggested drag operations to other applications.
- [DragConfiguration.OperationsWithinApp](./dragconfiguration/operationswithinapp-swift.struct.md)
  Describes the drag operations suggested to destinations within the app.
### Initializers
- [init(allowMove: Bool)](./dragconfiguration/init%28allowmove%29.md)
  Creates a drag configuration that can support drag-to-move in addition to drag-to-copy.
- [init(allowMove: Bool, allowDelete: Bool)](./dragconfiguration/init%28allowmove,allowdelete%29.md)
  Creates a drag configuration that can support drag-to-move and drag-to-delete in addition to drag-to-copy.
- [init(operationsWithinApp: DragConfiguration.OperationsWithinApp, operationsOutsideApp: DragConfiguration.OperationsOutsideApp)](./dragconfiguration/init%28operationswithinapp,operationsoutsideapp%29.md)
  Creates a default drag configuration with operation `.copy` support for drags within the application and to other applications.
### Instance Properties
- [var operationsOutsideApp: DragConfiguration.OperationsOutsideApp](./dragconfiguration/operationsoutsideapp-swift.property.md)
  The operations suggested by the drag source for drags to other applications.
- [var operationsWithinApp: DragConfiguration.OperationsWithinApp](./dragconfiguration/operationswithinapp-swift.property.md)
  The operations suggested by the drag source for drags within the application.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Escapable](../Swift/escapable.md)

## See Also

### Configuring drag-and-drop behavior
- [func dragConfiguration(DragConfiguration) -> some View](./view/dragconfiguration%28_%29.md)
  Configures a drag session.
- [func dropConfiguration((DropSession) -> DropConfiguration) -> some View](./view/dropconfiguration%28_%29.md)
  Configures a drop session.
- [struct DropConfiguration](./dropconfiguration.md)
  Describes the behavior of the drop.
- [func dragContainer(for:in:_:)](./view/dragcontainer%28for,in,_%29.md)
  A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [func dragContainer(for:itemID:in:_:)](./view/dragcontainer%28for,itemid,in,_%29.md)
  A container with draggable views.
- [func dragContainerSelection<ItemID>(@autoclosure () -> Array<ItemID>, containerNamespace: Namespace.ID?) -> some View](./view/dragcontainerselection%28_,containernamespace%29.md)
  Provides multiple item selection support for drag containers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dragconfiguration)*