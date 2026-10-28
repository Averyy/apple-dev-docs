# DropDelegate

**Framework**: SwiftUI  
**Kind**: protocol  
**Role**: Protocol

An interface that you implement to interact with a drop operation in a view modified to accept drops.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol DropDelegate
```

## Overview

The [`DropDelegate`](./dropdelegate.md) protocol provides a comprehensive and flexible way to interact with a drop operation. Specify a drop delegate when you modify a view to accept drops with the [`onDrop(of:delegate:)`](./view/ondrop%28of,delegate%29.md) method.

Alternatively, for simple drop cases that don’t require the full functionality of a drop delegate, you can modify a view to accept drops using the [`onDrop(of:isTargeted:perform:)`](./view/ondrop%28of,istargeted,perform%29.md) method. This method handles the drop using a closure you provide as part of the modifier.

## Topics

### Receiving drop information
- [func dropEntered(info: DropInfo)](./dropdelegate/dropentered%28info%29.md)
  Tells the delegate a validated drop has entered the modified view.
- [func dropExited(info: DropInfo)](./dropdelegate/dropexited%28info%29.md)
  Tells the delegate a validated drop operation has exited the modified view.
- [func dropUpdated(info: DropInfo) -> DropProposal?](./dropdelegate/dropupdated%28info%29.md)
  Tells the delegate that a validated drop moved inside the modified view.
- [func validateDrop(info: DropInfo) -> Bool](./dropdelegate/validatedrop%28info%29.md)
  Tells the delegate that a drop containing items conforming to one of the expected types entered a view that accepts drops.
- [func performDrop(info: DropInfo) -> Bool](./dropdelegate/performdrop%28info%29.md)
  Tells the delegate it can request the item provider data from the given information.

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
- [struct DropProposal](./dropproposal.md)
  The behavior of a drop.
- [enum DropOperation](./dropoperation.md)
  Operation types that determine how a drag and drop session resolves when the user drops a drag item.
- [struct DropInfo](./dropinfo.md)
  The current state of a drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropdelegate)*