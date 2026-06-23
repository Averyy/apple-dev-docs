# createTimer

**Framework**: App Intents  
**Kind**: property

An intent schema that creates a timer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var createTimer: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `clock` domain and one of your app’s actions matches the `createTimer` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .clock.createTimer)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `createTimer` schema:

```swift
@AppIntent(schema: .clock.createTimer)
struct CreateTimerIntent {
    var duration: Duration
    var label: String?
    var isSleepTimer: Bool

    func perform() async throws -> some ReturnsValue<<#TimerEntity#>> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var cancelTimer: some AppSchemaIntent](appschema/clockintent/canceltimer.md)
  An intent schema that cancels timers.
- [var createAlarm: some AppSchemaIntent](appschema/clockintent/createalarm.md)
  An intent schema that creates an alarm.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/clockintent/createtimer)*