# sendEvent(_:)

**Framework**: UIKit  
**Kind**: method

Dispatches an event to the appropriate responder objects in the app.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func sendEvent(_ event: UIEvent)
```

#### Discussion

If you require it, you can intercept incoming events by subclassing [`UIApplication`](uiapplication.md) and overriding this method. For every event you intercept, you must dispatch it by calling `[super sendEvent:event]` after handling the event in your implementation.

## Parameters

- `event`: A   object encapsulating the information about an event, including the touches involved.

## See Also

- [func sendAction(Selector, to: Any?, from: Any?, for: UIEvent?) -> Bool](uiapplication/sendaction(_:to:from:for:).md)
  Sends an action message identified by the selector to a specified target.
- [var applicationSupportsShakeToEdit: Bool](uiapplication/applicationsupportsshaketoedit.md)
  A Boolean value that determines whether shaking the device displays the undo-redo user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/sendevent(_:))*