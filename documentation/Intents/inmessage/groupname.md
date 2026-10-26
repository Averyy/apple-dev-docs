# groupName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name of the grouped conversation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
@NSCopying
var groupName: INSpeakableString? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INSpeakableString * groupName;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INSpeakableString * groupName;
```

## See Also

### Getting the Supplementary Attributes
- [var dateSent: Date?](./datesent.md)
  The date and time the app sent the message to each recipient.
- [var messageType: INMessageType](./messagetype.md)
  The type of content the message contains.
- [enum INMessageType](../inmessagetype.md)
  Constants that describe the kinds of content a message can contain.
- [var serviceName: String?](./servicename.md)
  The name of the service that delivers the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessage/groupname)*