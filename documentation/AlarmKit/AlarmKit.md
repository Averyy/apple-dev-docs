# AlarmKit

**Framework**: AlarmKit  
**Kind**: module

Schedule prominent alarms and countdowns to help people manage their time.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

#### Overview

Use `AlarmKit` to create custom alarms and timers in your app. `AlarmKit` provides a framework for managing alarms with customizable schedules and UI. It supports one-time and repeating alarms, with the option for countdown durations and snooze functionality. `AlarmKit` handles alarm authorization and provides UI for both templated and widget presentations. It supports traditional alarms, timers, or both, and provides methods to schedule, pause, resume, and cancel alarms.

## Topics

### Alarm management
- [Scheduling an alarm with AlarmKit](scheduling-an-alarm-with-alarmkit.md)
  Create prominent alerts at specified dates for your iOS app.
- [class AlarmManager](alarmmanager.md)
  An object that exposes functions to work with alarms: scheduling, snoozing, cancelling.
- [struct Alarm](alarm.md)
  An object that describes an alarm that can alert once or on a repeating schedule.
### Buttons
- [struct AlarmButton](alarmbutton.md)
  A structure that defines the appearance of buttons.
### Views
- [struct AlarmPresentation](alarmpresentation.md)
  An object that describes the content required for the alarm UI.
- [struct AlarmPresentationState](alarmpresentationstate.md)
  An object that describes the mutable content of the alarm.
- [struct AlarmAttributes](alarmattributes.md)
  An object that contains all information necessary for the alarm UI.
- [protocol AlarmMetadata](alarmmetadata.md)
  A metadata object that contains information about an alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AlarmKit)*