# popoverWillShow(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the popover will show.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func popoverWillShow(_ notification: Notification)
```

```objc
- (void) popoverWillShow:(NSNotification *) notification;
```

## Discussion

Invoked on the delegate when the [`willShowNotification`](../nspopover/willshownotification.md) notification is sent.

This method will also be invoked on the delegate’s popover, if the method has been implemented.

## See Also

### Popover Visibility
- [func popoverShouldClose(NSPopover) -> Bool](./popovershouldclose%28_%29.md)
  Allows a delegate to override a close request.
- [func popoverDidShow(Notification)](./popoverdidshow%28_%29.md)
  Invoked when the popover has been shown.
- [func popoverWillClose(Notification)](./popoverwillclose%28_%29.md)
  Invoked when the popover is about to close.
- [func popoverDidClose(Notification)](./popoverdidclose%28_%29.md)
  Invoked when the popover did close.
- [func popoverDidDetach(NSPopover)](./popoverdiddetach%28_%29.md)
  Indicates that a popover has been released while it’s in an implicitly detached state.
- [func popoverShouldDetach(NSPopover) -> Bool](./popovershoulddetach%28_%29.md)
  Returns a Boolean value that indicates whether a popover should detach from its positioning view and become a separate window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopoverdelegate/popoverwillshow(_:))*