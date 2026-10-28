# groupName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name of the group to receive the message.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: Use [`speakableGroupName`](./speakablegroupname.md) instead.

## Declaration

```swift
var groupName: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * groupName;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * groupName;
```

## Discussion

Use this property to identify the group that is the intended recipient of the message. Your app is responsible for managing groups and for using this parameter to identify the appropriate group.

## See Also

### Deprecated Symbols
- [convenience init(recipients: [INPerson]?, content: String?, speakableGroupName: INSpeakableString?, conversationIdentifier: String?, serviceName: String?, sender: INPerson?)](./init%28recipients,content,speakablegroupname,conversationidentifier,servicename,sender%29.md)
  Initializes a send message intent object with the specified content and recipients.
- [convenience init(recipients: [INPerson]?, content: String?, groupName: String?, serviceName: String?, sender: INPerson?)](./init%28recipients,content,groupname,servicename,sender%29.md)
  Initializes a send message intent object with the specified content and recipients.
- [convenience init(recipients: [INPerson]?, outgoingMessageType: INOutgoingMessageType, content: String?, speakableGroupName: INSpeakableString?, conversationIdentifier: String?, serviceName: String?, sender: INPerson?)](./init%28recipients,outgoingmessagetype,content,speakablegroupname,conversationidentifier,servicename,sender%29.md)
  Initializes a send message intent object with the specified content and recipients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintent/groupname)*