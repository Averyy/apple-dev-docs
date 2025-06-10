# Drag and drop

**Framework**: SwiftUI

Enable people to move or duplicate items by dragging them from one location to another.

#### Overview

Drag and drop offers people a convenient way to move content from one part of your app to another, or from one app to another, using an intuitive dragging gesture. Support this feature in your app by adding view modifiers to potential source and destination views within your app’s interface.

![None](https://docs-assets.developer.apple.com/published/389cb904528e698574c83a1ccfbb85d9/drag-and-drop-hero%402x.png)

In your modifiers, provide or accept types that conform to the [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable) protocol, or that inherit from the [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) class. When possible, prefer using transferable items.

For design guidance, see [`Drag and drop`](https://developer.apple.com/design/Human-Interface-Guidelines/drag-and-drop) in the Human Interface Guidelines.

## Topics

### Essentials
- [Adopting drag and drop using SwiftUI](adopting-drag-and-drop-using-swiftui.md)
  Enable drag-and-drop interactions in lists, tables and custom views.
- [Making a view into a drag source](making-a-view-into-a-drag-source.md)
  Adopt draggable API to provide items for drag-and-drop operations.
### Configuring drag and drop behavior
- [struct DragConfiguration](dragconfiguration.md)
  The behavior of the drag, proposed by the dragging source.
- [struct DropConfiguration](dropconfiguration.md)
  Describes the behavior of the drop.
### Moving items
- [struct DragSession](dragsession.md)
  Describes the ongoing dragging session.
- [struct DropSession](dropsession.md)
### Moving transferable items
- [func draggable<T>(@autoclosure () -> T) -> some View](view/draggable(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<V, T>(@autoclosure () -> T, preview: () -> V) -> some View](view/draggable(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool, isTargeted: (Bool) -> Void) -> some View](view/dropdestination(for:action:istargeted:).md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
### Moving items using item providers
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
- [enum DropOperation](dropoperation.md)
  Operation types that determine how a drag and drop session resolves when the user drops a drag item.
- [struct DropInfo](dropinfo.md)
  The current state of a drop.
### Describing preview formations
- [struct DragDropPreviewsFormation](dragdroppreviewsformation.md)
  On macOS, describes the way the dragged previews are visually composed. Both drag sources and drop destination can specify their desired preview formation.
### Configuring spring loading
- [func springLoadingBehavior(SpringLoadingBehavior) -> some View](view/springloadingbehavior(_:).md)
  Sets the spring loading behavior this view.
- [var springLoadingBehavior: SpringLoadingBehavior](environmentvalues/springloadingbehavior.md)
  The behavior of spring loaded interactions for the views associated with this environment.
- [struct SpringLoadingBehavior](springloadingbehavior.md)
  The options for controlling the spring loading behavior of views.

## See Also

- [Gestures](gestures.md)
  Define interactions from taps, clicks, and swipes to fine-grained gestures.
- [Input events](input-events.md)
  Respond to input from a hardware device, like a keyboard or a Touch Bar.
- [Clipboard](clipboard.md)
  Enable people to move or duplicate items by issuing Copy and Paste commands.
- [Focus](focus.md)
  Identify and control which visible object responds to user interaction.
- [System events](system-events.md)
  React to system events, like opening a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/drag-and-drop)*