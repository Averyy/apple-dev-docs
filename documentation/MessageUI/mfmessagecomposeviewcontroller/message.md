# message

**Framework**: Message UI  
**Kind**: property

A message object from your iMessage app extension.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@NSCopying
@MainActor var message: MSMessage? { get set }
```

#### Discussion

If your app has an iMessage app extension, you can display your iMessage app within the message compose view, just as you would in the Messages app. To display your iMessage app, create and assign an [`MSMessage`](https://developer.apple.com/documentation/Messages/MSMessage) object to this property.

By default, this property is set to `nil`.

For more information on creating iMessage apps, see [`Messages`](https://developer.apple.com/documentation/Messages).

## See Also

- [var recipients: [String]?](mfmessagecomposeviewcontroller/recipients.md)
  An array of strings that contains the initial recipients of the message.
- [var subject: String?](mfmessagecomposeviewcontroller/subject.md)
  The initial subject of the message.
- [var body: String?](mfmessagecomposeviewcontroller/body.md)
  The initial content of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/message)*