# NSApplication.ModalResponse

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

A set of button return values for modal dialogs.

**Availability**:
- macOS

## Declaration

```swift
struct ModalResponse
```

```c
typedef NSInteger NSModalResponse;
```

#### Discussion

The response value that a button returns can depend on which method is used to present the dialog. See [`alertWithMessageText:defaultButton:alternateButton:otherButton:informativeTextWithFormat:`](../nsalert/alertwithmessagetext_defaultbutton_alternatebutton_otherbutton_informativetextwithformat_.md), [`runModal()`](../nsalert/runmodal%28%29.md), and [`addButton(withTitle:)`](../nsalert/addbutton%28withtitle%29.md) for examples.

## Topics

### Responses
- [static var OK: NSApplication.ModalResponse](./modalresponse/ok.md)
  The presentation or dismissal of the sheet has finished.
- [static var cancel: NSApplication.ModalResponse](./modalresponse/cancel.md)
  The presentation or dismissal of the sheet has been canceled.
- [static var `continue`: NSApplication.ModalResponse](./modalresponse/continue.md)
  Modal session is continuing (returned by [`runModalSession(_:)`](./runmodalsession%28_%29.md) only).
- [static var stop: NSApplication.ModalResponse](./modalresponse/stop.md)
  Modal session was broken with [`stopModal()`](./stopmodal%28%29.md).
- [static var abort: NSApplication.ModalResponse](./modalresponse/abort.md)
  Modal session was broken with [`abortModal()`](./abortmodal%28%29.md).
- [static var alertFirstButtonReturn: NSApplication.ModalResponse](./modalresponse/alertfirstbuttonreturn.md)
  The user clicked the first (rightmost) button on the dialog or sheet.
- [static var alertSecondButtonReturn: NSApplication.ModalResponse](./modalresponse/alertsecondbuttonreturn.md)
  The user clicked the second button from the right edge of the dialog or sheet.
- [static var alertThirdButtonReturn: NSApplication.ModalResponse](./modalresponse/alertthirdbuttonreturn.md)
  The user clicked the third button from the right edge of the dialog or sheet.
### Initializers
- [init(Int)](./modalresponse/init%28_%29.md)
- [init(rawValue: Int)](./modalresponse/init%28rawvalue%29.md)
### Deprecated
- [var NSRunStoppedResponse: Int](../nsrunstoppedresponse.md)
  Modal session was broken with [`stopModal()`](./stopmodal%28%29.md).
- [var NSRunAbortedResponse: Int](../nsrunabortedresponse.md)
  Modal session was broken with [`abortModal()`](./abortmodal%28%29.md).
- [var NSRunContinuesResponse: Int](../nsruncontinuesresponse.md)
  Modal session is continuing (returned by [`runModalSession(_:)`](./runmodalsession%28_%29.md) only).

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing alert response buttons
- [var buttons: [NSButton]](../nsalert/buttons.md)
  The array of response buttons for the alert.
- [func addButton(withTitle: String) -> NSButton](../nsalert/addbutton%28withtitle%29.md)
  Adds a button with a given title to the alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/modalresponse)*