# INDeleteTasksTaskUnsupportedReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the reason the app can’t support the delete task request.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: INDeleteTasksTaskUnsupportedReason is deprecated. There is no replacement.

## Declaration

```swift
enum INDeleteTasksTaskUnsupportedReason
```

```c
enum INDeleteTasksTaskUnsupportedReason : NSInteger;
```

## Topics

### Reasons
- [INDeleteTasksTaskUnsupportedReason.noTasksFound](./indeletetaskstaskunsupportedreason/notasksfound.md)
  No relevant tasks found.
- [INDeleteTasksTaskUnsupportedReason.noTasksInApp](./indeletetaskstaskunsupportedreason/notasksinapp.md)
  No tasks exist in the app.
### Initializers
- [init?(rawValue: Int)](./indeletetaskstaskunsupportedreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a Resolution Result
- [init(taskResolutionResult: INTaskResolutionResult)](./indeletetaskstaskresolutionresult/init%28taskresolutionresult%29.md)
  Creates an object whose resolution involves successfully deleting a task.
- [class func unsupported(forReason: INDeleteTasksTaskUnsupportedReason) -> Self](./indeletetaskstaskresolutionresult/unsupported%28forreason%29.md)
  Creates an object whose resolution requires the user to confirm the task before continuing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetaskstaskunsupportedreason)*