# INSortType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating how the intent sorted the search results.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSortType is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
enum INSortType
```

```c
enum INSortType : NSInteger;
```

## Topics

### Constants
- [INSortType.unknown](./insorttype/unknown.md)
  The sort order is unknown.
- [INSortType.asIs](./insorttype/asis.md)
  The sorted items are in the order returned.
- [INSortType.byDate](./insorttype/bydate.md)
  The sorted items are in date order.
### Initializers
- [init?(rawValue: Int)](./insorttype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Specifying the Search Results
- [var notes: [INNote]?](./insearchfornotebookitemsintentresponse/notes.md)
  The notes found by the search.
- [var taskLists: [INTaskList]?](./insearchfornotebookitemsintentresponse/tasklists.md)
  The task lists found by the search.
- [var tasks: [INTask]?](./insearchfornotebookitemsintentresponse/tasks.md)
  The individual tasks found by the search.
- [var sortType: INSortType](./insearchfornotebookitemsintentresponse/sorttype.md)
  An indicator of how you sorted the search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insorttype)*