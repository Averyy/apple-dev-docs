# performDrop(info:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Tells the delegate it can request the item provider data from the given information.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func performDrop(info: DropInfo) -> Bool
```

#### Return Value

A Boolean that is `true` if the drop was successful, `false` otherwise.

#### Discussion

Incorporate the received data into your app’s data model as appropriate.

Make sure to start loading the contents of `NSItemProvider` instances from [`DropInfo`](dropinfo.md) within the scope of this method. Do not perform loading asynchronously on a different actor. Loading the contents may finish later, but it must start here. For security reasons, the drop receiver can access the dropped payload only before this method returns.

## See Also

- [func dropEntered(info: DropInfo)](dropdelegate/dropentered(info:).md)
  Tells the delegate a validated drop has entered the modified view.
- [func dropExited(info: DropInfo)](dropdelegate/dropexited(info:).md)
  Tells the delegate a validated drop operation has exited the modified view.
- [func dropUpdated(info: DropInfo) -> DropProposal?](dropdelegate/dropupdated(info:).md)
  Tells the delegate that a validated drop moved inside the modified view.
- [func validateDrop(info: DropInfo) -> Bool](dropdelegate/validatedrop(info:).md)
  Tells the delegate that a drop containing items conforming to one of the expected types entered a view that accepts drops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropdelegate/performdrop(info:))*