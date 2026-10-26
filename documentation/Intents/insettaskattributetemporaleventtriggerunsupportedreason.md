# INSetTaskAttributeTemporalEventTriggerUnsupportedReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Reasons the app can’t modify the temporal event trigger of the task.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
enum INSetTaskAttributeTemporalEventTriggerUnsupportedReason
```

```c
enum INSetTaskAttributeTemporalEventTriggerUnsupportedReason : NSInteger;
```

## Topics

### Reasons
- [INSetTaskAttributeTemporalEventTriggerUnsupportedReason.invalidRecurrence](./insettaskattributetemporaleventtriggerunsupportedreason/invalidrecurrence.md)
  The temporal event trigger refers to an invalid or unsupported schedule for repeating a task.
- [INSetTaskAttributeTemporalEventTriggerUnsupportedReason.timeInPast](./insettaskattributetemporaleventtriggerunsupportedreason/timeinpast.md)
  The temporal event trigger refers to a moment or time span that has already occurred.
### Initializers
- [init?(rawValue: Int)](./insettaskattributetemporaleventtriggerunsupportedreason/init%28rawvalue%29.md)

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
- [init(temporalEventTriggerResolutionResult: INTemporalEventTriggerResolutionResult)](./insettaskattributetemporaleventtriggerresolutionresult/init%28temporaleventtriggerresolutionresult%29.md)
  Creates an object with a resolution that successfully matches the specified temporal event.
- [class func unsupported(forReason: INSetTaskAttributeTemporalEventTriggerUnsupportedReason) -> Self](./insettaskattributetemporaleventtriggerresolutionresult/unsupported%28forreason%29.md)
  Creates an object with a resolution that provides a reason the temporal event trigger can’t be applied to the task the user intends to modify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributetemporaleventtriggerunsupportedreason)*