# AppSchema.ClockEntity

**Framework**: App Intents  
**Kind**: protocol

Identifies entity schemas in the clock domain.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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