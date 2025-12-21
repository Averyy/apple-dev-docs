# activate(ignoringOtherApps:)

**Framework**: AppKit  
**Kind**: method

Makes the receiver the active app.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func activate(ignoringOtherApps ignoreOtherApps: Bool)
```

#### Discussion

The `flag` parameter is normally set to [`false`](https://developer.apple.com/documentation/Swift/false). When the Finder launches an app, using a value of [`false`](https://developer.apple.com/documentation/Swift/false) for `flag` allows the app to become active if the user waits for it to launch, but the app remains unobtrusive if the user activates another app. Regardless of the setting of `flag`, there may be a time lag before the app activates—you shouldn’t assume the app will be active immediately after sending this message.

You rarely need to invoke this method. Under most circumstances, AppKit takes care of proper activation. However, you might find this method useful if you implement your own methods for inter-app communication.

You don’t need to send this message to make one of the app’s `NSWindows` key. When you send a [`makeKey()`](nswindow/makekey().md) message to an `NSWindow` object, you ensure that it’s the key window when the app is active.

## Parameters

- `ignoreOtherApps`: If  , the app activates only if no other app is currently active. If  , the app activates regardless.

## See Also

- [func deactivate()](nsapplication/deactivate.md)
  Deactivates the receiver.
- [var isActive: Bool](nsapplication/isactive.md)
  A Boolean value indicating whether this is the active app.
- [func endModalSession(NSApplication.ModalSession)](nsapplication/endmodalsession(_:).md)
  Finishes a modal session.
- [func beginSheet(NSWindow, modalFor: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer!)](nsapplication/beginsheet(_:modalfor:modaldelegate:didend:contextinfo:).md)
  Starts a document modal session.
- [func endSheet(NSWindow)](nsapplication/endsheet(_:).md)
  Ends a document modal session by specifying the sheet window.
- [func endSheet(NSWindow, returnCode: Int)](nsapplication/endsheet(_:returncode:).md)
  Ends a document modal session by specifying the sheet window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/activate(ignoringotherapps:))*