# unhideWithoutActivation()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Restores hidden windows without activating their owner (the receiver).

**Availability**:
- macOS

## Declaration

```swift
func unhideWithoutActivation()
```

```objc
- (void) unhideWithoutActivation;
```

#### Discussion

When this method begins, it posts an [`willUnhideNotification`](./willunhidenotification.md) to the default notification center. If it completes successfully, it posts an [`didUnhideNotification`](./didunhidenotification.md).

## See Also

### Related Documentation
- [func activate(ignoringOtherApps: Bool)](./activate%28ignoringotherapps%29.md)
  Makes the receiver the active app.
- [func applicationDidUnhide(Notification)](../nsapplicationdelegate/applicationdidunhide%28_%29.md)
  Tells the delegate that the app is now visible.
- [func applicationWillUnhide(Notification)](../nsapplicationdelegate/applicationwillunhide%28_%29.md)
  Tells the delegate that the app is about to become visible.
### Hiding Windows
- [var isHidden: Bool](./ishidden.md)
  A Boolean value indicating whether the app is hidden.
- [func hide(Any?)](./hide%28_%29.md)
  Hides all the receiver’s windows, and the next app in line is activated.
- [func unhide(Any?)](./unhide%28_%29.md)
  Restores hidden windows to the screen and makes the receiver active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/unhidewithoutactivation())*