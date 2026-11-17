# snoozeAlarm

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that snoozes the firing alarm.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var snoozeAlarm: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `clock` domain and one of your app’s actions matches the `snoozeAlarm` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .clock.snoozeAlarm)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `snoozeAlarm` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `clock_snoozeAlarm` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .clock.snoozeAlarm)
struct SnoozeAlarmIntent {
    /// Alarm to snooze.
    var alarm: <#AlarmEntity#>

    /// Snooze duration.
    var duration: Duration

    func perform() async throws -> some ReturnsValue<<#AlarmEntity#>> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the snooze-alarm intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `alarm` | `@AppEntity(schema: .clock.alarm)` | Your app | Alarm to snooze. `AlarmEntity` is a placeholder name for a type that conforms to the [`alarm`](../clockentity/alarm.md) entity schema, which your app defines and implements. |
| `duration` | `Duration` | Swift | Snooze duration. |

## See Also

### Actions
- [var cancelTimer: some AppSchemaIntent](./canceltimer.md)
  An intent schema that cancels timers.
- [var createAlarm: some AppSchemaIntent](./createalarm.md)
  An intent schema that creates an alarm.
- [var createTimer: some AppSchemaIntent](./createtimer.md)
  An intent schema that creates a timer.
- [var deleteAlarm: some AppSchemaIntent](./deletealarm.md)
  An intent schema that deletes the alarms.
- [var dismissAlarm: some AppSchemaIntent](./dismissalarm.md)
  An intent schema that dismisses a firing or snoozed alarm.
- [var pauseTimer: some AppSchemaIntent](./pausetimer.md)
  An intent schema that pauses a timer.
- [var resumeTimer: some AppSchemaIntent](./resumetimer.md)
  An intent schema that resumes a timer.
- [var updateAlarm: some AppSchemaIntent](./updatealarm.md)
  An intent schema that updates the alarm, for example, turn on / off the alarm, change the label, time, or repeating schedule.
- [var updateTimer: some AppSchemaIntent](./updatetimer.md)
  An intent schema that updates the timer’s attributes.
- [AppSchema.ClockIntent](../clockintent.md)
  Identifies intent schemas in the clock domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/clockintent/snoozealarm)*