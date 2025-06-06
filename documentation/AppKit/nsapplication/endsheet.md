# endSheet(_:)

**Framework**: AppKit  
**Kind**: method

Ends a document modal session by specifying the sheet window.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func endSheet(_ sheet: NSWindow)
```

#### Discussion

This method ends the modal session with the return code [`stop`](nsapplication/modalresponse/stop.md).

## Parameters

- `sheet`: The sheet whose modal session you want to end.

## See Also

- [func activate(ignoringOtherApps: Bool)](nsapplication/activate(ignoringotherapps:).md)
  Makes the receiver the active app.
- [func endModalSession(NSApplication.ModalSession)](nsapplication/endmodalsession(_:).md)
  Finishes a modal session.
- [func beginSheet(NSWindow, modalFor: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer!)](nsapplication/beginsheet(_:modalfor:modaldelegate:didend:contextinfo:).md)
  Starts a document modal session.
- [func endSheet(NSWindow, returnCode: Int)](nsapplication/endsheet(_:returncode:).md)
  Ends a document modal session by specifying the sheet window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/endsheet(_:))*