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

This value matches the result of the [`canSendText()`](mfmessagecomposeviewcontroller/cansendtext().md) class method.The `userInfo` dictionary for the [`MFMessageComposeViewControllerTextMessageAvailabilityDidChange`](https://developer.apple.com/documentation/foundation/nsnotification/name/1614064-mfmessagecomposeviewcontrollerte) notification includes this key. The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object that contains a Boolean value. This value matches the result of the [`canSendText()`](mfmessagecomposeviewcontroller/cansendtext().md) class method.

## See Also

- [static let MFMessageComposeViewControllerTextMessageAvailabilityDidChange: NSNotification.Name](../foundation/nsnotification/name/1614064-mfmessagecomposeviewcontrollerte.md)
  Posted when the value returned by the  class method has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontrollertextmessageavailabilitykey)*