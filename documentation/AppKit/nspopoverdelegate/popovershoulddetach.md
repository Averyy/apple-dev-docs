# popoverShouldDetach(_:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether a popover should detach from its positioning view and become a separate window.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func popoverShouldDetach(_ popover: NSPopover) -> Bool
```

#### Discussion

If you don’t implement this method, it returns [`false`](https://developer.apple.com/documentation/Swift/false) by default. If you return [`true`](https://developer.apple.com/documentation/Swift/true) from this method, but you don’t implement [`detachableWindow(for:)`](nspopoverdelegate/detachablewindow(for:).md) or you implement it to return `nil`, a detachable window is created with the popover’s [`contentViewController`](nspopover/contentviewcontroller.md).

An automatically created window has the same appearance as the detached popover. For example, if the popover’s [`contentViewController`](nspopover/contentviewcontroller.md) has a title, it will be bound to and displayed as the title of the detached window. When a popover is released in a detached state, it calls [`popoverDidDetach(_:)`](nspopoverdelegate/popoverdiddetach(_:).md) on the delegate. When a detached popover is closed, calls to [`popoverShouldClose(_:)`](nspopoverdelegate/popovershouldclose(_:).md), [`popoverWillClose(_:)`](nspopoverdelegate/popoverwillclose(_:).md), and [`popoverDidClose(_:)`](nspopoverdelegate/popoverdidclose(_:).md), in addition to the related notifications, specify the reason [`standard`](nspopover/closereason/standard.md).

## Parameters

- `popover`: The popover that may be detached.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopoverdelegate/popovershoulddetach(_:))*