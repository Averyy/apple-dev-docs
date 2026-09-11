# AppSchema.ClockEntity

**Framework**: App Intents  
**Kind**: protocol

Identifies entity schemas in the clock domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol ClockEntity : AppSchema.Kind
```

## Topics

### Instance Properties
- [var alarm: some AppSchemaEntity](appschema/clockentity/alarm.md)
  An entity schema for an alarm.
- [var stopwatch: some AppSchemaEntity](appschema/clockentity/stopwatch.md)
  An entity schema for a stopwatch.
- [var timer: some AppSchemaEntity](appschema/clockentity/timer.md)
  An entity schema for a timer.

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Entity](appschema/entity.md)

## See Also

- [var alarm: some AppSchemaEntity](appschema/clockentity/alarm.md)
  An entity schema for an alarm.
- [var timer: some AppSchemaEntity](appschema/clockentity/timer.md)
  An entity schema for a timer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/clockentity)*