# popoverDidDetach(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Indicates that a popover has been released while it’s in an implicitly detached state.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func popoverDidDetach(_ popover: NSPopover)
```

```objc
- (void) popoverDidDetach:(NSPopover *) popover;
```

#### Discussion

This method is not called when the popover’s detached window is returned by [`detachableWindow(for:)`](./detachablewindow%28for%29.md).

## Parameters

- `popover`: The popover that detached from its anchor view and is not closing.

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
- [func popoverDidClose(Notification)](./popoverdidclose%28_%29.md)
  Invoked when the popover did close.
- [func popoverShouldDetach(NSPopover) -> Bool](./popovershoulddetach%28_%29.md)
  Returns a Boolean value that indicates whether a popover should detach from its positioning view and become a separate window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopoverdelegate/popoverdiddetach(_:))*