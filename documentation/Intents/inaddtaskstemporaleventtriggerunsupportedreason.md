# INAddTasksTemporalEventTriggerUnsupportedReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Reasons the app can’t create a task with a particular temporal event trigger.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
enum INAddTasksTemporalEventTriggerUnsupportedReason
```

```c
enum INAddTasksTemporalEventTriggerUnsupportedReason : NSInteger;
```

## Topics

### Reasons
- [INAddTasksTemporalEventTriggerUnsupportedReason.invalidRecurrence](./inaddtaskstemporaleventtriggerunsupportedreason/invalidrecurrence.md)
  The temporal event trigger refers to an invalid or unsupported schedule for repeating a task.
- [INAddTasksTemporalEventTriggerUnsupportedReason.timeInPast](./inaddtaskstemporaleventtriggerunsupportedreason/timeinpast.md)
  The temporal event trigger refers to a moment or time span which has already occurred.
### Initializers
- [init?(rawValue: Int)](./inaddtaskstemporaleventtriggerunsupportedreason/init%28rawvalue%29.md)

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
- [init(temporalEventTriggerResolutionResult: INTemporalEventTriggerResolutionResult)](./inaddtaskstemporaleventtriggerresolutionresult/init%28temporaleventtriggerresolutionresult%29.md)
  Creates an object whose resolution successfully matches the specified temporal event.
- [class func unsupported(forReason: INAddTasksTemporalEventTriggerUnsupportedReason) -> Self](./inaddtaskstemporaleventtriggerresolutionresult/unsupported%28forreason%29.md)
  Creates an object whose resolution provides a reason why the temporal event trigger cannot be applied to the task the user intends to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtaskstemporaleventtriggerunsupportedreason)*