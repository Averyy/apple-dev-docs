# INSearchCallHistoryIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to list the calls matching the specified criteria.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INSearchCallHistoryIntent
```

```objc
@interface INSearchCallHistoryIntent : INIntent
```

## Overview

SiriKit creates [`INSearchCallHistoryIntent`](./insearchcallhistoryintent.md) objects when the user asks to see previous calls from their call history. This intent object contains the values for you to match when searching the user’s call history. Users can search for calls involving a specific person, calls that occurred on specific dates, or calls that are of a specific type such as missed calls. When performing the search, use only the parameters provided and ignore any that have no values.

To handle this intent, the handler object in your Intents extension must adopt the [`INSearchCallHistoryIntentHandling`](./insearchcallhistoryintenthandling.md) protocol. Your handler confirms the request and creates an [`INSearchCallHistoryIntentResponse`](./insearchcallhistoryintentresponse.md) object with the results of the search. For successful searches, Siri offers the user a way to launch your app and see the results.

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents |
| Always requires unlocked device | Yes |

## Topics

### Initializing the Intent Object
- [convenience init(dateCreated: INDateComponentsRange?, recipient: INPerson?, callCapabilities: INCallCapabilityOptions, callTypes: INCallRecordTypeOptions, unseen: Bool?)](./insearchcallhistoryintent/init%28datecreated,recipient,callcapabilities,calltypes,unseen%29.md)
  Creates a search call history intent object with the specified search criteria.
- [convenience init(callType: INCallRecordType, dateCreated: INDateComponentsRange?, recipient: INPerson?, callCapabilities: INCallCapabilityOptions)](./insearchcallhistoryintent/init%28calltype,datecreated,recipient,callcapabilities%29.md)
  Creates a search call history intent object with the specified search criteria.
- [- initWithDateCreated:recipient:callCapabilities:callTypes:unseen:](./insearchcallhistoryintent/initwithdatecreated_recipient_callcapabilities_calltypes_unseen_.md)
  Initializes the search call history intent object with the specified search criteria.
### Getting the Recipient
- [var recipient: INPerson?](./insearchcallhistoryintent/recipient.md)
  The person involved in the call.
### Getting the Call History Details
- [var dateCreated: INDateComponentsRange?](./insearchcallhistoryintent/datecreated.md)
  The range of dates associated with the call records.
- [var callTypes: INCallRecordTypeOptions](./insearchcallhistoryintent/calltypes.md)
  The types of calls to search.
- [var callType: INCallRecordType](./insearchcallhistoryintent/calltype.md)
  The call type.
- [var callCapabilities: INCallCapabilityOptions](./insearchcallhistoryintent/callcapabilities.md)
  The audio-video capabilities of the call.
- [var unseen: Bool?](./insearchcallhistoryintent/unseen-9ua7o.md)
  A Boolean value that indicates whether the user has seen the call yet.
- [unseen](./insearchcallhistoryintent/unseen-1mohp.md)
  A Boolean value that indicates whether the user has seen the call yet.
### Initializers
- [convenience init(call: INCallRecordType, dateCreated: INDateComponentsRange?, recipient: INPerson?, callCapabilities: INCallCapabilityOptions)](./insearchcallhistoryintent/init%28call,datecreated,recipient,callcapabilities%29.md)
### Default Implementations
- [INSearchCallHistoryIntent Implementations](./insearchcallhistoryintent/insearchcallhistoryintent-implementations.md)

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

### Call History Search
- [protocol INSearchCallHistoryIntentHandling](./insearchcallhistoryintenthandling.md)
  The handler interface for searching the user’s call history.
- [class INSearchCallHistoryIntentResponse](./insearchcallhistoryintentresponse.md)
  Your app’s response to a search call history intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintent)*