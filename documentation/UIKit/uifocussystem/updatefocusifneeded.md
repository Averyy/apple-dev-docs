# updateFocusIfNeeded()

**Framework**: UIKit  
**Kind**: method

Forces the system to act on a pending focus update for the current environment.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func updateFocusIfNeeded()
```

#### Discussion

If the current environment has a pending focus update, calling this method forces the system to update the focus information immediately instead of waiting for the next run loop cycle. If no focus update is pending, this method does nothing.

You create a pending focus update using the [`requestFocusUpdate(to:)`](uifocussystem/requestfocusupdate(to:).md) method. The system may also schedule focus updates in response to interface-related events.

## See Also

- [func requestFocusUpdate(to: any UIFocusEnvironment)](uifocussystem/requestfocusupdate(to:).md)
  Submits a request to update the focus state of the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocussystem/updatefocusifneeded())*