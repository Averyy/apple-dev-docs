# init(callType:dateCreated:recipient:callCapabilities:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a search call history intent object with the specified search criteria.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
convenience init(callType: INCallRecordType, dateCreated: INDateComponentsRange?, recipient: INPerson?, callCapabilities: INCallCapabilityOptions = [])
```

#### Return Value

A new [`INSearchCallHistoryIntent`](../insearchcallhistoryintent.md) object.

#### Discussion

Normally, you don’t create instances of this class yourself. Instead, Siri creates instances when the user asks to search their call history. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `callType`: The type of call to search. Use this parameter to specify whether you want to search all calls or search only outgoing calls, missed calls, or received calls.
- `dateCreated`: The dates associated with the call records. Use this parameter to specify the range of dates to search.
- `recipient`: The person who received the call. Match the information in this parameter against the user’s contacts.
- `callCapabilities`: The audio-video capabilities of the call. Use this parameter to specify whether you want to search audio-only calls, video calls, or both. You can combine the constants of the [`INCallCapabilityOptions`](../incallcapabilityoptions.md) type as needed.

## See Also

### Initializing the Intent Object
- [convenience init(dateCreated: INDateComponentsRange?, recipient: INPerson?, callCapabilities: INCallCapabilityOptions, callTypes: INCallRecordTypeOptions, unseen: Bool?)](./init%28datecreated,recipient,callcapabilities,calltypes,unseen%29.md)
  Creates a search call history intent object with the specified search criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintent/init(calltype:datecreated:recipient:callcapabilities:))*