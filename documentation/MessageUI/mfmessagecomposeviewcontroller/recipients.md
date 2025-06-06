# recipients

**Framework**: Message UI  
**Kind**: property

An array of strings that contains the initial recipients of the message.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var recipients: [String]? { get set }
```

#### Discussion

If you want to provide an initial array of one or more recipients for a message, do so before you display it. After the message is displayed you cannot change the value of this property.

Each string in the array should contain the phone number of the intended recipient.

## See Also

- [var subject: String?](mfmessagecomposeviewcontroller/subject.md)
  The initial subject of the message.
- [var body: String?](mfmessagecomposeviewcontroller/body.md)
  The initial content of the message.
- [var message: MSMessage?](mfmessagecomposeviewcontroller/message.md)
  A message object from your iMessage app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/recipients)*