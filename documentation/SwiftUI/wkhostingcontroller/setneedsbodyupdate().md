# setNeedsBodyUpdate()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Invalidates the current SwiftUI views and triggers an update during the next cycle.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency func setNeedsBodyUpdate()
```

## Discussion

Call this method to mark the views of the hosting controller as needing an update. During the next update cycle, the hosting controller fetches an updated set of views from its [`body`](./body.md) property.

## See Also

### Updating the root view
- [func updateBodyIfNeeded()](./updatebodyifneeded%28%29.md)
  Updates the interface controller’s set of views immediately, if updates are pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkhostingcontroller/setneedsbodyupdate())*