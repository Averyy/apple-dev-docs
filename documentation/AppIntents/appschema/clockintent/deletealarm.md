# deleteAlarm

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that deletes the alarms.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var deleteAlarm: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `clock` domain and one of your app’s actions matches the `deleteAlarm` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .clock.deleteAlarm)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `deleteAlarm` schema:

```swift
@AppIntent(schema: .clock.deleteAlarm)
struct DeleteAlarmIntent: DeleteIntent {
    var entities: [<#AlarmEntity#>]

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## See Also

### Actions
- [var cancelTimer: some AppSchemaIntent](./canceltimer.md)
  An intent schema that cancels timers.
- [var createAlarm: some AppSchemaIntent](./createalarm.md)
  An intent schema that creates an alarm.
- [var createTimer: some AppSchemaIntent](./createtimer.md)
  An intent schema that creates a timer.
- [var dismissAlarm: some AppSchemaIntent](./dismissalarm.md)
  An intent schema that dismisses a firing or snoozed alarm.
- [var pauseTimer: some AppSchemaIntent](./pausetimer.md)
  An intent schema that pauses a timer.
- [var resumeTimer: some AppSchemaIntent](./resumetimer.md)
  An intent schema that resumes a timer.
- [var snoozeAlarm: some AppSchemaIntent](./snoozealarm.md)
  An intent schema that snoozes the firing alarm.
- [var updateAlarm: some AppSchemaIntent](./updatealarm.md)
  An intent schema that updates the alarm, for example, turn on / off the alarm, change the label, time, or repeating schedule.
- [var updateTimer: some AppSchemaIntent](./updatetimer.md)
  An intent schema that updates the timer’s attributes.
- [AppSchema.ClockIntent](../clockintent.md)
  Identifies intent schemas in the clock domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/clockintent/deletealarm)*