# performClose(_:)

**Framework**: AppKit  
**Kind**: method

Attempts to close the popover.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@IBAction
@MainActor func performClose(_ sender: Any?)
```

#### Discussion

The popover will not be closed if it has a delegate and the delegate implements the returns [`popoverShouldClose(_:)`](nspopoverdelegate/popovershouldclose(_:).md) method returning [`false`](https://developer.apple.com/documentation/swift/false), or if a subclass of the NSPopover class implements `popoverShouldClose:` and returns [`false`](https://developer.apple.com/documentation/swift/false)).

The operation will fail if the popover is displaying a nested popover or if it has a child window. A window will attempt to close its popovers when it receives a [`performClose(_:)`](nswindow/performclose(_:).md) message.

The popover animates out when closed unless the [`animates`](nspopover/animates.md) property is set to [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `sender`: The sender of the action message.

## See Also

- [func close()](nspopover/close.md)
  Forces the popover to close without consulting its delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/performclose(_:))*