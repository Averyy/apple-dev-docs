# conversationIdentifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The identifier of the conversation that contains this message.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var conversationIdentifier: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * conversationIdentifier;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * conversationIdentifier;
```

## See Also

### Identifying the Message
- [var identifier: String](./identifier.md)
  The message’s unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessage/conversationidentifier)*