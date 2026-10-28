# updateBodyIfNeeded()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Updates the interface controller’s set of views immediately, if updates are pending.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency func updateBodyIfNeeded()
```

## Discussion

Calling this method forces the hosting controller to update its current set of views, but only if there are pending changes. If there are no pending changes, this method does nothing.

To mark the interface controller as needing an update, call [`setNeedsBodyUpdate()`](./setneedsbodyupdate%28%29.md).

## See Also

### Updating the root view
- [func setNeedsBodyUpdate()](./setneedsbodyupdate%28%29.md)
  Invalidates the current SwiftUI views and triggers an update during the next cycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkhostingcontroller/updatebodyifneeded())*