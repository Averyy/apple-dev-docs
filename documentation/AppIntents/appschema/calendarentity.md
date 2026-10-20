# AppSchema.CalendarEntity

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies entity schemas in the calendar domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol CalendarEntity : AppSchema.Kind
```

## Topics

### Instance Properties
- [var attendee: some AppSchemaEntity](./calendarentity/attendee.md)
  An entity schema for an attendee.
- [var calendar: some AppSchemaEntity](./calendarentity/calendar.md)
  An entity schema for a calendar.
- [var event: some AppSchemaEntity](./calendarentity/event.md)
  An entity schema for an event.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Entity](./entity.md)

## See Also

### Content and parameter types
- [var attendee: some AppSchemaEntity](./calendarentity/attendee.md)
  An entity schema for an attendee.
- [var calendar: some AppSchemaEntity](./calendarentity/calendar.md)
  An entity schema for a calendar.
- [var event: some AppSchemaEntity](./calendarentity/event.md)
  An entity schema for an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/calendarentity)*