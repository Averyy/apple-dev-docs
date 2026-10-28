# MFMessageComposeViewControllerTextMessageAvailabilityDidChangeNotification

**Framework**: Message UI  
**Kind**: var  
**Role**: Global Variable

Posted when the value returned by the [`canSendText()`](./mfmessagecomposeviewcontroller/cansendtext%28%29.md) class method has changed.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```c
extern NSString * const MFMessageComposeViewControllerTextMessageAvailabilityDidChangeNotification;
```

## Discussion

Upon receiving this notification, query its `userInfo` dictionary with the [`MFMessageComposeViewControllerTextMessageAvailabilityKey`](./mfmessagecomposeviewcontrollertextmessageavailabilitykey.md) key. If the availability of text message sending has changed, your app should invalidate caches and update its user interface as appropriate.

## See Also

### Handling notifications
- [let MFMessageComposeViewControllerTextMessageAvailabilityKey: String](./mfmessagecomposeviewcontrollertextmessageavailabilitykey.md)
  The value of this key is a number object that contains a Boolean value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontrollertextmessageavailabilitydidchangenotification)*