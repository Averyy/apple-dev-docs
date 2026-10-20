# close()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Forces the popover to close without consulting its delegate.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func close()
```

```objc
- (void) close;
```

#### Discussion

Any popovers nested within the popovers will also receive a [`close()`](./close%28%29.md) message. When a window is closed in response to the [`close()`](../nswindow/close%28%29.md) message being sent, all of its popovers are closed. The popover animates out when closed unless the [`animates`](./animates.md) property is set to [`false`](../../Swift/false.md).

## See Also

### Closing a Popover
- [func performClose(Any?)](./performclose%28_%29.md)
  Attempts to close the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/close())*