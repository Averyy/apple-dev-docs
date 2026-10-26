# recipients

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The people who received the message.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var recipients: [INPerson]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<INPerson *> * recipients;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<INPerson *> * recipients;
```

## See Also

### Getting the Participants
- [var sender: INPerson?](./sender.md)
  The person who sent the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessage/recipients)*