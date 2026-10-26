# INSearchForNotebookItemsIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for searching for notes, tasks, and reminders.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
protocol INSearchForNotebookItemsIntentHandling : NSObjectProtocol
```

```objc
@protocol INSearchForNotebookItemsIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INSearchForNotebookItemsIntentHandling`](./insearchfornotebookitemsintenthandling.md) protocol to resolve, confirm, and handle requests to search for notes, tasks, and reminders in your app’s content. Adopt this protocol in an object of your Intents extension that’s capable of performing the search and returning the search results to SiriKit.

Siri delivers an [`INSearchForNotebookItemsIntent`](./insearchfornotebookitemsintent.md) object to your handler when the user asks to search for items in your app. The provided intent object contains the search parameters provided by the user. Use the methods of this protocol to resolve the parameters and return the search results.

## Topics

### Resolving the Intent Parameters
- [func resolveItemType(for: INSearchForNotebookItemsIntent, with: (INNotebookItemTypeResolutionResult) -> Void)](./insearchfornotebookitemsintenthandling/resolveitemtype%28for,with%29.md)
  Resolves the type of items to search.
- [func resolveTitle(for: INSearchForNotebookItemsIntent, with: (INSpeakableStringResolutionResult) -> Void)](./insearchfornotebookitemsintenthandling/resolvetitle%28for,with%29.md)
  Resolves the string to use when searching the title of notes, tasks, or reminders.
- [func resolveContent(for: INSearchForNotebookItemsIntent, with: (INStringResolutionResult) -> Void)](./insearchfornotebookitemsintenthandling/resolvecontent%28for,with%29.md)
  Resolves the string to use when searching the content of notes.
- [func resolveStatus(for: INSearchForNotebookItemsIntent, with: (INTaskStatusResolutionResult) -> Void)](./insearchfornotebookitemsintenthandling/resolvestatus%28for,with%29.md)
  Resolves the status value to use during the search.
- [func resolveDateSearchType(for: INSearchForNotebookItemsIntent, with: (INDateSearchTypeResolutionResult) -> Void)](./insearchfornotebookitemsintenthandling/resolvedatesearchtype%28for,with%29.md)
  Resolves how to use a date value during the search.
- [func resolveDateTime(for: INSearchForNotebookItemsIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./insearchfornotebookitemsintenthandling/resolvedatetime%28for,with%29.md)
  Resolves the date to use during a date-based search.
- [func resolveLocation(for: INSearchForNotebookItemsIntent, with: (INPlacemarkResolutionResult) -> Void)](./insearchfornotebookitemsintenthandling/resolvelocation%28for,with%29.md)
  Resolves how to use a location value during the search.
- [func resolveLocationSearchType(for: INSearchForNotebookItemsIntent, with: (INLocationSearchTypeResolutionResult) -> Void)](./insearchfornotebookitemsintenthandling/resolvelocationsearchtype%28for,with%29.md)
  Resolves the location to use during a location-based search.
- [func resolveTaskPriority(for: INSearchForNotebookItemsIntent, with: (INTaskPriorityResolutionResult) -> Void)](./insearchfornotebookitemsintenthandling/resolvetaskpriority%28for,with%29.md)
  Resolves the priority to use during a priority-based search.
- [func resolveTemporalEventTriggerTypes(for: INSearchForNotebookItemsIntent, with: (INTemporalEventTriggerTypeOptionsResolutionResult) -> Void)](./insearchfornotebookitemsintenthandling/resolvetemporaleventtriggertypes%28for,with%29.md)
  Resolves the trigger type to use during a temporal-based search.
### Confirming the Response
- [func confirm(intent: INSearchForNotebookItemsIntent, completion: (INSearchForNotebookItemsIntentResponse) -> Void)](./insearchfornotebookitemsintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can perform the search.
### Handling the Intent
- [func handle(intent: INSearchForNotebookItemsIntent, completion: (INSearchForNotebookItemsIntentResponse) -> Void)](./insearchfornotebookitemsintenthandling/handle%28intent,completion%29.md)
  Performs the search and deliver the results to SiriKit.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INNotebookDomainHandling](./innotebookdomainhandling.md)

## See Also

### Notebook Search
- [class INSearchForNotebookItemsIntent](./insearchfornotebookitemsintent.md)
  A request to search for notes, tasks, and reminders.
- [class INSearchForNotebookItemsIntentResponse](./insearchfornotebookitemsintentresponse.md)
  Your app’s response to a request to search for notes, tasks, or reminders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintenthandling)*