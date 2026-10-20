# MFMessageComposeViewControllerTextMessageAvailabilityDidChange

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

The system posts this notification when the value [`canSendText()`](../../../MessageUI/mfmessagecomposeviewcontroller/cansendtext%28%29.md) returns has changed.

Upon receiving this notification, query its `userInfo` dictionary with the [`MFMessageComposeViewControllerTextMessageAvailabilityKey`](../../../MessageUI/mfmessagecomposeviewcontrollertextmessageavailabilitykey.md) key. If the availability of text message sending has changed, your app should invalidate caches and update its user interface as appropriate.

## See Also

### MessageUI
- [static let MFMessageComposeViewControllerTextMessageAvailabilityDidChange: NSNotification.Name](./mfmessagecomposeviewcontrollertextmessageavailabilitydidchange.md)
  Posted when the current device’s ability to send text messages changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/mfmessagecomposeviewcontrollertextmessageavailabilitydidchange)*