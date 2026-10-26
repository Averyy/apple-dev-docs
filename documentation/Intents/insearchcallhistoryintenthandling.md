# INSearchCallHistoryIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for searching the user’s call history.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
protocol INSearchCallHistoryIntentHandling : NSObjectProtocol
```

```objc
@protocol INSearchCallHistoryIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INSearchCallHistoryIntentHandling`](./insearchcallhistoryintenthandling.md) protocol to resolve, confirm, and handle requests to search for calls in the user’s call history. Adopt this protocol in an object of your Intents extension that’s capable of performing the search and finding any matching records. Siri doesn’t display the call information found during the search. After a successful search, Siri launches your app to display that information.

Siri delivers an [`INSearchCallHistoryIntent`](./insearchcallhistoryintent.md) object to your handler when the user asks to search their call history. The provided intent object contains the search parameters, such as any contacts involved in the call or the range of dates to search. Use the methods of this protocol to resolve the search parameters and to perform the search.

## Topics

### Resolving the Intent Parameters
- [func resolveCallTypes(for: INSearchCallHistoryIntent, with: (INCallRecordTypeOptionsResolutionResult) -> Void)](./insearchcallhistoryintenthandling/resolvecalltypes%28for,with%29.md)
  Resolves the search criteria for the call type.
- [func resolveCallType(for: INSearchCallHistoryIntent, with: (INCallRecordTypeResolutionResult) -> Void)](./insearchcallhistoryintenthandling/resolvecalltype%28for,with%29.md)
  Resolves the search criteria for the call type.
- [func resolveRecipient(for: INSearchCallHistoryIntent, with: (INPersonResolutionResult) -> Void)](./insearchcallhistoryintenthandling/resolverecipient%28for,with%29.md)
  Resolves the search criteria for the recipients.
- [func resolveDateCreated(for: INSearchCallHistoryIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./insearchcallhistoryintenthandling/resolvedatecreated%28for,with%29.md)
  Resolves the range of dates for the search.
- [func resolveUnseen(for: INSearchCallHistoryIntent, with: (INBooleanResolutionResult) -> Void)](./insearchcallhistoryintenthandling/resolveunseen%28for,with%29.md)
  Resolves whether you can search for calls that the user hasn’t yet seen.
### Confirming the Response
- [func confirm(intent: INSearchCallHistoryIntent, completion: (INSearchCallHistoryIntentResponse) -> Void)](./insearchcallhistoryintenthandling/confirm%28intent,completion%29.md)
  Confirms that you can perform the search.
### Handling the Intent
- [func handle(intent: INSearchCallHistoryIntent, completion: (INSearchCallHistoryIntentResponse) -> Void)](./insearchcallhistoryintenthandling/handle%28intent,completion%29.md)
  Handles searching the user’s call history.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INCallsDomainHandling](./incallsdomainhandling.md)

## See Also

### Call History Search
- [class INSearchCallHistoryIntent](./insearchcallhistoryintent.md)
  A request to list the calls matching the specified criteria.
- [class INSearchCallHistoryIntentResponse](./insearchcallhistoryintentresponse.md)
  Your app’s response to a search call history intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintenthandling)*