# canSendText()

**Framework**: Message UI  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the current device is capable of sending text messages.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func canSendText() -> Bool
```

```objc
+ (BOOL) canSendText;
```

## Return Value

[`true`](../../Swift/true.md) if the device can send text messages or [`false`](../../Swift/false.md) if it cannot.

## Discussion

Always call this method before attempting to present the message compose view controller. A device may be unable to send messages if it does not support messaging or if it is not currently configured to send messages. This method applies only to the ability to send text messages via iMessage, SMS, and MMS.

To be notified of changes in the availability of sending text messages, register as an observer of the [`MFMessageComposeViewControllerTextMessageAvailabilityDidChangeNotification`](../mfmessagecomposeviewcontrollertextmessageavailabilitydidchangenotification.md) notification.

## See Also

### Determining if message composition is available
- [class func canSendAttachments() -> Bool](./cansendattachments%28%29.md)
  Indicates whether or not messages can include attachments.
- [class func canSendSubject() -> Bool](./cansendsubject%28%29.md)
  Indicates whether or not messages can include subject lines, according to the user’s configuration in Settings.
- [class func isSupportedAttachmentUTI(String) -> Bool](./issupportedattachmentuti%28_%29.md)
  Indicates whether or not the message can accept a file, with the specified UTI, as an attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/cansendtext())*