# popoverShouldDetach(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether a popover should detach from its positioning view and become a separate window.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func popoverShouldDetach(_ popover: NSPopover) -> Bool
```

```objc
- (BOOL) popoverShouldDetach:(NSPopover *) popover;
```

#### Discussion

If you don’t implement this method, it returns [`false`](../../Swift/false.md) by default. If you return [`true`](../../Swift/true.md) from this method, but you don’t implement [`detachableWindow(for:)`](./detachablewindow%28for%29.md) or you implement it to return `nil`, a detachable window is created with the popover’s [`contentViewController`](../nspopover/contentviewcontroller.md).

An automatically created window has the same appearance as the detached popover. For example, if the popover’s [`contentViewController`](../nspopover/contentviewcontroller.md) has a title, it will be bound to and displayed as the title of the detached window. When a popover is released in a detached state, it calls [`popoverDidDetach(_:)`](./popoverdiddetach%28_%29.md) on the delegate. When a detached popover is closed, calls to [`popoverShouldClose(_:)`](./popovershouldclose%28_%29.md), [`popoverWillClose(_:)`](./popoverwillclose%28_%29.md), and [`popoverDidClose(_:)`](./popoverdidclose%28_%29.md), in addition to the related notifications, specify the reason [`standard`](../nspopover/closereason/standard.md).

## Parameters

- `popover`: The popover that may be detached.

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
- [func popoverDidDetach(NSPopover)](./popoverdiddetach%28_%29.md)
  Indicates that a popover has been released while it’s in an implicitly detached state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopoverdelegate/popovershoulddetach(_:))*