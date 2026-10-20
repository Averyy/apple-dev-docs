# AppSchema.ClockEnum

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies enum schemas in the clock domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol ClockEnum : AppSchema.Kind
```

## Topics

### Instance Properties
- [var alarmTriggerState: some AppSchemaEnum](./clockenum/alarmtriggerstate.md)
  An enum schema for an alarm trigger state parameter.
- [var stopwatchState: some AppSchemaEnum](./clockenum/stopwatchstate.md)
  An enum schema for a stopwatch state parameter.
- [var timerState: some AppSchemaEnum](./clockenum/timerstate.md)
  An enum schema for a timer state parameter.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Enum](./enum.md)

## See Also

### Types for static parameters
- [var alarmTriggerState: some AppSchemaEnum](./clockenum/alarmtriggerstate.md)
  An enum schema for an alarm trigger state parameter.
- [var timerState: some AppSchemaEnum](./clockenum/timerstate.md)
  An enum schema for a timer state parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/clockenum)*