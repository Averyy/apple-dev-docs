# OK

**Framework**: AppKit  
**Kind**: property

The presentation or dismissal of the sheet has finished.

**Availability**:
- macOS ?+

## Declaration

```swift
static var OK: NSApplication.ModalResponse { get }
```

## See Also

- [static var cancel: NSApplication.ModalResponse](nsapplication/modalresponse/cancel.md)
  The presentation or dismissal of the sheet has been canceled.
- [static var `continue`: NSApplication.ModalResponse](nsapplication/modalresponse/continue.md)
  Modal session is continuing (returned by [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md) only).
- [static var stop: NSApplication.ModalResponse](nsapplication/modalresponse/stop.md)
  Modal session was broken with [`stopModal()`](nsapplication/stopmodal().md).
- [static var abort: NSApplication.ModalResponse](nsapplication/modalresponse/abort.md)
  Modal session was broken with [`abortModal()`](nsapplication/abortmodal().md).
- [static var alertFirstButtonReturn: NSApplication.ModalResponse](nsapplication/modalresponse/alertfirstbuttonreturn.md)
  The user clicked the first (rightmost) button on the dialog or sheet.
- [static var alertSecondButtonReturn: NSApplication.ModalResponse](nsapplication/modalresponse/alertsecondbuttonreturn.md)
  The user clicked the second button from the right edge of the dialog or sheet.
- [static var alertThirdButtonReturn: NSApplication.ModalResponse](nsapplication/modalresponse/alertthirdbuttonreturn.md)
  The user clicked the third button from the right edge of the dialog or sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/modalresponse/ok)*