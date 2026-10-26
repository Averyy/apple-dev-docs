# sortType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An indicator of how you sorted the search results.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntentResponse is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var sortType: INSortType { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readwrite) INSortType sortType;
```

*macOS*

```objc
@property (atomic, assign, readwrite) INSortType sortType;
```

#### Discussion

After assigning the search results to the appropriate property of your response object, update this property to specify how you sorted the results.

## See Also

### Specifying the Search Results
- [var notes: [INNote]?](./notes.md)
  The notes found by the search.
- [var taskLists: [INTaskList]?](./tasklists.md)
  The task lists found by the search.
- [var tasks: [INTask]?](./tasks.md)
  The individual tasks found by the search.
- [enum INSortType](../insorttype.md)
  Constants indicating how the intent sorted the search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintentresponse/sorttype)*