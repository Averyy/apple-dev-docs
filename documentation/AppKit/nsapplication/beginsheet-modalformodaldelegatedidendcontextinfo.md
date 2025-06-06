# beginSheet(_:modalFor:modalDelegate:didEnd:contextInfo:)

**Framework**: AppKit  
**Kind**: method

Starts a document modal session.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func beginSheet(_ sheet: NSWindow, modalFor docWindow: NSWindow, modalDelegate: Any?, didEnd didEndSelector: Selector?, contextInfo: UnsafeMutableRawPointer!)
```

#### Discussion

This method displays the sheet modally on the specified window and returns control to the caller. Most events targeted at `docWindow` are prohibited while the sheet is displayed but the app’s main run loop runs normally otherwise.

## Parameters

- `sheet`: The window object representing the sheet you want to display.
- `docWindow`: The window object to which you want to attach the sheet.
- `modalDelegate`: The delegate object that defines your   method. If  , the method in   is not called.
- `didEndSelector`: An optional method to call when the sheet’s modal session has ended. This method must be defined on the object in the   parameter and have the following signature:
- `contextInfo`: A pointer to the context info you want passed to the   method when the sheet’s modal session ends.

## See Also

- [func activate(ignoringOtherApps: Bool)](nsapplication/activate(ignoringotherapps:).md)
  Makes the receiver the active app.
- [func endModalSession(NSApplication.ModalSession)](nsapplication/endmodalsession(_:).md)
  Finishes a modal session.
- [func endSheet(NSWindow)](nsapplication/endsheet(_:).md)
  Ends a document modal session by specifying the sheet window.
- [func endSheet(NSWindow, returnCode: Int)](nsapplication/endsheet(_:returncode:).md)
  Ends a document modal session by specifying the sheet window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/beginsheet(_:modalfor:modaldelegate:didend:contextinfo:))*