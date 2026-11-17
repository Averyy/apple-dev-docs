# conversationIdentifier

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The app-specific identifier for the message conversation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var conversationIdentifier: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * conversationIdentifier;
```

## Discussion

This property represents a unique string your app can use to identify the message conversation. CarPlay passes this string to your SiriKit intents during the message flows, but doesn’t use it otherwise. If you initialized the message list item with a contact, the value of this property is `nil`.

## See Also

### Getting the message context
- [var phoneOrEmailAddress: String?](./phoneoremailaddress.md)
  The phone or email address of the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem/conversationidentifier)*