# hide(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Hides all the receiver’s windows, and the next app in line is activated.

**Availability**:
- macOS

## Declaration

```swift
func hide(_ sender: Any?)
```

```objc
- (void) hide:(id) sender;
```

#### Discussion

This method is usually invoked when the user chooses Hide in the app’s main menu. When this method begins, it posts an [`willHideNotification`](./willhidenotification.md) to the default notification center. When it completes successfully, it posts an [`didHideNotification`](./didhidenotification.md).

## Parameters

- `sender`: The object that sent the command.

## See Also

### Related Documentation
- [func miniaturizeAll(Any?)](./miniaturizeall%28_%29.md)
  Miniaturizes all the receiver’s windows.
- [func applicationDidHide(Notification)](../nsapplicationdelegate/applicationdidhide%28_%29.md)
  Tells the delegate that the app is now hidden.
- [func applicationWillHide(Notification)](../nsapplicationdelegate/applicationwillhide%28_%29.md)
  Tells the delegate that the app is about to be hidden.
### Hiding Windows
- [var isHidden: Bool](./ishidden.md)
  A Boolean value indicating whether the app is hidden.
- [func unhide(Any?)](./unhide%28_%29.md)
  Restores hidden windows to the screen and makes the receiver active.
- [func unhideWithoutActivation()](./unhidewithoutactivation%28%29.md)
  Restores hidden windows without activating their owner (the receiver).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/hide(_:))*