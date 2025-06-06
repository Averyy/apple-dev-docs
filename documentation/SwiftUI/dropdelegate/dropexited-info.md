# dropExited(info:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Tells the delegate a validated drop operation has exited the modified view.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func dropExited(info: DropInfo)
```

#### Discussion

The default implementation does nothing.

## See Also

- [func dropEntered(info: DropInfo)](dropdelegate/dropentered(info:).md)
  Tells the delegate a validated drop has entered the modified view.
- [func dropUpdated(info: DropInfo) -> DropProposal?](dropdelegate/dropupdated(info:).md)
  Tells the delegate that a validated drop moved inside the modified view.
- [func validateDrop(info: DropInfo) -> Bool](dropdelegate/validatedrop(info:).md)
  Tells the delegate that a drop containing items conforming to one of the expected types entered a view that accepts drops.
- [func performDrop(info: DropInfo) -> Bool](dropdelegate/performdrop(info:).md)
  Tells the delegate it can request the item provider data from the given information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropdelegate/dropexited(info:))*