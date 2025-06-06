# endModalSession(_:)

**Framework**: AppKit  
**Kind**: method

Finishes a modal session.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func endModalSession(_ session: NSApplication.ModalSession)
```

## Parameters

- `session`: A modal session structure returned by a previous invocation of  .

## See Also

- [func beginModalSession(for: NSWindow) -> NSApplication.ModalSession](nsapplication/beginmodalsession(for:).md)
  Sets up a modal session with the given window and returns a pointer to the `NSModalSession` structure representing the session.
- [func runModalSession(NSApplication.ModalSession) -> NSApplication.ModalResponse](nsapplication/runmodalsession(_:).md)
  Runs a given modal session, as defined in a previous invocation of [`beginModalSession(for:)`](nsapplication/beginmodalsession(for:).md).
- [func activate(ignoringOtherApps: Bool)](nsapplication/activate(ignoringotherapps:).md)
  Makes the receiver the active app.
- [func beginSheet(NSWindow, modalFor: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer!)](nsapplication/beginsheet(_:modalfor:modaldelegate:didend:contextinfo:).md)
  Starts a document modal session.
- [func endSheet(NSWindow)](nsapplication/endsheet(_:).md)
  Ends a document modal session by specifying the sheet window.
- [func endSheet(NSWindow, returnCode: Int)](nsapplication/endsheet(_:returncode:).md)
  Ends a document modal session by specifying the sheet window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/endmodalsession(_:))*