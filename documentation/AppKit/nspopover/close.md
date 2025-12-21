# close()

**Framework**: AppKit  
**Kind**: method

Forces the popover to close without consulting its delegate.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func close()
```

#### Discussion

Any popovers nested within the popovers will also receive a [`close()`](nspopover/close().md) message. When a window is closed in response to the [`close()`](nswindow/close().md) message being sent, all of its popovers are closed. The popover animates out when closed unless the [`animates`](nspopover/animates.md) property is set to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func performClose(Any?)](nspopover/performclose(_:).md)
  Attempts to close the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/close())*