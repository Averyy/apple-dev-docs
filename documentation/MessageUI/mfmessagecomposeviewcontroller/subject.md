# subject

**Framework**: Message UI  
**Kind**: property

The initial subject of the message.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var subject: String? { get set }
```

#### Discussion

If you want to provide an initial subject for a message, do so before you display it. After the message is displayed you cannot change the value of this property.

## See Also

- [var recipients: [String]?](mfmessagecomposeviewcontroller/recipients.md)
  An array of strings that contains the initial recipients of the message.
- [var body: String?](mfmessagecomposeviewcontroller/body.md)
  The initial content of the message.
- [var message: MSMessage?](mfmessagecomposeviewcontroller/message.md)
  A message object from your iMessage app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/subject)*