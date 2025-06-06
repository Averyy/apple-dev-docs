# NSPopoverDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of optional methods that a popover delegate can implement to provide additional or custom functionality.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSPopoverDelegate : NSObjectProtocol
```

#### Overview

See [`NSPopover`](nspopover.md) for more information on popovers in general.

## Topics

### Popover Window
- [func detachableWindow(for: NSPopover) -> NSWindow?](nspopoverdelegate/detachablewindow(for:).md)
  Detaches the popover creating a window containing the content.
### Popover Visibility
- [func popoverShouldClose(NSPopover) -> Bool](nspopoverdelegate/popovershouldclose(_:).md)
  Allows a delegate to override a close request.
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

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSPopover](nspopover.md)
  A means to display additional content related to existing content on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopoverdelegate)*