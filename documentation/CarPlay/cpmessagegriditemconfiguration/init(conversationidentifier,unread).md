# init(conversationIdentifier:unread:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates the configuration object with a conversation identifier and Boolean value.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
init(conversationIdentifier: String, unread: Bool)
```

```objc
- (instancetype) initWithConversationIdentifier:(NSString *) conversationIdentifier unread:(BOOL) unread;
```

## Return Value

An initialized configuration object.

## Parameters

- `conversationIdentifier`: A string you use to uniquely identify the conversation in your app. Choose a value that is unique for the conversation. For example, if you assign a [`UUID`](../../Foundation/uuid.md) type to each conversation, specify that value as a string.
- `unread`: A Boolean value to set the conversation status to unread. Specify `true` if the conversation contains unread messages, or `false` if it doesn’t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagegriditemconfiguration/init(conversationidentifier:unread:))*