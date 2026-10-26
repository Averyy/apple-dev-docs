# INTaskPriority

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the priority for a task.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: INTaskPriority is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
enum INTaskPriority
```

```c
enum INTaskPriority : NSInteger;
```

## Topics

### Constants
- [INTaskPriority.flagged](./intaskpriority/flagged.md)
  A task the user flagged.
- [INTaskPriority.notFlagged](./intaskpriority/notflagged.md)
  A task the user didn’t flag.
- [INTaskPriority.unknown](./intaskpriority/unknown.md)
  The task’s priority isn’t known.
### Initializers
- [init?(rawValue: Int)](./intaskpriority/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Searching for Tasks by Their Priority
- [var taskPriority: INTaskPriority](./insearchfornotebookitemsintent/taskpriority.md)
- [var temporalEventTriggerTypes: INTemporalEventTriggerTypeOptions](./insearchfornotebookitemsintent/temporaleventtriggertypes.md)
- [struct INTemporalEventTriggerTypeOptions](./intemporaleventtriggertypeoptions.md)
  Constants indicating how often to trigger an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intaskpriority)*