# canSendAttachments()

**Framework**: Message UI  
**Kind**: method

Indicates whether or not messages can include attachments.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func canSendAttachments() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the device can send attachments in MMS or iMessage messages, or [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

## See Also

- [class func canSendText() -> Bool](mfmessagecomposeviewcontroller/cansendtext.md)
  Returns a Boolean value that indicates whether the current device is capable of sending text messages.
- [class func canSendSubject() -> Bool](mfmessagecomposeviewcontroller/cansendsubject.md)
  Indicates whether or not messages can include subject lines, according to the user’s configuration in Settings.
- [class func isSupportedAttachmentUTI(String) -> Bool](mfmessagecomposeviewcontroller/issupportedattachmentuti(_:).md)
  Indicates whether or not the message can accept a file, with the specified UTI, as an attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/cansendattachments())*