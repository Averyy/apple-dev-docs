# AlarmPresentation

**Framework**: AlarmKit  
**Kind**: struct

An object that describes the content required for the alarm UI.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
struct AlarmPresentation
```

#### Overview

The following example shows how to set different views for an alarm using the `AlarmPresentation` model.

```swift
let alert = AlarmPresentation.Alert(title: "Eggs are ready!",
stopButton: AlarmButton(text: "Stop", textColor: .blue, systemImageName: "stop.circle"),
secondaryButton: AlarmButton(text: "Repeat", textColor: .blue, systemImageName: "repeat"),
secondaryButtonBehavior: .countdown)

let countdown = AlarmPresentation.Countdown(title: "Eggs are cooking")

let paused = AlarmPresentation.Paused(title: "Timer paused",
resumeButton: AlarmButton(text: "Resume", textColor: .blue, systemImageName:"play.circle"))

let presentation = AlarmPresentation(alert: alert, countdown: countdown, paused: paused)

```

## Topics

### Defining the alarm UI
- [init(alert: AlarmPresentation.Alert, countdown: AlarmPresentation.Countdown?, paused: AlarmPresentation.Paused?)](alarmpresentation/init(alert:countdown:paused:).md)
  Configures an alert with an optional countdown and paused state.
- [var alert: AlarmPresentation.Alert](alarmpresentation/alert-swift.property.md)
  The content for the alert mode of the alarm.
- [var countdown: AlarmPresentation.Countdown?](alarmpresentation/countdown-swift.property.md)
  The content for the snooze or countdown mode of the alarm.
- [var paused: AlarmPresentation.Paused?](alarmpresentation/paused-swift.property.md)
  The content for the pause mode of the alarm.
### Describing an alarm state
- [AlarmPresentation.Alert](alarmpresentation/alert-swift.struct.md)
  An object that describes the UI of the alert that appears when an alarm fires.
- [AlarmPresentation.Countdown](alarmpresentation/countdown-swift.struct.md)
  An object that describes the content required for the countdown UI.
- [AlarmPresentation.Paused](alarmpresentation/paused-swift.struct.md)
  An object that describes the content required for the paused UI.
### Decoding
- [init(from: any Decoder) throws](alarmpresentation/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](alarmpresentation/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AlarmPresentationState](alarmpresentationstate.md)
  An object that describes the mutable content of the alarm.
- [struct AlarmAttributes](alarmattributes.md)
  An object that contains all information necessary for the alarm UI.
- [protocol AlarmMetadata](alarmmetadata.md)
  A metadata object that contains information about an alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentation)*