# setNeedsBodyUpdate()

**Framework**: SwiftUI  
**Kind**: method

Invalidates the current SwiftUI views and triggers an update during the next cycle.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency func setNeedsBodyUpdate()
```

#### Discussion

Call this method to mark the views of the hosting controller as needing an update. During the next update cycle, the hosting controller fetches an updated set of views from its [`body`](wkhostingcontroller/body.md) property.

## See Also

- [func updateBodyIfNeeded()](wkhostingcontroller/updatebodyifneeded.md)
  Updates the interface controller’s set of views immediately, if updates are pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkhostingcontroller/setneedsbodyupdate())*