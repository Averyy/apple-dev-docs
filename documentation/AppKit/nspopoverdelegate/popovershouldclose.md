# popoverShouldClose(_:)

**Framework**: AppKit  
**Kind**: method

Allows a delegate to override a close request.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func popoverShouldClose(_ popover: NSPopover) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the popover should close, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

The popover invokes this method on its delegate whenever it is about to close. This gives the delegate a chance to override the close.

If there is no delegate or the delegate does not implement this method the default behavior is that the popover will close.

## Parameters

- `popover`: The popover.

## See Also

- [func popoverWillShow(Notification)](nspopoverdelegate/popoverwillshow(_:).md)
  Invoked when the popover will show.
- [func popoverDidShow(Notification)](nspopoverdelegate/popoverdidshow(_:).md)
  Invoked when the popover has been shown.
- [func popoverWillClose(Notification)](nspopoverdelegate/popoverwillclose(_:).md)
  Invoked when the popover is about to close.
- [func popoverDidClose(Notification)](nspopoverdelegate/popoverdidclose(_:).md)
  Invoked when the popover did close.
- [func popoverDidDetach(NSPopover)](nspopoverdelegate/popoverdiddetach(_:).md)
  Indicates that a popover has been released while it’s in an implicitly detached state.
- [func popoverShouldDetach(NSPopover) -> Bool](nspopoverdelegate/popovershoulddetach(_:).md)
  Returns a Boolean value that indicates whether a popover should detach from its positioning view and become a separate window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopoverdelegate/popovershouldclose(_:))*