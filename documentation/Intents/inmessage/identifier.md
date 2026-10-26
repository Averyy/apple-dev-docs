# identifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The message’s unique identifier.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var identifier: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * identifier;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * identifier;
```

## Mentions

- [Improving interactions between Siri and your messaging app](../../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)

## See Also

### Identifying the Message
- [var conversationIdentifier: String?](./conversationidentifier.md)
  The identifier of the conversation that contains this message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessage/identifier)*