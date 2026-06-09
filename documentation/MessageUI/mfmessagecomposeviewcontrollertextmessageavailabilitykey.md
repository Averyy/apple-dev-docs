# MFMessageComposeViewControllerTextMessageAvailabilityKey

**Framework**: Message UI  
**Kind**: var

The value of this key is a number object that contains a Boolean value.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
let MFMessageComposeViewControllerTextMessageAvailabilityKey: String
```

#### Discussion

This value matches the result of the [`canSendText()`](mfmessagecomposeviewcontroller/cansendtext().md) class method.The `userInfo` dictionary for the [`MFMessageComposeViewControllerTextMessageAvailabilityDidChangeNotification`](mfmessagecomposeviewcontrollertextmessageavailabilitydidchangenotification.md) notification includes this key. The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object that contains a Boolean value. This value matches the result of the [`canSendText()`](mfmessagecomposeviewcontroller/cansendtext().md) class method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontrollertextmessageavailabilitykey)*