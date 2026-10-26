# resolveLocation(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves how to use a location value during the search.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
optional func resolveLocation(for intent: INSearchForNotebookItemsIntent, with completion: @escaping @Sendable (INPlacemarkResolutionResult) -> Void)
```

```swift
optional func resolveLocation(for intent: INSearchForNotebookItemsIntent) async -> INPlacemarkResolutionResult
```

```objc
- (void) resolveLocationForSearchForNotebookItems:(INSearchForNotebookItemsIntent *) intent withCompletion:(void (^)(INPlacemarkResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve how to use a location value during the search. Use this method to verify that you can perform a location-based search for the type specified by the [`locationSearchType`](../insearchfornotebookitemsintent/locationsearchtype.md) property of the intent. If the type is [`INLocationSearchType.unknown`](../inlocationsearchtype/unknown.md) or you do not consider locations when performing the search, you can return a resolution indicating that the location type is not required. Return a successful resolution if you support searching using the specified type or return a different result if you do not support the specific type requested by the user.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the search type that you support.

## See Also

### Resolving the Intent Parameters
- [func resolveItemType(for: INSearchForNotebookItemsIntent, with: (INNotebookItemTypeResolutionResult) -> Void)](./resolveitemtype%28for,with%29.md)
  Resolves the type of items to search.
- [func resolveTitle(for: INSearchForNotebookItemsIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvetitle%28for,with%29.md)
  Resolves the string to use when searching the title of notes, tasks, or reminders.
- [func resolveContent(for: INSearchForNotebookItemsIntent, with: (INStringResolutionResult) -> Void)](./resolvecontent%28for,with%29.md)
  Resolves the string to use when searching the content of notes.
- [func resolveStatus(for: INSearchForNotebookItemsIntent, with: (INTaskStatusResolutionResult) -> Void)](./resolvestatus%28for,with%29.md)
  Resolves the status value to use during the search.
- [func resolveDateSearchType(for: INSearchForNotebookItemsIntent, with: (INDateSearchTypeResolutionResult) -> Void)](./resolvedatesearchtype%28for,with%29.md)
  Resolves how to use a date value during the search.
- [func resolveDateTime(for: INSearchForNotebookItemsIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvedatetime%28for,with%29.md)
  Resolves the date to use during a date-based search.
- [func resolveLocationSearchType(for: INSearchForNotebookItemsIntent, with: (INLocationSearchTypeResolutionResult) -> Void)](./resolvelocationsearchtype%28for,with%29.md)
  Resolves the location to use during a location-based search.
- [func resolveTaskPriority(for: INSearchForNotebookItemsIntent, with: (INTaskPriorityResolutionResult) -> Void)](./resolvetaskpriority%28for,with%29.md)
  Resolves the priority to use during a priority-based search.
- [func resolveTemporalEventTriggerTypes(for: INSearchForNotebookItemsIntent, with: (INTemporalEventTriggerTypeOptionsResolutionResult) -> Void)](./resolvetemporaleventtriggertypes%28for,with%29.md)
  Resolves the trigger type to use during a temporal-based search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintenthandling/resolvelocation(for:with:))*