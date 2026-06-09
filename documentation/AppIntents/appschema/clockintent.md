# AppSchema.ClockIntent

**Framework**: App Intents  
**Kind**: protocol

Identifies intent schemas in the clock domain.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol ClockIntent : AppSchema.Kind
```

## Topics

### Instance Properties
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
- [var lapStopwatch: some AppSchemaIntent](appschema/clockintent/lapstopwatch.md)
  An intent schema that laps the stopwatch.
- [var pauseTimer: some AppSchemaIntent](appschema/clockintent/pausetimer.md)
  An intent schema that pauses a timer.
- [var resetStopwatch: some AppSchemaIntent](appschema/clockintent/resetstopwatch.md)
  An intent schema that resets the stopwatch.
- [var resumeTimer: some AppSchemaIntent](appschema/clockintent/resumetimer.md)
  An intent schema that resumes a timer.
- [var snoozeAlarm: some AppSchemaIntent](appschema/clockintent/snoozealarm.md)
  An intent schema that snoozes the firing alarm.
- [var startStopwatch: some AppSchemaIntent](appschema/clockintent/startstopwatch.md)
  An intent schema that starts the stopwatch.
- [var stopStopwatch: some AppSchemaIntent](appschema/clockintent/stopstopwatch.md)
  An intent schema that stops the stopwatch.
- [var updateAlarm: some AppSchemaIntent](appschema/clockintent/updatealarm.md)
  An intent schema that updates the alarm, for example, turn on / off the alarm, change the label, time, or repeating schedule.
- [var updateTimer: some AppSchemaIntent](appschema/clockintent/updatetimer.md)
  An intent schema that updates the timer’s attributes.

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Intent](appschema/intent.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/clockintent)*