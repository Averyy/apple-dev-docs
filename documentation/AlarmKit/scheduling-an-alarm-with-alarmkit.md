# Scheduling an alarm with AlarmKit

**Framework**: AlarmKit

Create prominent alerts at specified dates for your iOS app.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Xcode 26.0+ (Beta)

#### Overview

An alarm is an alert that presents at a pre-determined time based on a schedule or after a countdown. It overrides both a device’s focus and silent mode, if necessary.

This sample project uses AlarmKit to create and manage different types of alarms. In this app people can create and manage:

-  which alert only once at a specified time in the future.
-  which alert with a weekly cadence.
-  which alert after a countdown, and start immediately.

This project also includes a widget extension for setting up the custom countdown Live Activity associated with an alarm.

> **Note**: This sample code project is associated with WWDC25 session 230: [`Wake up to the AlarmKit API`](https://developer.apple.comhttps://developer.apple.com/wwdc25/230).

#### Authorize the App to Schedule Alarms

This sample prompts people to authorize the app to allow AlarmKit to schedule alarms and create alerts by calling [`requestAuthorization()`](alarmmanager/requestauthorization().md) on [`AlarmManager`](alarmmanager.md). Otherwise, when a person adds their first alarm, AlarmKit automatically requests this authorization on behalf of the app, before scheduling the alarm. If this sample doesn’t get this authorization, then any alarm created by the app isn’t scheduled and subsequently doesn’t alert.

```swift
do {
    let state = try await alarmManager.requestAuthorization()
    return state == .authorized
} catch {
    print("Error occurred while requesting authorization: \(error)")
    return false
}
```

The sample includes the [`NSAlarmKitUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAlarmKitUsageDescription) key in the app’s `Info.plist` with a descriptive string explaining why it schedules alarms. This string appears in the system prompt when requesting authorization, in this sample the string is:

```None
We'll schedule alerts for alarms you create within our app.
```

If the `NSAlarmKitUsageDescription` key is missing or its value is an empty string, apps can’t schedule alarms with AlarmKit.

#### Create the Alarm Schedule

The sample app creates an alarm with either, or both, a countdown duration and a schedule, based on the options a person sets.

[`Alarm.CountdownDuration`](alarm/countdownduration-swift.struct.md) uses the selected `TimeInterval` for the  pre-alert countdown, which displays the alert when the countdown reaches 0.

[`Alarm.Schedule`](alarm/schedule-swift.enum.md) enables people to set a one-time alarm, or configure a weekly schedule. For single-occurrence alarms, the [`repeats`](alarm/schedule-swift.enum/relative/repeats.md) property is set to [`Alarm.Schedule.Relative.Recurrence.never`](alarm/schedule-swift.enum/relative/recurrence/never.md). For recurring alarms, the `repeats` property is set to [`Alarm.Schedule.Relative.Recurrence.weekly(_:)`](alarm/schedule-swift.enum/relative/recurrence/weekly(_:).md) with an associated array `Locale.Weekday`, indicating the days of the week the alarm alerts.

```swift
let time = Alarm.Schedule.Relative.Time(hour: hour, minute: minute)
return .relative(.init(
    time: time,
    repeats: weekdays.isEmpty ? .never : .weekly(Array(weekdays))
))
```

#### Configure the Alarms Ui Attributes

AlarmKit provides a presentation for each of the three alarm states - [`AlarmPresentation.Alert`](alarmpresentation/alert-swift.struct.md), [`AlarmPresentation.Countdown`](alarmpresentation/countdown-swift.struct.md), and [`AlarmPresentation.Paused`](alarmpresentation/paused-swift.struct.md). Because `Countdown` and `Paused` are optional presentations, this sample doesn’t use them if the alarm only has an `Alert` state.

```swift
let alertContent = AlarmPresentation.Alert(title: userInput.localizedLabel,
        stopButton: .stopButton,
        secondaryButton: secondaryButton,
        secondaryButtonBehavior: secondaryButtonBehavior)

guard userInput.countdownDuration != nil else {
    // An alarm without countdown specifies only an alert state.
    return AlarmPresentation(alert: alertContent)
}

// With countdown enabled, provide a presentation for both a countdown and paused state.
let countdownContent = AlarmPresentation.Countdown(title: userInput.localizedLabel,
        pauseButton: .pauseButton)

let pausedContent = AlarmPresentation.Paused(title: "Paused",
        resumeButton: .resumeButton)

return AlarmPresentation(alert: alertContent, countdown: countdownContent, paused: pausedContent)
```

Alongside the [`stopButton`](alarmpresentation/alert-swift.struct/stopbutton.md), the sample includes another action button in the alerting UI. This action depends on [`secondaryButton`](alarmpresentation/alert-swift.struct/secondarybutton.md) and [`secondaryButtonBehavior`](alarmpresentation/alert-swift.struct/secondarybuttonbehavior-swift.property.md).

```swift
var secondaryButtonBehavior: AlarmPresentation.Alert.SecondaryButtonBehavior? {
    switch selectedSecondaryButton {
    case .none: nil
    case .countdown: .countdown
    case .openApp: .custom
    }
}
```

When the `secondaryButtonBehavior` property is set to [`AlarmPresentation.Alert.SecondaryButtonBehavior.countdown`](alarmpresentation/alert-swift.struct/secondarybuttonbehavior-swift.enum/countdown.md), the secondary button is a `Repeat` action, which re-triggers the alarm after a certain `TimeInterval`, as specified in [`postAlert`](alarm/countdownduration-swift.struct/postalert.md). If the `secondaryButtonBehavior` is set to [`AlarmPresentation.Alert.SecondaryButtonBehavior.custom`](alarmpresentation/alert-swift.struct/secondarybuttonbehavior-swift.enum/custom.md), the alarm alert displays an `Open` action to launch the app.

```swift
let secondaryButton: AlarmButton? = switch secondaryButtonBehavior {
    case .countdown: .repeatButton
    case .custom: .openAppButton
    default: nil
}
```

> **Note**: The system forwards the alert presentation to a paired watch (if any) to notify people when an alarm is alerting.

The content for these presentations is wrapped into [`ActivityAttributes`](https://developer.apple.com/documentation/ActivityKit/ActivityAttributes), along with [`tintColor`](alarmattributes/tintcolor.md), and [`metadata`](alarmattributes/metadata.md). The tint color associates the alarms with the sample app and also differentiates them from other app’s alarms on the person’s device.

```swift
let attributes = AlarmAttributes(presentation: alarmPresentation(with: userInput),
        metadata: CookingData(),
        tintColor: Color.blue)
```

#### Schedule the Configured Alarm

The sample uses a unique identifier to track alarms registered with AlarmKit. The sample manages and updates alarm states, such as [`pause(id:)`](alarmmanager/pause(id:).md) and [`cancel(id:)`](alarmmanager/cancel(id:).md), using this identifier.

When a person taps the button in the alerting UI, the [`AlarmManager`](alarmmanager.md) automatically handles stop or countdown functionalities, depending on the button type.

> 💡 **Tip**: You can add additional actions for each button type using [`App Intents`](https://developer.apple.com/documentation/AppIntents), which you can configure using [`AlarmManager.AlarmConfiguration`](alarmmanager/alarmconfiguration.md).

```swift
let id = UUID()
let alarmConfiguration = AlarmConfiguration(countdownDuration: userInput.countdownDuration,
        schedule: userInput.schedule,
        attributes: attributes,
        stopIntent: StopIntent(alarmID: id.uuidString),
        secondaryIntent: secondaryIntent(alarmID: id, userInput: userInput))
```

This sample creates the alarm ID and [`AlarmManager.AlarmConfiguration`](alarmmanager/alarmconfiguration.md) and schedules the alarm with [`AlarmManager`](alarmmanager.md).

```swift
let alarm = try await alarmManager.schedule(id: id, configuration: alarmConfiguration)
```

#### Observe State Changes on the Alarms

At initialization, the `ViewModel` subscribes to alarm events from [`shared`](alarmmanager/shared.md). This enables the sample app to have the latest state of an alarm even if the alarm state updated while the sample app isn’t running.

```swift
Task {
    for await incomingAlarms in alarmManager.alarmUpdates {
        updateAlarmState(with: incomingAlarms)
    }
}
```

> **Note**: An [`Alarm`](alarm.md) that’s not included in the [`alarmUpdates`](alarmmanager/alarmupdates-swift.property.md) asynchronous stream is no longer scheduled with AlarmKit.

#### Create a Widget Extension for Live Activities

The sample app adds a widget extension target to customize non-alerting presentations in the Dynamic Island, Lock Screen, and StandBy. The widget extension receives the same [`AlarmAttributes`](alarmattributes.md) structure that you provide to [`shared`](alarmmanager/shared.md) when scheduling alarms. It includes the metadata provided in the [`Configure the alarm’s UI attributes`](https://developer.apple.com#Configure-the-alarms-UI-attributes) section above.

> ❗ **Important**: AlarmKit expects a widget extension if an app supports a countdown presentation. Otherwise, the system may unexpectedly dismiss alarms and fail to alert. For more information, see [`ActivityKit`](https://developer.apple.com/documentation/ActivityKit).

## See Also

- [class AlarmManager](alarmmanager.md)
  An object that exposes functions to work with alarms: scheduling, snoozing, cancelling.
- [struct Alarm](alarm.md)
  An object that describes an alarm that can alert once or on a repeating schedule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/scheduling-an-alarm-with-alarmkit)*