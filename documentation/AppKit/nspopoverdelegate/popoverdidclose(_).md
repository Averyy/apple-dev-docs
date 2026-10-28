# popoverDidClose(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the popover did close.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func popoverDidClose(_ notification: Notification)
```

```objc
- (void) popoverDidClose:(NSNotification *) notification;
```

## Discussion

Invoked on the delegate when the [`didCloseNotification`](../nspopover/didclosenotification.md) notification is sent.

This method will also be invoked on the delegate’s popover, if the method has been implemented.

## See Also

### Popover Visibility
- [func popoverShouldClose(NSPopover) -> Bool](./popovershouldclose%28_%29.md)
  Allows a delegate to override a close request.
- [func popoverWillShow(Notification)](./popoverwillshow%28_%29.md)
  Invoked when the popover will show.
- [func popoverDidShow(Notification)](./popoverdidshow%28_%29.md)
  Invoked when the popover has been shown.
- [func popoverWillClose(Notification)](./popoverwillclose%28_%29.md)
  Invoked when the popover is about to close.
- [func popoverDidDetach(NSPopover)](./popoverdiddetach%28_%29.md)
  Indicates that a popover has been released while it’s in an implicitly detached state.
- [func popoverShouldDetach(NSPopover) -> Bool](./popovershoulddetach%28_%29.md)
  Returns a Boolean value that indicates whether a popover should detach from its positioning view and become a separate window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopoverdelegate/popoverdidclose(_:))*