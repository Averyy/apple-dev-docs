# endModalSession(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Finishes a modal session.

**Availability**:
- macOS

## Declaration

```swift
func endModalSession(_ session: NSApplication.ModalSession)
```

```objc
- (void) endModalSession:(NSModalSession) session;
```

## Parameters

- `session`: A modal session structure returned by a previous invocation of [`beginModalSession(for:)`](./beginmodalsession%28for%29.md).

## See Also

### Related Documentation
- [func beginModalSession(for: NSWindow) -> NSApplication.ModalSession](./beginmodalsession%28for%29.md)
  Sets up a modal session with the given window and returns a pointer to the `NSModalSession` structure representing the session.
- [func runModalSession(NSApplication.ModalSession) -> NSApplication.ModalResponse](./runmodalsession%28_%29.md)
  Runs a given modal session, as defined in a previous invocation of [`beginModalSession(for:)`](./beginmodalsession%28for%29.md).
### Deprecated methods
- [func activate(ignoringOtherApps: Bool)](./activate%28ignoringotherapps%29.md)
  Makes the receiver the active app.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/endmodalsession(_:))*