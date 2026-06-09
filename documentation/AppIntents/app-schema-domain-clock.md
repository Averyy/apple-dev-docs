# Clock

**Framework**: App Intents

Make your clock app’s actions available to Apple Intelligence and Siri by adopting schemas for common alarm and timer actions.

#### Overview

The `.clock` domain defines app schemas that provide a structured representation for common alarm and timer actions and content. Apply schemas in the `.clock` domain to make your app’s clock functionality available to Apple Intelligence and Siri. Each schema defines the requirements for intents, parameters, and results so people get a consistent experience across clock apps. For example, a person can set an alarm on different apps that support the [`createAlarm`](appschema/clockintent/createalarm.md) schema with the same phrases.

The following table maps example phrases that apply to each schema. Your app needs to support all of these schemas when it supports any one of them.

| Clock intent schemas | Example phrases |
| --- | --- |
| [`createAlarm`](appschema/clockintent/createalarm.md) | “Set an alarm.” or “Wake me up at 7 AM.” |
| [`updateAlarm`](appschema/clockintent/updatealarm.md) | “Change my alarm.” or “Change the 7 AM alarm to 8 AM.” |
| [`snoozeAlarm`](appschema/clockintent/snoozealarm.md) | “Snooze.” or “Give me 5 more minutes.” |
| [`dismissAlarm`](appschema/clockintent/dismissalarm.md) | “Dismiss the alarm.” or “Stop the alarm.” |
| [`deleteAlarm`](appschema/clockintent/deletealarm.md) | “Delete my alarm.” or “Remove the 7 AM alarm.” |
| [`createTimer`](appschema/clockintent/createtimer.md) | “Set a timer.” or “Timer for 5 minutes.” |
| [`updateTimer`](appschema/clockintent/updatetimer.md) | “Add 5 minutes to the timer.” or “Change the timer to 10 minutes.” |
| [`pauseTimer`](appschema/clockintent/pausetimer.md) | “Pause the timer.” |
| [`resumeTimer`](appschema/clockintent/resumetimer.md) | “Resume the timer.” or “Start the timer again.” |
| [`cancelTimer`](appschema/clockintent/canceltimer.md) | “Cancel the timer.” or “Stop the timer.” |

At build time, Xcode validates whether your app implements all the schemas in the group.

> 💡 **Tip**: Xcode generates a template implementation when you type `clock_` and select a schema from the suggestions list.

For more information about making your app’s actions available to Apple Intelligence and Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

## Topics

### Actions
- [var cancelTimer: some AppSchemaIntent](appschema/clockintent/canceltimer.md)
  An intent schema that cancels timers.
- [var createAlarm: some AppSchemaIntent](appschema/clockintent/createalarm.md)
  An intent schema that creates an alarm.
- [var createTimer: some AppSchemaIntent](appschema/clockintent/createtimer.md)
  An intent schema that creates a timer.
- [var deleteAlarm: some AppSchemaIntent](appschema/clockintent/deletealarm.md)
  An intent schema that deletes the alarms.
- [var dismissAlarm: some AppSchemaIntent](appschema/clockintent/dismissalarm.md)
  An intent schema that dismisses a firing or snoozed alarm.
- [var pauseTimer: some AppSchemaIntent](appschema/clockintent/pausetimer.md)
  An intent schema that pauses a timer.
- [var resumeTimer: some AppSchemaIntent](appschema/clockintent/resumetimer.md)
  An intent schema that resumes a timer.
- [var snoozeAlarm: some AppSchemaIntent](appschema/clockintent/snoozealarm.md)
  An intent schema that snoozes the firing alarm.
- [var updateAlarm: some AppSchemaIntent](appschema/clockintent/updatealarm.md)
  An intent schema that updates the alarm, for example, turn on / off the alarm, change the label, time, or repeating schedule.
- [var updateTimer: some AppSchemaIntent](appschema/clockintent/updatetimer.md)
  An intent schema that updates the timer’s attributes.
- [AppSchema.ClockIntent](appschema/clockintent.md)
  Identifies intent schemas in the clock domain.
### Content and parameter types
- [var alarm: some AppSchemaEntity](appschema/clockentity/alarm.md)
  An entity schema for an alarm.
- [var timer: some AppSchemaEntity](appschema/clockentity/timer.md)
  An entity schema for a timer.
- [AppSchema.ClockEntity](appschema/clockentity.md)
  Identifies entity schemas in the clock domain.
### Types for static parameters
- [var alarmTriggerState: some AppSchemaEnum](appschema/clockenum/alarmtriggerstate.md)
  An enum schema for an alarm trigger state parameter.
- [var timerState: some AppSchemaEnum](appschema/clockenum/timerstate.md)
  An enum schema for a timer state parameter.
- [AppSchema.ClockEnum](appschema/clockenum.md)
  Identifies enum schemas in the clock domain.

## See Also

- [Audio](app-schema-domain-audio.md)
  Make your audio app’s actions available to Apple Intelligence and Siri by adopting schemas for common audio playback actions.
- [Calendar](app-schema-domain-calendar.md)
  Make your calendar app’s actions available to Apple Intelligence and Siri by adopting schemas for common calendar actions.
- [Camera](app-schema-domain-camera.md)
  Make your camera app’s actions available to Apple Intelligence and Siri by adopting schemas for common camera actions.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-clock)*