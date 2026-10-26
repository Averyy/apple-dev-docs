# resolveTaskPriority(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the priority to use during a priority-based search.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
optional func resolveTaskPriority(for intent: INSearchForNotebookItemsIntent, with completion: @escaping @Sendable (INTaskPriorityResolutionResult) -> Void)
```

```swift
optional func resolveTaskPriority(for intent: INSearchForNotebookItemsIntent) async -> INTaskPriorityResolutionResult
```

```objc
- (void) resolveTaskPriorityForSearchForNotebookItems:(INSearchForNotebookItemsIntent *) intent withCompletion:(void (^)(INTaskPriorityResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to verify that you can perform a location-based search using the specified information. Consider the value of the [`taskPriority`](../insearchfornotebookitemsintent/taskpriority.md) property of the intent when determining your response. If the task type is unknown, return a value of not required to indicate that you do not intend to use the priority information during the search. If the search type is a different value, return a successful resolution if the [`taskPriority`](../insearchfornotebookitemsintent/taskpriority.md) property of the intent contains enough information to perform the search. Return a different result if it does not.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the location information that you intend to use during the search.

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
- [func resolveLocation(for: INSearchForNotebookItemsIntent, with: (INPlacemarkResolutionResult) -> Void)](./resolvelocation%28for,with%29.md)
  Resolves how to use a location value during the search.
- [func resolveLocationSearchType(for: INSearchForNotebookItemsIntent, with: (INLocationSearchTypeResolutionResult) -> Void)](./resolvelocationsearchtype%28for,with%29.md)
  Resolves the location to use during a location-based search.
- [func resolveTemporalEventTriggerTypes(for: INSearchForNotebookItemsIntent, with: (INTemporalEventTriggerTypeOptionsResolutionResult) -> Void)](./resolvetemporaleventtriggertypes%28for,with%29.md)
  Resolves the trigger type to use during a temporal-based search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintenthandling/resolvetaskpriority(for:with:))*