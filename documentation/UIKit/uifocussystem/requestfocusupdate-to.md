# requestFocusUpdate(to:)

**Framework**: UIKit  
**Kind**: method

Submits a request to update the focus state of the specified object.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func requestFocusUpdate(to environment: any UIFocusEnvironment)
```

#### Discussion

Use this method to ask the focus engine to update the focus-related information for the specified object. If the update request is accepted, the focus engine updates the object’s focus-related information during the next run loop cycle. If the specified object does not contain a focused item, calling this method has no effect.

## Parameters

- `environment`: The view, view controller, window, or other object that you want to update. You can specify any object that adopts the   protocol.

## See Also

- [func updateFocusIfNeeded()](uifocussystem/updatefocusifneeded.md)
  Forces the system to act on a pending focus update for the current environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocussystem/requestfocusupdate(to:))*