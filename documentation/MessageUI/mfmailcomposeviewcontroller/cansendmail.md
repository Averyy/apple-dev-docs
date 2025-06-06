# canSendMail()

**Framework**: Message UI  
**Kind**: method

Returns a Boolean that indicates whether the current device is able to send email.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func canSendMail() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the device is configured for sending email or [`false`](https://developer.apple.com/documentation/swift/false) if it is not.

#### Discussion

You should call this method before attempting to display the mail composition interface. If it returns [`false`](https://developer.apple.com/documentation/swift/false), you must not display the mail composition interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/cansendmail())*