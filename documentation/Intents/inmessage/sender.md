# sender

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The person who sent the message.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var sender: INPerson? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INPerson * sender;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INPerson * sender;
```

## See Also

### Getting the Participants
- [var recipients: [INPerson]?](./recipients.md)
  The people who received the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessage/sender)*