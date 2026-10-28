# groupNames

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The names of any groups associated with the message.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: Use speakableGroupNames instead

## Declaration

```swift
var groupNames: [String]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSString *> * groupNames;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<NSString *> * groupNames;
```

## Discussion

When this property contains one or more [`NSString`](../../Foundation/nsstring.md) objects, your search should return only messages that sent to the specified groups. Use the operator in the [`groupNamesOperator`](./groupnamesoperator.md) property to determine whether to search for messages containing all, some, or none of the specified groups.

## See Also

### Deprecated Symbols
- [convenience init(recipients: [INPerson]?, senders: [INPerson]?, searchTerms: [String]?, attributes: INMessageAttributeOptions, dateTimeRange: INDateComponentsRange?, identifiers: [String]?, notificationIdentifiers: [String]?, speakableGroupNames: [INSpeakableString]?)](./init%28recipients,senders,searchterms,attributes,datetimerange,identifiers,notificationidentifiers,speakablegroupnames%29.md)
  Creates a *search messages* intent object with the specified search criteria.
- [convenience init(recipients: [INPerson]?, senders: [INPerson]?, searchTerms: [String]?, attributes: INMessageAttributeOptions, dateTimeRange: INDateComponentsRange?, identifiers: [String]?, notificationIdentifiers: [String]?, groupNames: [String]?)](./init%28recipients,senders,searchterms,attributes,datetimerange,identifiers,notificationidentifiers,groupnames%29.md)
  Creates a *search messages* intent object with the specified search criteria.
- [var groupNamesOperator: INConditionalOperator](./groupnamesoperator.md)
  The operator that defines how to use the group names in the search criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/groupnames)*