# init(recipients:senders:searchTerms:attributes:dateTime:identifiers:notificationIdentifiers:groupNames:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: Use the designated initializer instead

## Declaration

```swift
convenience init(recipients: [INPerson]?, senders: [INPerson]?, searchTerms: [String]?, attributes: INMessageAttributeOptions = [], dateTime dateTimeRange: INDateComponentsRange?, identifiers: [String]?, notificationIdentifiers: [String]?, groupNames: [String]?)
```

```objc
- (instancetype) initWithRecipients:(NSArray<INPerson *> *) recipients senders:(NSArray<INPerson *> *) senders searchTerms:(NSArray<NSString *> *) searchTerms attributes:(INMessageAttributeOptions) attributes dateTimeRange:(INDateComponentsRange *) dateTimeRange identifiers:(NSArray<NSString *> *) identifiers notificationIdentifiers:(NSArray<NSString *> *) notificationIdentifiers groupNames:(NSArray<NSString *> *) groupNames;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/init(recipients:senders:searchterms:attributes:datetime:identifiers:notificationidentifiers:groupnames:))*