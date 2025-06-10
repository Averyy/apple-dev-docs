# init(conversationIdentifier:unread:)

**Framework**: CarPlay  
**Kind**: init

Initialize a @c CPMessageGridItemConfiguration for use in a @c CPListTemplate.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
init(conversationIdentifier: String, unread: Bool)
```

## Parameters

- `conversationIdentifier`: A value meaningful to your app to identify this conversation.   This identifier is not directly displayed to the user; rather, when the user selects this grid item,   SiriKit will pass this identifier back to your app for your own use.
- `unread`: A Boolean value indicating whether the item shows an unread indicator. The default value of this property is @c NO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagegriditemconfiguration/init(conversationidentifier:unread:))*