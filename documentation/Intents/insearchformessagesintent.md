# INSearchForMessagesIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to list the messages that match the specified criteria.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INSearchForMessagesIntent
```

```objc
@interface INSearchForMessagesIntent : INIntent
```

## Mentions

- [Improving interactions between Siri and your messaging app](../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)

#### Overview

Siri creates [`INSearchForMessagesIntent`](./insearchformessagesintent.md) objects when the user asks to see sent or received messages. You must implement this intent to support the reading of messages by Siri. This intent object contains the values for you to match when searching the user’s messages. Users can search for messages involving a specific person, messages with specific sent or received dates, or messages containing specific terms. When performing the search, use only the provided parameters, and ignore any that have no values.

To handle this intent, the handler object in your Intents extension must adopt the [`INSearchForMessagesIntentHandling`](./insearchformessagesintenthandling.md) protocol. Your handler confirms the request and creates an [`INSearchForMessagesIntentResponse`](./insearchformessagesintentresponse.md) object with the results of the search. For successful searches, Siri offers the user a way to launch your app and see the results.

> ❗ **Important**:  To implement support for this intent fully, you must also implement support for the [`INSetMessageAttributeIntent`](./insetmessageattributeintent.md) class. After reading messages that your search returns, Siri marks them as read by modifying the attributes of the messages using that intent class. For more information about supporting the set message attribute intent, see [`INSetMessageAttributeIntent`](./insetmessageattributeintent.md).

To allow a user wearing AirPods to automatically hear messages, you must implement both [`INSearchForMessagesIntent`](./insearchformessagesintent.md) and [`INSendMessageIntent`](./insendmessageintent.md). Add [`announcement`](../UserNotifications/unauthorizationoptions/announcement.md) to the options when calling [`requestAuthorization(options:completionHandler:)`](../UserNotifications/unusernotificationcenter/requestauthorization%28options,completionhandler%29.md). Finally, add [`allowAnnouncement`](../UserNotifications/unnotificationcategoryoptions/allowannouncement.md) to the category option and [`INSearchForMessagesIntent`](./insearchformessagesintent.md) to the category intent identifier.

##### Additional Intent Attributes

Additional attributes of this intent object include the following:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents |
| Requires unlocked device | Yes, unless Show Previews is in an enabled state on the user’s device. |

Apps can optionally ask the user to unlock the device before handling this intent. To require unlocking of the device, include the name of this class in the `IntentsRestrictedWhileLocked` key of your Intents extension’s `Info.plist` file.

## Topics

### Creating the Intent Object
- [init(recipients: [INPerson]?, senders: [INPerson]?, searchTerms: [String]?, attributes: INMessageAttributeOptions, dateTime: INDateComponentsRange?, identifiers: [String]?, notificationIdentifiers: [String]?, speakableGroupNames: [INSpeakableString]?, conversationIdentifiers: [String]?)](./insearchformessagesintent/init%28recipients,senders,searchterms,attributes,datetime,identifiers,notificationidentifiers,speakablegroupnames,conversationidentifiers%29.md)
  Creates a search messages intent object with the specified search criteria.
### Getting the Senders and Recipients
- [var recipients: [INPerson]?](./insearchformessagesintent/recipients.md)
  The contacts who are the recipients of the messages.
- [var recipientsOperator: INConditionalOperator](./insearchformessagesintent/recipientsoperator.md)
  The operator that defines how to use the recipients in the search criteria.
- [var senders: [INPerson]?](./insearchformessagesintent/senders.md)
  The senders to include or exclude when you search for messages.
- [var sendersOperator: INConditionalOperator](./insearchformessagesintent/sendersoperator.md)
  The operator that defines how to use the senders in the search criteria.
- [var speakableGroupNames: [INSpeakableString]?](./insearchformessagesintent/speakablegroupnames.md)
  The names of any groups associated with the message.
- [var speakableGroupNamesOperator: INConditionalOperator](./insearchformessagesintent/speakablegroupnamesoperator.md)
  The operator that defines how to use the group names in the search criteria.
### Getting the Search Criteria
- [var searchTerms: [String]?](./insearchformessagesintent/searchterms.md)
  The terms to look for in the messages.
- [var searchTermsOperator: INConditionalOperator](./insearchformessagesintent/searchtermsoperator.md)
  The operator that defines how to use the set of terms in the search criteria.
- [var dateTimeRange: INDateComponentsRange?](./insearchformessagesintent/datetimerange.md)
  The range of dates in which to search for messages.
- [var attributes: INMessageAttributeOptions](./insearchformessagesintent/attributes.md)
  The attributes that must be present on a message to yield a match.
### Specifying Message Identifiers
- [var identifiers: [String]?](./insearchformessagesintent/identifiers.md)
  The message identifiers to locate in your search.
- [var identifiersOperator: INConditionalOperator](./insearchformessagesintent/identifiersoperator.md)
  The operator that defines how to use the identifiers in the search criteria.
- [var conversationIdentifiers: [String]?](./insearchformessagesintent/conversationidentifiers.md)
  The conversation identifiers to locate in your search.
- [var conversationIdentifiersOperator: INConditionalOperator](./insearchformessagesintent/conversationidentifiersoperator.md)
  The operator that defines how to use the conversation identifiers in the search criteria.
- [var notificationIdentifiers: [String]?](./insearchformessagesintent/notificationidentifiers.md)
  The notification identifiers to locate in your search.
- [var notificationIdentifiersOperator: INConditionalOperator](./insearchformessagesintent/notificationidentifiersoperator.md)
  The operator that defines how to use the notification identifiers in the search criteria.
### Deprecated Symbols
- [convenience init(recipients: [INPerson]?, senders: [INPerson]?, searchTerms: [String]?, attributes: INMessageAttributeOptions, dateTimeRange: INDateComponentsRange?, identifiers: [String]?, notificationIdentifiers: [String]?, speakableGroupNames: [INSpeakableString]?)](./insearchformessagesintent/init%28recipients,senders,searchterms,attributes,datetimerange,identifiers,notificationidentifiers,speakablegroupnames%29.md)
  Creates a *search messages* intent object with the specified search criteria.
- [convenience init(recipients: [INPerson]?, senders: [INPerson]?, searchTerms: [String]?, attributes: INMessageAttributeOptions, dateTimeRange: INDateComponentsRange?, identifiers: [String]?, notificationIdentifiers: [String]?, groupNames: [String]?)](./insearchformessagesintent/init%28recipients,senders,searchterms,attributes,datetimerange,identifiers,notificationidentifiers,groupnames%29.md)
  Creates a *search messages* intent object with the specified search criteria.
- [var groupNames: [String]?](./insearchformessagesintent/groupnames.md)
  The names of any groups associated with the message.
- [var groupNamesOperator: INConditionalOperator](./insearchformessagesintent/groupnamesoperator.md)
  The operator that defines how to use the group names in the search criteria.
### Initializers
- [convenience init(recipients: [INPerson]?, senders: [INPerson]?, searchTerms: [String]?, attributes: INMessageAttributeOptions, dateTime: INDateComponentsRange?, identifiers: [String]?, notificationIdentifiers: [String]?, groupNames: [String]?)](./insearchformessagesintent/init%28recipients,senders,searchterms,attributes,datetime,identifiers,notificationidentifiers,groupnames%29.md)
- [convenience init(recipients: [INPerson]?, senders: [INPerson]?, searchTerms: [String]?, attributes: INMessageAttributeOptions, dateTime: INDateComponentsRange?, identifiers: [String]?, notificationIdentifiers: [String]?, speakableGroupNames: [INSpeakableString]?)](./insearchformessagesintent/init%28recipients,senders,searchterms,attributes,datetime,identifiers,notificationidentifiers,speakablegroupnames%29.md)
- [init(recipients: [INPerson]?, senders: [INPerson]?, searchTerms: [String]?, attributes: INMessageAttributeOptions, dateTimeRange: INDateComponentsRange?, identifiers: [String]?, notificationIdentifiers: [String]?, speakableGroupNames: [INSpeakableString]?, conversationIdentifiers: [String]?)](./insearchformessagesintent/init%28recipients,senders,searchterms,attributes,datetimerange,identifiers,notificationidentifiers,speakablegroupnames,conversationidentifiers%29.md)
### Default Implementations
- [INSearchForMessagesIntent Implementations](./insearchformessagesintent/insearchformessagesintent-implementations.md)

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Searching for Messages
- [protocol INSearchForMessagesIntentHandling](./insearchformessagesintenthandling.md)
  An interface that handles requests to search the current user’s messages.
- [class INSearchForMessagesIntentResponse](./insearchformessagesintentresponse.md)
  Your app’s response to a search for messages intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent)*