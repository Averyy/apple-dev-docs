# init(recipients:senders:searchTerms:attributes:dateTimeRange:identifiers:notificationIdentifiers:groupNames:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a *search messages* intent object with the specified search criteria.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: Use the designated initializer instead

## Declaration

```swift
convenience init(recipients: [INPerson]?, senders: [INPerson]?, searchTerms: [String]?, attributes: INMessageAttributeOptions = [], dateTimeRange: INDateComponentsRange?, identifiers: [String]?, notificationIdentifiers: [String]?, groupNames: [String]?)
```

#### Discussion

Normally, you do not create instances of this class yourself. Instead, Siri creates instances when the user asks to search their messages. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths. Specify `nil` for any parameters that you do not want used during the search.

## Parameters

- `recipients`: The recipients of the messages. You can specify multiple people to search for messages received by multiple users.
- `senders`: The senders of the messages. You can specify multiple people to search for messages sent by multiple users.
- `searchTerms`: An array of terms to look for in the message contents. Each term constitutes a search string to be matched in the message contents.
- `attributes`: Additional message attributes to consider during the search. For a list of possible values, see [`INMessageAttributeOptions`](../inmessageattributeoptions.md).
- `dateTimeRange`: The dates associated with the messages. Use this parameter to specify the range of dates to search.
- `identifiers`: The identifier strings of the messages. Use this parameter when you want to specify messages based on their unique ID.
- `notificationIdentifiers`: An array of identifiers from [`UNNotification`](../../UserNotifications/unnotification.md) objects. Use this parameter to search the notifications associated with your app.
- `groupNames`: An array of strings representing any group addresses receiving the message.

## See Also

### Deprecated Symbols
- [convenience init(recipients: [INPerson]?, senders: [INPerson]?, searchTerms: [String]?, attributes: INMessageAttributeOptions, dateTimeRange: INDateComponentsRange?, identifiers: [String]?, notificationIdentifiers: [String]?, speakableGroupNames: [INSpeakableString]?)](./init%28recipients,senders,searchterms,attributes,datetimerange,identifiers,notificationidentifiers,speakablegroupnames%29.md)
  Creates a *search messages* intent object with the specified search criteria.
- [var groupNames: [String]?](./groupnames.md)
  The names of any groups associated with the message.
- [var groupNamesOperator: INConditionalOperator](./groupnamesoperator.md)
  The operator that defines how to use the group names in the search criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/init(recipients:senders:searchterms:attributes:datetimerange:identifiers:notificationidentifiers:groupnames:))*