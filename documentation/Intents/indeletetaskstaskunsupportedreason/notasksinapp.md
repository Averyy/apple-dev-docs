# INDeleteTasksTaskUnsupportedReason.noTasksInApp

**Framework**: Intents  
**Kind**: case  
**Role**: Case

No tasks exist in the app.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: INDeleteTasksTaskUnsupportedReason is deprecated. There is no replacement.

## Declaration

```swift
case noTasksInApp
```

```c
INDeleteTasksTaskUnsupportedReasonNoTasksInApp
```

#### Discussion

Use this reason when there are no tasks in the app. If tasks exist, but do not match the user’s intent, use [`INDeleteTasksTaskUnsupportedReason.noTasksFound`](./notasksfound.md)

## See Also

### Reasons
- [INDeleteTasksTaskUnsupportedReason.noTasksFound](./notasksfound.md)
  No relevant tasks found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetaskstaskunsupportedreason/notasksinapp)*