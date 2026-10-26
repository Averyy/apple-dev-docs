# serviceName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name of the service that delivers the message.

**Availability**:
- iOS 13.2+
- iPadOS 13.2+
- Mac Catalyst 13.2+
- visionOS 1.0+
- watchOS 6.1+

## Declaration

```swift
var serviceName: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * serviceName;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * serviceName;
```

## See Also

### Getting the Supplementary Attributes
- [var dateSent: Date?](./datesent.md)
  The date and time the app sent the message to each recipient.
- [var groupName: INSpeakableString?](./groupname.md)
  The name of the grouped conversation.
- [var messageType: INMessageType](./messagetype.md)
  The type of content the message contains.
- [enum INMessageType](../inmessagetype.md)
  Constants that describe the kinds of content a message can contain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessage/servicename)*