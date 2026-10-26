# INSearchForMessagesIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface that handles requests to search the current user’s messages.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
protocol INSearchForMessagesIntentHandling : NSObjectProtocol
```

```objc
@protocol INSearchForMessagesIntentHandling <NSObject>
```

## Mentions

- [Dispatching intents to handlers](../SiriKit/dispatching-intents-to-handlers.md)

#### Overview

Use the methods of the [`INSearchForMessagesIntentHandling`](./insearchformessagesintenthandling.md) protocol to resolve, confirm, and handle requests to search the current user’s messages. Adopt this protocol in an object of your Intents extension capable of searching your app’s messages.

Siri delivers an [`INSearchForMessagesIntent`](./insearchformessagesintent.md) object to your handler when the user asks to search their messages. The provided intent object contains the search parameters to use when matching messages. Use the methods of this protocol to resolve the search parameters, to perform the search, and to return the results.

## Topics

### Resolving the Intent Parameters
- [func resolveRecipients(for: INSearchForMessagesIntent, with: ([INPersonResolutionResult]) -> Void)](./insearchformessagesintenthandling/resolverecipients%28for,with%29.md)
  Resolves the user’s input when they search for messages sent to specific people.
- [func resolveSenders(for: INSearchForMessagesIntent, with: ([INPersonResolutionResult]) -> Void)](./insearchformessagesintenthandling/resolvesenders%28for,with%29.md)
  Resolves the user’s input when they search for messages sent by specific people.
- [func resolveAttributes(for: INSearchForMessagesIntent, with: (INMessageAttributeOptionsResolutionResult) -> Void)](./insearchformessagesintenthandling/resolveattributes%28for,with%29.md)
  Resolves the user’s input when they search for messages with specific attributes.
- [func resolveDateTimeRange(for: INSearchForMessagesIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./insearchformessagesintenthandling/resolvedatetimerange%28for,with%29.md)
  Resolves the user’s input when they search for messages sent in a specific time period.
- [func resolveSpeakableGroupNames(for: INSearchForMessagesIntent, with: ([INSpeakableStringResolutionResult]) -> Void)](./insearchformessagesintenthandling/resolvespeakablegroupnames%28for,with%29.md)
  Resolves the user’s input when they search for messages sent to a specific group of people.
- [func resolveGroupNames(for: INSearchForMessagesIntent, with: ([INStringResolutionResult]) -> Void)](./insearchformessagesintenthandling/resolvegroupnames%28for,with%29.md)
  Resolves the user’s input when they search for messages sent to a specific group of people.
### Confirming the Response
- [func confirm(intent: INSearchForMessagesIntent, completion: (INSearchForMessagesIntentResponse) -> Void)](./insearchformessagesintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can perform the search.
### Handling the Intent
- [func handle(intent: INSearchForMessagesIntent, completion: (INSearchForMessagesIntentResponse) -> Void)](./insearchformessagesintenthandling/handle%28intent,completion%29.md)
  Performs the search and returns the results.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INMessagesDomainHandling](./inmessagesdomainhandling.md)

## See Also

### Searching for Messages
- [class INSearchForMessagesIntent](./insearchformessagesintent.md)
  A request to list the messages that match the specified criteria.
- [class INSearchForMessagesIntentResponse](./insearchformessagesintentresponse.md)
  Your app’s response to a search for messages intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintenthandling)*