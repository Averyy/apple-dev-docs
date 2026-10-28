# notes

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The notes found by the search.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntentResponse is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var notes: [INNote]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<INNote *> * notes;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSArray<INNote *> * notes;
```

## Discussion

When searching for items of type [`INNotebookItemType.note`](../innotebookitemtype/note.md), put the results of your search in this property. Assign a value to the [`sortType`](./sorttype.md) property that indicates how you sorted the results.

## See Also

### Specifying the Search Results
- [var taskLists: [INTaskList]?](./tasklists.md)
  The task lists found by the search.
- [var tasks: [INTask]?](./tasks.md)
  The individual tasks found by the search.
- [var sortType: INSortType](./sorttype.md)
  An indicator of how you sorted the search results.
- [enum INSortType](../insorttype.md)
  Constants indicating how the intent sorted the search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintentresponse/notes)*