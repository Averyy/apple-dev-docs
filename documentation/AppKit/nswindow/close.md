# close()

**Framework**: AppKit  
**Kind**: method

Removes the window from the screen.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func close()
```

#### Discussion

If the window is set to be released when closed, a `release` message is sent to the object after the current event is completed. For an `NSWindow` object, the default is to be released on closing, while for an [`NSPanel`](nspanel.md) object, the default is not to be released. You can use the [`isReleasedWhenClosed`](nswindow/isreleasedwhenclosed.md) property to change the default behavior.

A window doesn’t have to be visible to receive the close message. For example, when the application terminates, it sends the close message to all windows in its window list, even those that are not currently visible.

The close method posts a [`willCloseNotification`](nswindow/willclosenotification.md) notification to the default notification center.

The close method differs in two important ways from the [`performClose(_:)`](nswindow/performclose(_:).md) method:

- It does not attempt to send a [`windowShouldClose(_:)`](nswindowdelegate/windowshouldclose(_:).md) message to the window or its delegate.
- It does not simulate the user clicking the close button by momentarily highlighting the button.

Use [`performClose(_:)`](nswindow/performclose(_:).md) if you need these features.

## See Also

- [func orderOut(Any?)](nswindow/orderout(_:).md)
  Removes the window from the screen list, which hides the window.
- [func performClose(Any?)](nswindow/performclose(_:).md)
  Simulates the user clicking the close button by momentarily highlighting the button and then closing the window.
- [var isReleasedWhenClosed: Bool](nswindow/isreleasedwhenclosed.md)
  A Boolean value that indicates whether the window is released when it receives the `close` message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/close())*