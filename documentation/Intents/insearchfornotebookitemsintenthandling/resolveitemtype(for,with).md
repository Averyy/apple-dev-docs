# resolveItemType(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the type of items to search.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
optional func resolveItemType(for intent: INSearchForNotebookItemsIntent, with completion: @escaping @Sendable (INNotebookItemTypeResolutionResult) -> Void)
```

```swift
optional func resolveItemType(for intent: INSearchForNotebookItemsIntent) async -> INNotebookItemTypeResolutionResult
```

```objc
- (void) resolveItemTypeForSearchForNotebookItems:(INSearchForNotebookItemsIntent *) intent withCompletion:(void (^)(INNotebookItemTypeResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve the type of items to search for. Use this method to verify that you can search for items of the specified type. If you support searching for the items, return a successful resolution with that item type. For types you do not support, you can return a successful resolution with a type that you do support. Alternatively, if you do not want to search an unsupported type, return a not required resolution from this method and use your confirmation method to indicate that a failure occurred.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the item type that you intend to include in your search results.

## See Also

### Resolving the Intent Parameters
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
- [func resolveLocation(for: INSearchForNotebookItemsIntent, with: (INPlacemarkResolutionResult) -> Void)](./resolvelocation%28for,with%29.md)
  Resolves how to use a location value during the search.
- [func resolveLocationSearchType(for: INSearchForNotebookItemsIntent, with: (INLocationSearchTypeResolutionResult) -> Void)](./resolvelocationsearchtype%28for,with%29.md)
  Resolves the location to use during a location-based search.
- [func resolveTaskPriority(for: INSearchForNotebookItemsIntent, with: (INTaskPriorityResolutionResult) -> Void)](./resolvetaskpriority%28for,with%29.md)
  Resolves the priority to use during a priority-based search.
- [func resolveTemporalEventTriggerTypes(for: INSearchForNotebookItemsIntent, with: (INTemporalEventTriggerTypeOptionsResolutionResult) -> Void)](./resolvetemporaleventtriggertypes%28for,with%29.md)
  Resolves the trigger type to use during a temporal-based search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintenthandling/resolveitemtype(for:with:))*