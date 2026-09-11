# AppSchema.CalendarIntent

**Framework**: App Intents  
**Kind**: protocol

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
- [var createEvent: some AppSchemaIntent](appschema/calendarintent/createevent.md)
  An intent schema that creates a calendar event.
- [var deleteEvent: some AppSchemaIntent](appschema/calendarintent/deleteevent.md)
  An intent schema that deletes a calendar event.
- [var updateEvent: some AppSchemaIntent](appschema/calendarintent/updateevent.md)
  An intent schema that updates a calendar event.

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Intent](appschema/intent.md)

## See Also

- [var createEvent: some AppSchemaIntent](appschema/calendarintent/createevent.md)
  An intent schema that creates a calendar event.
- [var deleteEvent: some AppSchemaIntent](appschema/calendarintent/deleteevent.md)
  An intent schema that deletes a calendar event.
- [var updateEvent: some AppSchemaIntent](appschema/calendarintent/updateevent.md)
  An intent schema that updates a calendar event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/calendarintent)*