# NSApplication.ModalResponse

**Framework**: AppKit  
**Kind**: struct

A set of button return values for modal dialogs.

**Availability**:
- macOS ?+

## Declaration

```swift
struct ModalResponse
```

#### Discussion

The response value that a button returns can depend on which method is used to present the dialog. See [`alertWithMessageText:defaultButton:alternateButton:otherButton:informativeTextWithFormat:`](nsalert/alertwithmessagetext:defaultbutton:alternatebutton:otherbutton:informativetextwithformat:.md), [`runModal()`](nsalert/runmodal().md), and [`addButton(withTitle:)`](nsalert/addbutton(withtitle:).md) for examples.

## Topics

### Responses
- [static let OK: NSApplication.ModalResponse](nsapplication/modalresponse/ok.md)
  The presentation or dismissal of the sheet has finished.
- [static let cancel: NSApplication.ModalResponse](nsapplication/modalresponse/cancel.md)
  The presentation or dismissal of the sheet has been canceled.
- [static let `continue`: NSApplication.ModalResponse](nsapplication/modalresponse/continue.md)
  Modal session is continuing (returned by [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md) only).
- [static let stop: NSApplication.ModalResponse](nsapplication/modalresponse/stop.md)
  Modal session was broken with [`stopModal()`](nsapplication/stopmodal().md).
- [static let abort: NSApplication.ModalResponse](nsapplication/modalresponse/abort.md)
  Modal session was broken with [`abortModal()`](nsapplication/abortmodal().md).
- [static let alertFirstButtonReturn: NSApplication.ModalResponse](nsapplication/modalresponse/alertfirstbuttonreturn.md)
  The user clicked the first (rightmost) button on the dialog or sheet.
- [static let alertSecondButtonReturn: NSApplication.ModalResponse](nsapplication/modalresponse/alertsecondbuttonreturn.md)
  The user clicked the second button from the right edge of the dialog or sheet.
- [static let alertThirdButtonReturn: NSApplication.ModalResponse](nsapplication/modalresponse/alertthirdbuttonreturn.md)
  The user clicked the third button from the right edge of the dialog or sheet.
### Deprecated Responses
- [var NSRunStoppedResponse: Int](nsrunstoppedresponse.md)
  Modal session was broken with [`stopModal()`](nsapplication/stopmodal().md).
- [var NSRunAbortedResponse: Int](nsrunabortedresponse.md)
  Modal session was broken with [`abortModal()`](nsapplication/abortmodal().md).
- [var NSRunContinuesResponse: Int](nsruncontinuesresponse.md)
  Modal session is continuing (returned by [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md) only).
### Initializers
- [init(Int)](nsapplication/modalresponse/init(_:).md)
- [init(rawValue: Int)](nsapplication/modalresponse/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSAlert.Style](nsalert/style.md)
  The set of alert styles to style alerts in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/modalresponse)*