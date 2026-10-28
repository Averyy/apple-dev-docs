# initWithDateCreated:recipient:callCapabilities:callTypes:unseen:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Initializes the search call history intent object with the specified search criteria.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```objc
- (instancetype) initWithDateCreated:(INDateComponentsRange *) dateCreated recipient:(INPerson *) recipient callCapabilities:(INCallCapabilityOptions) callCapabilities callTypes:(INCallRecordTypeOptions) callTypes unseen:(NSNumber *) unseen;
```

## Return Value

A new [`INSearchCallHistoryIntent`](../insearchcallhistoryintent.md) object.

## Discussion

Normally, you don’t create instances of this class yourself. Instead, Siri creates instances when the user asks to search their call history. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `dateCreated`: The dates associated with the call records. Use this parameter to specify the range of dates to search.
- `recipient`: The person who received the call. Match the information in this parameter against the user’s contacts.
- `callCapabilities`: The audio-video capabilities of the call. Use this parameter to specify whether you want to search audio-only calls, video calls, or both. You can combine the constants of the [`INCallCapabilityOptions`](../incallcapabilityoptions.md) type as needed.
- `callTypes`: The types of calls to search. Use this parameter to specify whether you want to search all calls or search only outgoing calls, missed calls, or received calls.
- `unseen`: A Boolean indicating whether the user has seen the call yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintent/initwithdatecreated:recipient:callcapabilities:calltypes:unseen:)*