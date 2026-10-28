# groupNamesOperator

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The operator that defines how to use the group names in the search criteria.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: Use speakableGroupNamesOperator instead

## Declaration

```swift
var groupNamesOperator: INConditionalOperator { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INConditionalOperator groupNamesOperator;
```

*macOS*

```objc
@property (atomic, assign, readonly) INConditionalOperator groupNamesOperator;
```

## Discussion

This property indicates whether the message must contain all, some, or none of the groups listed in the [`groupNames`](./groupnames.md) property.

## See Also

### Deprecated Symbols
- [convenience init(recipients: [INPerson]?, senders: [INPerson]?, searchTerms: [String]?, attributes: INMessageAttributeOptions, dateTimeRange: INDateComponentsRange?, identifiers: [String]?, notificationIdentifiers: [String]?, speakableGroupNames: [INSpeakableString]?)](./init%28recipients,senders,searchterms,attributes,datetimerange,identifiers,notificationidentifiers,speakablegroupnames%29.md)
  Creates a *search messages* intent object with the specified search criteria.
- [convenience init(recipients: [INPerson]?, senders: [INPerson]?, searchTerms: [String]?, attributes: INMessageAttributeOptions, dateTimeRange: INDateComponentsRange?, identifiers: [String]?, notificationIdentifiers: [String]?, groupNames: [String]?)](./init%28recipients,senders,searchterms,attributes,datetimerange,identifiers,notificationidentifiers,groupnames%29.md)
  Creates a *search messages* intent object with the specified search criteria.
- [var groupNames: [String]?](./groupnames.md)
  The names of any groups associated with the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/groupnamesoperator)*