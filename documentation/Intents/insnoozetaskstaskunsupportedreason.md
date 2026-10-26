# INSnoozeTasksTaskUnsupportedReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that indicates the reason the app can’t support the snooze task request.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
enum INSnoozeTasksTaskUnsupportedReason
```

```c
enum INSnoozeTasksTaskUnsupportedReason : NSInteger;
```

## Topics

### Constants
- [INSnoozeTasksTaskUnsupportedReason.noTasksFound](./insnoozetaskstaskunsupportedreason/notasksfound.md)
  A resolution result that indicates no tasks were found.
### Initializers
- [init?(rawValue: Int)](./insnoozetaskstaskunsupportedreason/init%28rawvalue%29.md)

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
- [init(taskResolutionResult: INTaskResolutionResult)](./insnoozetaskstaskresolutionresult/init%28taskresolutionresult%29.md)
  Creates an object whose resolution involves successfully snoozing a task.
- [class func unsupported(forReason: INSnoozeTasksTaskUnsupportedReason) -> Self](./insnoozetaskstaskresolutionresult/unsupported%28forreason%29.md)
  Creates an object whose resolution requires the user to confirm the task to be snoozed before continuing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insnoozetaskstaskunsupportedreason)*