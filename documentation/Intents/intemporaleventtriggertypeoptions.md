# INTemporalEventTriggerTypeOptions

**Framework**: Intents  
**Kind**: struct  
**Role**: Structure

Constants indicating how often to trigger an event.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: INTemporalEventTriggerTypeOptions is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
struct INTemporalEventTriggerTypeOptions
```

```c
enum INTemporalEventTriggerTypeOptions : NSUInteger;
```

## Topics

### Temporal Event Triggers
- [static var notScheduled: INTemporalEventTriggerTypeOptions](./intemporaleventtriggertypeoptions/notscheduled.md)
  No temporal event trigger scheduled.
- [static var scheduledNonRecurring: INTemporalEventTriggerTypeOptions](./intemporaleventtriggertypeoptions/schedulednonrecurring.md)
  A single scheduled temporal event trigger.
- [static var scheduledRecurring: INTemporalEventTriggerTypeOptions](./intemporaleventtriggertypeoptions/scheduledrecurring.md)
  A recurring, scheduled temporal event trigger.
### Initializers
- [init(rawValue: UInt)](./intemporaleventtriggertypeoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Searching for Tasks by Their Priority
- [var taskPriority: INTaskPriority](./insearchfornotebookitemsintent/taskpriority.md)
- [enum INTaskPriority](./intaskpriority.md)
  Constants indicating the priority for a task.
- [var temporalEventTriggerTypes: INTemporalEventTriggerTypeOptions](./insearchfornotebookitemsintent/temporaleventtriggertypes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intemporaleventtriggertypeoptions)*