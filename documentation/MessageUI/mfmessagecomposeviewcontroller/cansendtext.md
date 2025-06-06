# canSendText()

**Framework**: Message UI  
**Kind**: method

Returns a Boolean value that indicates whether the current device is capable of sending text messages.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func canSendText() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the device can send text messages or [`false`](https://developer.apple.com/documentation/swift/false) if it cannot.

#### Discussion

Always call this method before attempting to present the message compose view controller. A device may be unable to send messages if it does not support messaging or if it is not currently configured to send messages. This method applies only to the ability to send text messages via iMessage, SMS, and MMS.

To be notified of changes in the availability of sending text messages, register as an observer of the [`MFMessageComposeViewControllerTextMessageAvailabilityDidChange`](https://developer.apple.com/documentation/foundation/nsnotification/name/1614064-mfmessagecomposeviewcontrollerte) notification.

## See Also

- [class func canSendAttachments() -> Bool](mfmessagecomposeviewcontroller/cansendattachments.md)
  Indicates whether or not messages can include attachments.
- [class func canSendSubject() -> Bool](mfmessagecomposeviewcontroller/cansendsubject.md)
  Indicates whether or not messages can include subject lines, according to the user’s configuration in Settings.
- [class func isSupportedAttachmentUTI(String) -> Bool](mfmessagecomposeviewcontroller/issupportedattachmentuti(_:).md)
  Indicates whether or not the message can accept a file, with the specified UTI, as an attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/cansendtext())*