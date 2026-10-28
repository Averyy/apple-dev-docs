# endSheet(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Ends a document modal session by specifying the sheet window.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`endSheet(_:)`](../nswindow/endsheet%28_%29-4dmmq.md) method of [`NSWindow`](../nswindow.md) instead.

## Declaration

```swift
func endSheet(_ sheet: NSWindow)
```

```objc
- (void) endSheet:(NSWindow *) sheet;
```

## Discussion

This method ends the modal session with the return code [`stop`](./modalresponse/stop.md).

## Parameters

- `sheet`: The sheet whose modal session you want to end.

## See Also

### Deprecated methods
- [func activate(ignoringOtherApps: Bool)](./activate%28ignoringotherapps%29.md)
  Makes the receiver the active app.
- [func endModalSession(NSApplication.ModalSession)](./endmodalsession%28_%29.md)
  Finishes a modal session.
- [func beginSheet(NSWindow, modalFor: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer!)](./beginsheet%28_,modalfor,modaldelegate,didend,contextinfo%29.md)
  Starts a document modal session.
- [func endSheet(NSWindow, returnCode: Int)](./endsheet%28_,returncode%29.md)
  Ends a document modal session by specifying the sheet window.
- [- beginModalSessionForWindow:relativeToWindow:](./beginmodalsessionforwindow_relativetowindow_.md)
- [- runModalForWindow:relativeToWindow:](./runmodalforwindow_relativetowindow_.md)
- [- application:printFiles:](./application_printfiles_.md)
  Use the delegate method [`application:printFiles:withSettings:showPrintPanels:`](../nsapplicationdelegate/application%28_,printfiles,withsettings,showprintpanels%29.md) instead.
- [- application:delegateHandlesKey:](../../ObjectiveC/nsobject-swift.class/application_delegatehandleskey_.md)
  Sent by Cocoa’s built-in scripting support during execution of `get` or `set` script commands to find out if the delegate can handle operations on the specified key-value key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/endsheet(_:))*