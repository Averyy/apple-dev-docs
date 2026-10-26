# messageType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The type of content the message contains.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var messageType: INMessageType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INMessageType messageType;
```

*macOS*

```objc
@property (atomic, readonly) INMessageType messageType;
```

## See Also

### Getting the Supplementary Attributes
- [var dateSent: Date?](./datesent.md)
  The date and time the app sent the message to each recipient.
- [var groupName: INSpeakableString?](./groupname.md)
  The name of the grouped conversation.
- [enum INMessageType](../inmessagetype.md)
  Constants that describe the kinds of content a message can contain.
- [var serviceName: String?](./servicename.md)
  The name of the service that delivers the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessage/messagetype)*