# conversationIdentifier

**Framework**: CarPlay  
**Kind**: property

The conversation’s unique identifier.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var conversationIdentifier: String? { get set }
```

#### Discussion

Provide the value that your app uses to identify the conversation. Siri passes this value to your app when the user selects the list item so that you can take any necessary action, such as, updating your message store to mark the conversation as read.

CarPlay doesn’t display this value to the user.

## See Also

- [var phoneOrEmailAddress: String?](cpmessagelistitem/phoneoremailaddress.md)
  The contact’s phone number or email address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem/conversationidentifier)*