# dateSent

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The date and time the app sent the message to each recipient.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var dateSent: Date? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSDate * dateSent;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSDate * dateSent;
```

## See Also

### Getting the Supplementary Attributes
- [var groupName: INSpeakableString?](./groupname.md)
  The name of the grouped conversation.
- [var messageType: INMessageType](./messagetype.md)
  The type of content the message contains.
- [enum INMessageType](../inmessagetype.md)
  Constants that describe the kinds of content a message can contain.
- [var serviceName: String?](./servicename.md)
  The name of the service that delivers the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessage/datesent)*