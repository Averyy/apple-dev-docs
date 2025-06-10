# MFMessageComposeViewControllerTextMessageAvailabilityDidChange

**Framework**: Foundation  
**Kind**: property

Posted when the value returned by the [`canSendText()`](https://developer.apple.com/documentation/MessageUI/MFMessageComposeViewController/canSendText()) class method has changed.

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

Upon receiving this notification, query its `userInfo` dictionary with the [`MFMessageComposeViewControllerTextMessageAvailabilityKey`](https://developer.apple.com/documentation/MessageUI/MFMessageComposeViewControllerTextMessageAvailabilityKey) key. If the availability of text message sending has changed, your app should invalidate caches and update its user interface as appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/mfmessagecomposeviewcontrollertextmessageavailabilitydidchange)*