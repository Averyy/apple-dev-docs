# performClose(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Attempts to close the popover.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@IBAction
func performClose(_ sender: Any?)
```

```objc
- (void) performClose:(id) sender;
```

#### Discussion

The popover will not be closed if it has a delegate and the delegate implements the returns [`popoverShouldClose(_:)`](../nspopoverdelegate/popovershouldclose%28_%29.md) method returning [`false`](../../Swift/false.md), or if a subclass of the NSPopover class implements `popoverShouldClose:` and returns [`false`](../../Swift/false.md)).

The operation will fail if the popover is displaying a nested popover or if it has a child window. A window will attempt to close its popovers when it receives a [`performClose(_:)`](../nswindow/performclose%28_%29.md) message.

The popover animates out when closed unless the [`animates`](./animates.md) property is set to [`false`](../../Swift/false.md).

## Parameters

- `sender`: The sender of the action message.

## See Also

### Closing a Popover
- [func close()](./close%28%29.md)
  Forces the popover to close without consulting its delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/performclose(_:))*