# init(identifier:conversationIdentifier:content:dateSent:sender:recipients:groupName:serviceName:messageType:referencedMessage:reaction:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
convenience init(identifier: String, conversationIdentifier: String?, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?, groupName: INSpeakableString?, serviceName: String?, messageType: INMessageType, referencedMessage: INMessage?, reaction: INMessageReaction?)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier conversationIdentifier:(NSString *) conversationIdentifier content:(NSString *) content dateSent:(NSDate *) dateSent sender:(INPerson *) sender recipients:(NSArray<INPerson *> *) recipients groupName:(INSpeakableString *) groupName serviceName:(NSString *) serviceName messageType:(INMessageType) messageType referencedMessage:(INMessage *) referencedMessage reaction:(INMessageReaction *) reaction;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessage/init(identifier:conversationidentifier:content:datesent:sender:recipients:groupname:servicename:messagetype:referencedmessage:reaction:))*