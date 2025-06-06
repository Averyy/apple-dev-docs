# helpRequested(_:)

**Framework**: AppKit  
**Kind**: method

Displays context-sensitive help for the receiver if help has been registered.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func helpRequested(_ eventPtr: NSEvent)
```

#### Discussion

[`NSWindow`](nswindow.md) invokes this method automatically when the user clicks for help and help has been registered using [`setContextHelp(_:for:)`](nshelpmanager/setcontexthelp(_:for:).md). Otherwise, `NSWindow` passes the message to the next responder. Subclasses are not required to override this method.

> **Note**:  Current hardware does not invoke this method and application code should not call it directly. To provide context-sensitive help, use help tags (tooltips). For more information, see [`macOS Human Interface Guidelines - Help Tags (Tooltips)`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/macos/user-interaction/help/#help-tags).

 Current hardware does not invoke this method and application code should not call it directly. To provide context-sensitive help, use help tags (tooltips). For more information, see [`macOS Human Interface Guidelines - Help Tags (Tooltips)`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/macos/user-interaction/help/#help-tags).

## Parameters

- `eventPtr`: An object encapsulating information about the help-request event.

## See Also

- [func showContextHelp(Any?)](nsresponder/showcontexthelp(_:).md)
  Implemented by subclasses to invoke the help system, displaying information relevant to the receiver and its current state.
- [func cursorUpdate(with: NSEvent)](nsresponder/cursorupdate(with:).md)
  Informs the receiver that the mouse cursor has moved into a cursor rectangle.
- [func flagsChanged(with: NSEvent)](nsresponder/flagschanged(with:).md)
  Informs the receiver that the user has pressed or released a modifier key (Shift, Control, and so on).
- [func tabletPoint(with: NSEvent)](nsresponder/tabletpoint(with:).md)
  Informs the receiver that a tablet-point event has occurred.
- [func tabletProximity(with: NSEvent)](nsresponder/tabletproximity(with:).md)
  Informs the receiver that a tablet-proximity event has occurred.
- [func scrollWheel(with: NSEvent)](nsresponder/scrollwheel(with:).md)
  Informs the receiver that the mouse’s scroll wheel has moved.
- [func quickLook(with: NSEvent)](nsresponder/quicklook(with:).md)
  Performs a Quick Look on the content at the location specified by the supplied event.
- [func changeMode(with: NSEvent)](nsresponder/changemode(with:).md)
  Informs the responder that performed a double-tap on the side of an Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/helprequested(_:))*