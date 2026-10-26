# init(recipients:senders:searchTerms:attributes:dateTime:identifiers:notificationIdentifiers:speakableGroupNames:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 11.0+ - Deprecated in 12.0
- iPadOS 11.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 5.0

> **Deprecated**: Use the designated initializer instead

## Declaration

```swift
convenience init(recipients: [INPerson]?, senders: [INPerson]?, searchTerms: [String]?, attributes: INMessageAttributeOptions = [], dateTime dateTimeRange: INDateComponentsRange?, identifiers: [String]?, notificationIdentifiers: [String]?, speakableGroupNames: [INSpeakableString]?)
```

```objc
- (instancetype) initWithRecipients:(NSArray<INPerson *> *) recipients senders:(NSArray<INPerson *> *) senders searchTerms:(NSArray<NSString *> *) searchTerms attributes:(INMessageAttributeOptions) attributes dateTimeRange:(INDateComponentsRange *) dateTimeRange identifiers:(NSArray<NSString *> *) identifiers notificationIdentifiers:(NSArray<NSString *> *) notificationIdentifiers speakableGroupNames:(NSArray<INSpeakableString *> *) speakableGroupNames;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/init(recipients:senders:searchterms:attributes:datetime:identifiers:notificationidentifiers:speakablegroupnames:))*