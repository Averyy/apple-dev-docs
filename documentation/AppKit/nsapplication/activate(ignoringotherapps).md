# activate(ignoringOtherApps:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Makes the receiver the active app.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

> **Deprecated**: Use NSApplication method [`activate()`](./activate%28%29.md) instead.

## Declaration

```swift
func activate(ignoringOtherApps ignoreOtherApps: Bool)
```

```objc
- (void) activateIgnoringOtherApps:(BOOL) ignoreOtherApps;
```

#### Discussion

The `flag` parameter is normally set to [`false`](../../Swift/false.md). When the Finder launches an app, using a value of [`false`](../../Swift/false.md) for `flag` allows the app to become active if the user waits for it to launch, but the app remains unobtrusive if the user activates another app. Regardless of the setting of `flag`, there may be a time lag before the app activates—you shouldn’t assume the app will be active immediately after sending this message.

You rarely need to invoke this method. Under most circumstances, AppKit takes care of proper activation. However, you might find this method useful if you implement your own methods for inter-app communication.

You don’t need to send this message to make one of the app’s `NSWindows` key. When you send a [`makeKey()`](../nswindow/makekey%28%29.md) message to an `NSWindow` object, you ensure that it’s the key window when the app is active.

## Parameters

- `ignoreOtherApps`: If [`false`](../../Swift/false.md), the app activates only if no other app is currently active. If [`true`](../../Swift/true.md), the app activates regardless.

## See Also

### Related Documentation
- [func deactivate()](./deactivate%28%29.md)
  Deactivates the receiver.
- [var isActive: Bool](./isactive.md)
  A Boolean value indicating whether this is the active app.
### Deprecated methods
- [func endModalSession(NSApplication.ModalSession)](./endmodalsession%28_%29.md)
  Finishes a modal session.
- [func beginSheet(NSWindow, modalFor: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer!)](./beginsheet%28_,modalfor,modaldelegate,didend,contextinfo%29.md)
  Starts a document modal session.
- [func endSheet(NSWindow)](./endsheet%28_%29.md)
  Ends a document modal session by specifying the sheet window.
- [func endSheet(NSWindow, returnCode: Int)](./endsheet%28_,returncode%29.md)
  Ends a document modal session by specifying the sheet window.
- [- beginModalSessionForWindow:relativeToWindow:](./beginmodalsessionforwindow_relativetowindow_.md)
- [- runModalForWindow:relativeToWindow:](./runmodalforwindow_relativetowindow_.md)
- [- application:printFiles:](./application_printfiles_.md)
  Use the delegate method [`application:printFiles:withSettings:showPrintPanels:`](../nsapplicationdelegate/application%28_,printfiles,withsettings,showprintpanels%29.md) instead.
- [- application:delegateHandlesKey:](../../ObjectiveC/nsobject-swift.class/application_delegatehandleskey_.md)
  Sent by Cocoa’s built-in scripting support during execution of `get` or `set` script commands to find out if the delegate can handle operations on the specified key-value key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/activate(ignoringotherapps:))*