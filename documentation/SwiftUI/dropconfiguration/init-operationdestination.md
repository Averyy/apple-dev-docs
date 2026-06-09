# init(operation:destination:)

**Framework**: SwiftUI  
**Kind**: init

Creates a drop configuration with the provided operation and reorder destination.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init<ItemID, CollectionID>(operation: DropOperation, destination: ReorderDifference<ItemID, CollectionID>.Destination) where ItemID : Hashable, ItemID : Sendable, CollectionID : Hashable, CollectionID : Sendable
```

#### Discussion

Use this initializer when you want to decide where the destination value of the current reordering session should be. The value that you pass to this initializer will be the value used for this update.

If you don’t want to update the destination value, or your [`dropDestination(for:isEnabled:action:)`](view/dropdestination(for:isenabled:action:).md) is not configured with a `View/reorderContainer(for:in:move:)`, use the initializer variant that takes only a `DropOperation`.

- operation: The drop operation that the drop destination chooses to perform on the drop.
- destination: The destination value for the reordering operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropconfiguration/init(operation:destination:))*