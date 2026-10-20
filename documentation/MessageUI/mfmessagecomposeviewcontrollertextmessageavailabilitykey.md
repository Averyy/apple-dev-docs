# MFMessageComposeViewControllerTextMessageAvailabilityKey

**Framework**: Message UI  
**Kind**: var  
**Role**: Global Variable

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

```c
extern NSString * const MFMessageComposeViewControllerTextMessageAvailabilityKey;
```

#### Discussion

This value matches the result of the [`canSendText()`](./mfmessagecomposeviewcontroller/cansendtext%28%29.md) class method.The `userInfo` dictionary for the [`MFMessageComposeViewControllerTextMessageAvailabilityDidChangeNotification`](./mfmessagecomposeviewcontrollertextmessageavailabilitydidchangenotification.md) notification includes this key. The value of this key is an [`NSNumber`](../Foundation/nsnumber.md) object that contains a Boolean value. This value matches the result of the [`canSendText()`](./mfmessagecomposeviewcontroller/cansendtext%28%29.md) class method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontrollertextmessageavailabilitykey)*