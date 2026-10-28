# stop

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Modal session was broken with [`stopModal()`](../stopmodal%28%29.md).

**Availability**:
- macOS 10.9+

## Declaration

```swift
static var stop: NSApplication.ModalResponse { get }
```

```c
static const NSModalResponse NSModalResponseStop;
```

## Discussion

This constant is also used as the default response for sheet.

## See Also

### Responses
- [static var OK: NSApplication.ModalResponse](./ok.md)
  The presentation or dismissal of the sheet has finished.
- [static var cancel: NSApplication.ModalResponse](./cancel.md)
  The presentation or dismissal of the sheet has been canceled.
- [static var `continue`: NSApplication.ModalResponse](./continue.md)
  Modal session is continuing (returned by [`runModalSession(_:)`](../runmodalsession%28_%29.md) only).
- [static var abort: NSApplication.ModalResponse](./abort.md)
  Modal session was broken with [`abortModal()`](../abortmodal%28%29.md).
- [static var alertFirstButtonReturn: NSApplication.ModalResponse](./alertfirstbuttonreturn.md)
  The user clicked the first (rightmost) button on the dialog or sheet.
- [static var alertSecondButtonReturn: NSApplication.ModalResponse](./alertsecondbuttonreturn.md)
  The user clicked the second button from the right edge of the dialog or sheet.
- [static var alertThirdButtonReturn: NSApplication.ModalResponse](./alertthirdbuttonreturn.md)
  The user clicked the third button from the right edge of the dialog or sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/modalresponse/stop)*