# popoverShouldClose(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows a delegate to override a close request.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func popoverShouldClose(_ popover: NSPopover) -> Bool
```

```objc
- (BOOL) popoverShouldClose:(NSPopover *) popover;
```

## Return Value

[`true`](../../Swift/true.md) if the popover should close, [`false`](../../Swift/false.md) otherwise.

## Discussion

The popover invokes this method on its delegate whenever it is about to close. This gives the delegate a chance to override the close.

If there is no delegate or the delegate does not implement this method the default behavior is that the popover will close.

## Parameters

- `popover`: The popover.

## See Also

### Popover Visibility
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
- [func popoverShouldDetach(NSPopover) -> Bool](./popovershoulddetach%28_%29.md)
  Returns a Boolean value that indicates whether a popover should detach from its positioning view and become a separate window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopoverdelegate/popovershouldclose(_:))*