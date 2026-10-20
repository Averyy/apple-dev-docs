# canSendMail()

**Framework**: Message UI  
**Kind**: method  
**Role**: Type Method

Returns a Boolean that indicates whether the current device is able to send email.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func canSendMail() -> Bool
```

```objc
+ (BOOL) canSendMail;
```

#### Return Value

[`true`](../../Swift/true.md) if the device is configured for sending email or [`false`](../../Swift/false.md) if it is not.

#### Discussion

You should call this method before attempting to display the mail composition interface. If it returns [`false`](../../Swift/false.md), you must not display the mail composition interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/cansendmail())*