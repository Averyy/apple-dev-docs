# popoverDidClose(_:)

**Framework**: AppKit  
**Kind**: method

Invoked when the popover did close.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func popoverDidClose(_ notification: Notification)
```

#### Discussion

Invoked on the delegate when the [`didCloseNotification`](nspopover/didclosenotification.md) notification is sent.

This method will also be invoked on the delegate’s popover, if the method has been implemented.

## See Also

- [func popoverShouldClose(NSPopover) -> Bool](nspopoverdelegate/popovershouldclose(_:).md)
  Allows a delegate to override a close request.
- [func popoverWillShow(Notification)](nspopoverdelegate/popoverwillshow(_:).md)
  Invoked when the popover will show.
- [func popoverDidShow(Notification)](nspopoverdelegate/popoverdidshow(_:).md)
  Invoked when the popover has been shown.
- [func popoverWillClose(Notification)](nspopoverdelegate/popoverwillclose(_:).md)
  Invoked when the popover is about to close.
- [func popoverDidDetach(NSPopover)](nspopoverdelegate/popoverdiddetach(_:).md)
  Indicates that a popover has been released while it’s in an implicitly detached state.
- [func popoverShouldDetach(NSPopover) -> Bool](nspopoverdelegate/popovershoulddetach(_:).md)
  Returns a Boolean value that indicates whether a popover should detach from its positioning view and become a separate window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopoverdelegate/popoverdidclose(_:))*