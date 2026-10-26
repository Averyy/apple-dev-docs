# tasks

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The individual tasks found by the search.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntentResponse is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var tasks: [INTask]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<INTask *> * tasks;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSArray<INTask *> * tasks;
```

#### Discussion

When searching for items of type [`INNotebookItemType.task`](../innotebookitemtype/task.md) or `reminder`, put the results of your search in this property. Assign a value to the [`sortType`](./sorttype.md) property that indicates how you sorted the results.

## See Also

### Specifying the Search Results
- [var notes: [INNote]?](./notes.md)
  The notes found by the search.
- [var taskLists: [INTaskList]?](./tasklists.md)
  The task lists found by the search.
- [var sortType: INSortType](./sorttype.md)
  An indicator of how you sorted the search results.
- [enum INSortType](../insorttype.md)
  Constants indicating how the intent sorted the search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintentresponse/tasks)*