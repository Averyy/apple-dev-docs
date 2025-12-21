# MFMessageComposeViewControllerTextMessageAvailabilityDidChange

**Framework**: Foundation  
**Kind**: property

Posted when the current device’s ability to send text messages changes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
static let MFMessageComposeViewControllerTextMessageAvailabilityDidChange: NSNotification.Name
```

#### Discussion

The system posts this notification when the value [`canSendText()`](https://developer.apple.com/documentation/MessageUI/MFMessageComposeViewController/canSendText()) returns has changed.

Upon receiving this notification, query its `userInfo` dictionary with the [`MFMessageComposeViewControllerTextMessageAvailabilityKey`](https://developer.apple.com/documentation/MessageUI/MFMessageComposeViewControllerTextMessageAvailabilityKey) key. If the availability of text message sending has changed, your app should invalidate caches and update its user interface as appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/mfmessagecomposeviewcontrollertextmessageavailabilitydidchange)*