# Calendar

**Framework**: App Intents

Make your calendar app’s actions available to Apple Intelligence and Siri by adopting schemas for common calendar actions.

#### Overview

The `.calendar` domain defines app schemas that provide a structured representation for common calendar actions and content. Apply schemas in the `.calendar` domain to make your app’s calendar functionality available to Apple Intelligence and Siri.

The following table maps example phrases that apply to each schema:

| Calendar intent schemas | Example phrases |
| --- | --- |
| [`createEvent`](appschema/calendarintent/createevent.md) | “Create an event.” or “Schedule a meeting with Bill tomorrow at 2 PM.” |
| [`deleteEvent`](appschema/calendarintent/deleteevent.md) | “Delete this event.” or “Cancel the meeting.” |
| [`updateEvent`](appschema/calendarintent/updateevent.md) | “Reschedule the meeting.” or “Move the meeting to tomorrow.” |

> 💡 **Tip**: Xcode generates a template implementation when you type `calendar_` and select a schema from the suggestions list.

For more information about making your app’s actions available to Apple Intelligence and Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

## Topics

### Essentials
- [Integrating your calendar app with Apple Intelligence](integrating-your-calendar-app-with-apple-intelligence.md)
  Adopt calendar schemas so people can create, find, and manage events with Siri.
### Actions
- [var createEvent: some AppSchemaIntent](appschema/calendarintent/createevent.md)
  An intent schema that creates a calendar event.
- [var deleteEvent: some AppSchemaIntent](appschema/calendarintent/deleteevent.md)
  An intent schema that deletes a calendar event.
- [var updateEvent: some AppSchemaIntent](appschema/calendarintent/updateevent.md)
  An intent schema that updates a calendar event.
- [AppSchema.CalendarIntent](appschema/calendarintent.md)
  Identifies intent schemas in the calendar domain.
### Content and parameter types
- [var attendee: some AppSchemaEntity](appschema/calendarentity/attendee.md)
  An entity schema for an attendee.
- [var calendar: some AppSchemaEntity](appschema/calendarentity/calendar.md)
  An entity schema for a calendar.
- [var event: some AppSchemaEntity](appschema/calendarentity/event.md)
  An entity schema for an event.
- [AppSchema.CalendarEntity](appschema/calendarentity.md)
  Identifies entity schemas in the calendar domain.
### Types for static parameters
- [var attendeeStatus: some AppSchemaEnum](appschema/calendarenum/attendeestatus.md)
  An enum schema for an attendee status parameter.
- [var attendeeType: some AppSchemaEnum](appschema/calendarenum/attendeetype.md)
  An enum schema for an attendee type parameter.
- [var eventSpan: some AppSchemaEnum](appschema/calendarenum/eventspan.md)
  An enum schema for an event span parameter.
- [var eventStatus: some AppSchemaEnum](appschema/calendarenum/eventstatus.md)
  An enum schema for an event status parameter.
- [AppSchema.CalendarEnum](appschema/calendarenum.md)
  Identifies enum schemas in the calendar domain.

## See Also

- [Audio](app-schema-domain-audio.md)
  Make your audio app’s actions available to Apple Intelligence and Siri by adopting schemas for common audio playback actions.
- [Camera](app-schema-domain-camera.md)
  Make your camera app’s actions available to Apple Intelligence and Siri by adopting schemas for common camera actions.
- [Clock](app-schema-domain-clock.md)
  Make your clock app’s actions available to Apple Intelligence and Siri by adopting schemas for common alarm and timer actions.
- [Files](app-schema-domain-files.md)
  Make your file-management app’s actions available to Apple Intelligence and Siri by adopting schemas for common file actions.
- [Mail](app-schema-domain-mail.md)
  Make your email app’s actions available to Apple Intelligence and Siri by adopting schemas for common email actions.
- [Maps](app-schema-domain-maps.md)
  Make your navigation app’s actions available to Apple Intelligence and Siri by adopting schemas for common navigation actions.
- [Messages](app-schema-domain-messages.md)
  Make your messaging app’s actions available to Apple Intelligence and Siri by adopting schemas for common messaging actions.
- [Notes](app-schema-domain-notes.md)
  Make your note-taking app’s actions available to Apple Intelligence and Siri by adopting schemas for common note actions.
- [Phone](app-schema-domain-phone.md)
  Make your phone app’s actions available to Apple Intelligence and Siri by adopting schemas for calling actions.
- [Photos](app-schema-domain-photos.md)
  Make your photo and video app’s actions available to Apple Intelligence and Siri by adopting schemas for common photo and video actions.
- [Reminders](app-schema-domain-reminders.md)
  Make your reminder app’s actions available to Apple Intelligence and Siri by adopting schemas for common reminder actions.
- [System and in-app search](app-schema-domain-system-and-in-app-search.md)
  Make your app’s actions available to Apple Intelligence and Siri by adopting schemas for in-app search and content access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-calendar)*