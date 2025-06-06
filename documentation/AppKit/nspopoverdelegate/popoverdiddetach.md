# popoverDidDetach(_:)

**Framework**: AppKit  
**Kind**: method

Indicates that a popover has been released while it’s in an implicitly detached state.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func popoverDidDetach(_ popover: NSPopover)
```

#### Discussion

This method is not called when the popover’s detached window is returned by [`detachableWindow(for:)`](nspopoverdelegate/detachablewindow(for:).md).

## Parameters

- `popover`: The popover that detached from its anchor view and is not closing.

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
- [func popoverShouldDetach(NSPopover) -> Bool](nspopoverdelegate/popovershoulddetach(_:).md)
  Returns a Boolean value that indicates whether a popover should detach from its positioning view and become a separate window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopoverdelegate/popoverdiddetach(_:))*