# sendAction(_:to:from:for:)

**Framework**: UIKit  
**Kind**: method

Sends an action message identified by the selector to a specified target.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func sendAction(_ action: Selector, to target: Any?, from sender: Any?, for event: UIEvent?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if a responder object handled the action message, [`false`](https://developer.apple.com/documentation/swift/false) if no object in the responder chain handled the message.

#### Discussion

Normally, this method is invoked by a [`UIControl`](uicontrol.md) object that the user has touched. The default implementation dispatches the action method to the given target object or, if no target is specified, to the first responder. Subclasses may override this method to perform special dispatching of action messages.

By default, this method pushes two parameters when calling the target. These last two parameters are optional for the receiver because it is up to the caller (usually a [`UIControl`](uicontrol.md) object) to remove any parameters it added. This design enables the action selector to be one of the following:

- `- (void)action`
- `- (void)action:(id)sender`
- `- (void)action:(id)sender forEvent:(UIEvent *)event`

## Parameters

- `action`: A selector identifying an action method. See the discussion for information on the permitted selector forms.
- `target`: The object to receive the action message. If   is  , the app sends the message to the first responder, from whence it progresses up the responder chain until it is handled.
- `sender`: The object that is sending the action message. The default sender is the   object that invokes this method.
- `event`: A   object that encapsulates information about the event originating the action message.

## See Also

- [func sendEvent(UIEvent)](uiapplication/sendevent(_:).md)
  Dispatches an event to the appropriate responder objects in the app.
- [var applicationSupportsShakeToEdit: Bool](uiapplication/applicationsupportsshaketoedit.md)
  A Boolean value that determines whether shaking the device displays the undo-redo user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/sendaction(_:to:from:for:))*