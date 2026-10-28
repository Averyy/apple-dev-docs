# INNotebookItemType.task

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A task item type.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INNotebookItemType is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case task
```

```c
INNotebookItemTypeTask
```

## Discussion

Search your app’s tasks and return each one using an [`INTask`](../intask.md) object. A task is usually contained within a task list, but may be standalone if your app does not support task lists.

## See Also

### Enumeration Cases
- [INNotebookItemType.unknown](./unknown.md)
  An unknown type of item.
- [INNotebookItemType.note](./note.md)
  A note item type.
- [INNotebookItemType.taskList](./tasklist.md)
  A task list item type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innotebookitemtype/task)*