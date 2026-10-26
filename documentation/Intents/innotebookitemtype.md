# INNotebookItemType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the types of items to search.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INNotebookItemType is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
enum INNotebookItemType
```

```c
enum INNotebookItemType : NSInteger;
```

## Topics

### Enumeration Cases
- [INNotebookItemType.unknown](./innotebookitemtype/unknown.md)
  An unknown type of item.
- [INNotebookItemType.note](./innotebookitemtype/note.md)
  A note item type.
- [INNotebookItemType.taskList](./innotebookitemtype/tasklist.md)
  A task list item type.
- [INNotebookItemType.task](./innotebookitemtype/task.md)
  A task item type.
### Initializers
- [init?(rawValue: Int)](./innotebookitemtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Searching by Type
- [var itemType: INNotebookItemType](./insearchfornotebookitemsintent/itemtype.md)
  The type of items to include in your search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innotebookitemtype)*