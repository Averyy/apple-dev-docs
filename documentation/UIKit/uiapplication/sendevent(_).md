# sendEvent(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Dispatches an event to the appropriate responder objects in the app.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func sendEvent(_ event: UIEvent)
```

```objc
- (void) sendEvent:(UIEvent *) event;
```

## Discussion

If you require it, you can intercept incoming events by subclassing [`UIApplication`](../uiapplication.md) and overriding this method. For every event you intercept, you must dispatch it by calling `[super sendEvent:event]` after handling the event in your implementation.

## Parameters

- `event`: A [`UIEvent`](../uievent.md) object encapsulating the information about an event, including the touches involved.

## See Also

### Controlling and handling events
- [func sendAction(Selector, to: Any?, from: Any?, for: UIEvent?) -> Bool](./sendaction%28_,to,from,for%29.md)
  Sends an action message identified by the selector to a specified target.
- [var applicationSupportsShakeToEdit: Bool](./applicationsupportsshaketoedit.md)
  A Boolean value that determines whether shaking the device displays the undo-redo user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/sendevent(_:))*