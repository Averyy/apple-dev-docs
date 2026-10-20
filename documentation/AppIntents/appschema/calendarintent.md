# AppSchema.CalendarIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies intent schemas in the calendar domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol CalendarIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var createEvent: some AppSchemaIntent](./calendarintent/createevent.md)
  An intent schema that creates a calendar event.
- [var deleteEvent: some AppSchemaIntent](./calendarintent/deleteevent.md)
  An intent schema that deletes a calendar event.
- [var updateEvent: some AppSchemaIntent](./calendarintent/updateevent.md)
  An intent schema that updates a calendar event.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Intent](./intent.md)

## See Also

### Actions
- [var createEvent: some AppSchemaIntent](./calendarintent/createevent.md)
  An intent schema that creates a calendar event.
- [var deleteEvent: some AppSchemaIntent](./calendarintent/deleteevent.md)
  An intent schema that deletes a calendar event.
- [var updateEvent: some AppSchemaIntent](./calendarintent/updateevent.md)
  An intent schema that updates a calendar event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/calendarintent)*