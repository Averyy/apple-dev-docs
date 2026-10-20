# endSheet(_:returnCode:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Ends a document modal session by specifying the sheet window.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`endSheet(_:returnCode:)`](../nswindow/endsheet%28_,returncode%29.md) method of [`NSWindow`](../nswindow.md) instead.

## Declaration

```swift
func endSheet(_ sheet: NSWindow, returnCode: Int)
```

```objc
- (void) endSheet:(NSWindow *) sheet returnCode:(NSInteger) returnCode;
```

## Parameters

- `sheet`: The sheet whose modal session you want to end.
- `returnCode`: The return code to send to the delegate. You can use one of the return codes defined in [`NSApplication.ModalResponse`](./modalresponse.md) or a custom value that you define.

## See Also

### Deprecated methods
- [func activate(ignoringOtherApps: Bool)](./activate%28ignoringotherapps%29.md)
  Makes the receiver the active app.
- [func endModalSession(NSApplication.ModalSession)](./endmodalsession%28_%29.md)
  Finishes a modal session.
- [func beginSheet(NSWindow, modalFor: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer!)](./beginsheet%28_,modalfor,modaldelegate,didend,contextinfo%29.md)
  Starts a document modal session.
- [func endSheet(NSWindow)](./endsheet%28_%29.md)
  Ends a document modal session by specifying the sheet window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/endsheet(_:returncode:))*