# INTaskType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating how the task behaves.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INTaskType is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
enum INTaskType
```

```c
enum INTaskType : NSInteger;
```

## Topics

### Constants
- [INTaskType.unknown](./intasktype/unknown.md)
  An unknown type of task.
- [INTaskType.notCompletable](./intasktype/notcompletable.md)
  A task that the intent can’t mark as completed.
- [INTaskType.completable](./intasktype/completable.md)
  A task that the intent can mark as completed.
### Initializers
- [init?(rawValue: Int)](./intasktype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Task Type
- [var taskType: INTaskType](./intask/tasktype.md)
  Information about the behavior of the task in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intasktype)*