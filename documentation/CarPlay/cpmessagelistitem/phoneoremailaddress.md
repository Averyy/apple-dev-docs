# phoneOrEmailAddress

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The phone or email address of the contact.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var phoneOrEmailAddress: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * phoneOrEmailAddress;
```

## Discussion

This property represents the primary way to communicate with the contact. CarPlay passes this string to your SiriKit intents during message flows, but doesn’t use it otherwise. If you initialized the message list item with a conversation identifier, the value of this property is `nil`.

## See Also

### Getting the message context
- [var conversationIdentifier: String?](./conversationidentifier.md)
  The app-specific identifier for the message conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem/phoneoremailaddress)*