# canSendAttachments()

**Framework**: Message UI  
**Kind**: method  
**Role**: Type Method

Indicates whether or not messages can include attachments.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func canSendAttachments() -> Bool
```

```objc
+ (BOOL) canSendAttachments;
```

## Return Value

[`true`](../../Swift/true.md) if the device can send attachments in MMS or iMessage messages, or [`false`](../../Swift/false.md) otherwise.

## See Also

### Determining if message composition is available
- [class func canSendText() -> Bool](./cansendtext%28%29.md)
  Returns a Boolean value that indicates whether the current device is capable of sending text messages.
- [class func canSendSubject() -> Bool](./cansendsubject%28%29.md)
  Indicates whether or not messages can include subject lines, according to the user’s configuration in Settings.
- [class func isSupportedAttachmentUTI(String) -> Bool](./issupportedattachmentuti%28_%29.md)
  Indicates whether or not the message can accept a file, with the specified UTI, as an attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/cansendattachments())*