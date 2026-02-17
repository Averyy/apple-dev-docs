# stop

**Framework**: AppKit  
**Kind**: property

Modal session was broken with [`stopModal()`](nsapplication/stopmodal().md).

**Availability**:
- macOS 10.9+

## Declaration

```swift
static var stop: NSApplication.ModalResponse { get }
```

#### Discussion

This constant is also used as the default response for sheet.

## See Also

- [static var OK: NSApplication.ModalResponse](nsapplication/modalresponse/ok.md)
  The presentation or dismissal of the sheet has finished.
- [static var cancel: NSApplication.ModalResponse](nsapplication/modalresponse/cancel.md)
  The presentation or dismissal of the sheet has been canceled.
- [static var `continue`: NSApplication.ModalResponse](nsapplication/modalresponse/continue.md)
  Modal session is continuing (returned by [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md) only).
- [static var abort: NSApplication.ModalResponse](nsapplication/modalresponse/abort.md)
  Modal session was broken with [`abortModal()`](nsapplication/abortmodal().md).
- [static var alertFirstButtonReturn: NSApplication.ModalResponse](nsapplication/modalresponse/alertfirstbuttonreturn.md)
  The user clicked the first (rightmost) button on the dialog or sheet.
- [static var alertSecondButtonReturn: NSApplication.ModalResponse](nsapplication/modalresponse/alertsecondbuttonreturn.md)
  The user clicked the second button from the right edge of the dialog or sheet.
- [static var alertThirdButtonReturn: NSApplication.ModalResponse](nsapplication/modalresponse/alertthirdbuttonreturn.md)
  The user clicked the third button from the right edge of the dialog or sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/modalresponse/stop)*