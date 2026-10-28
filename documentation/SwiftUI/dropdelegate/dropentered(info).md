# dropEntered(info:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate a validated drop has entered the modified view.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func dropEntered(info: DropInfo)
```

## Discussion

The default implementation does nothing.

## Default Implementations

### DropDelegate Implementations
- [func dropEntered(info: DropInfo)](./dropentered%28info%29-2tqut.md)
  Tells the delegate a validated drop has entered the modified view.

## See Also

### Receiving drop information
- [func dropExited(info: DropInfo)](./dropexited%28info%29.md)
  Tells the delegate a validated drop operation has exited the modified view.
- [func dropUpdated(info: DropInfo) -> DropProposal?](./dropupdated%28info%29.md)
  Tells the delegate that a validated drop moved inside the modified view.
- [func validateDrop(info: DropInfo) -> Bool](./validatedrop%28info%29.md)
  Tells the delegate that a drop containing items conforming to one of the expected types entered a view that accepts drops.
- [func performDrop(info: DropInfo) -> Bool](./performdrop%28info%29.md)
  Tells the delegate it can request the item provider data from the given information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropdelegate/dropentered(info:))*