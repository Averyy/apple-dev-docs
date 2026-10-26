# INSearchForNotebookItemsIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a request to search for notes, tasks, or reminders.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntentResponse is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class INSearchForNotebookItemsIntentResponse
```

```objc
@interface INSearchForNotebookItemsIntentResponse : INIntentResponse
```

#### Overview

Use an [`INSearchForNotebookItemsIntentResponse`](./insearchfornotebookitemsintentresponse.md) object to return the search results requested by the user. Siri communicates the information from your response to the user at appropriate times.

You create an [`INSearchForNotebookItemsIntentResponse`](./insearchfornotebookitemsintentresponse.md) object in the [`confirm(intent:completion:)`](./insearchfornotebookitemsintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./insearchfornotebookitemsintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INSearchForNotebookItemsIntentHandling`](./insearchfornotebookitemsintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INSearchForNotebookItemsIntentResponseCode, userActivity: NSUserActivity?)](./insearchfornotebookitemsintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INSearchForNotebookItemsIntentResponseCode](./insearchfornotebookitemsintentresponse/code.md)
  The code indicating whether your app successfully handled the intent.
- [enum INSearchForNotebookItemsIntentResponseCode](./insearchfornotebookitemsintentresponsecode.md)
  Constants indicating the state of the response.
### Specifying the Search Results
- [var notes: [INNote]?](./insearchfornotebookitemsintentresponse/notes.md)
  The notes found by the search.
- [var taskLists: [INTaskList]?](./insearchfornotebookitemsintentresponse/tasklists.md)
  The task lists found by the search.
- [var tasks: [INTask]?](./insearchfornotebookitemsintentresponse/tasks.md)
  The individual tasks found by the search.
- [var sortType: INSortType](./insearchfornotebookitemsintentresponse/sorttype.md)
  An indicator of how you sorted the search results.
- [enum INSortType](./insorttype.md)
  Constants indicating how the intent sorted the search results.

## Relationships

### Inherits From
- [INIntentResponse](./inintentresponse.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Notebook Search
- [protocol INSearchForNotebookItemsIntentHandling](./insearchfornotebookitemsintenthandling.md)
  The handler interface for searching for notes, tasks, and reminders.
- [class INSearchForNotebookItemsIntent](./insearchfornotebookitemsintent.md)
  A request to search for notes, tasks, and reminders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintentresponse)*