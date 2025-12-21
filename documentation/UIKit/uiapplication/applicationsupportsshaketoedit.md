# applicationSupportsShakeToEdit

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether shaking the device displays the undo-redo user interface.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var applicationSupportsShakeToEdit: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/Swift/true). Set the property to [`false`](https://developer.apple.com/documentation/Swift/false) if you don’t want your app to display the Undo and Redo buttons when users shake the device.

## See Also

- [func sendEvent(UIEvent)](uiapplication/sendevent(_:).md)
  Dispatches an event to the appropriate responder objects in the app.
- [func sendAction(Selector, to: Any?, from: Any?, for: UIEvent?) -> Bool](uiapplication/sendaction(_:to:from:for:).md)
  Sends an action message identified by the selector to a specified target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/applicationsupportsshaketoedit)*