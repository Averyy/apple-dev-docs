# applicationSupportsShakeToEdit

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether shaking the device displays the undo-redo user interface.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var applicationSupportsShakeToEdit: Bool { get set }
```

```objc
@property (nonatomic) BOOL applicationSupportsShakeToEdit;
```

#### Discussion

The default value is [`true`](../../Swift/true.md). Set the property to [`false`](../../Swift/false.md) if you don’t want your app to display the Undo and Redo buttons when users shake the device.

## See Also

### Controlling and handling events
- [func sendEvent(UIEvent)](./sendevent%28_%29.md)
  Dispatches an event to the appropriate responder objects in the app.
- [func sendAction(Selector, to: Any?, from: Any?, for: UIEvent?) -> Bool](./sendaction%28_,to,from,for%29.md)
  Sends an action message identified by the selector to a specified target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/applicationsupportsshaketoedit)*