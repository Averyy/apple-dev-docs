# AlarmPresentation.Paused

**Framework**: AlarmKit  
**Kind**: struct  
**Role**: Structure

An object that configures the UI for a paused timer state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct Paused
```

#### Overview

This is only applicable to timers that can be paused. To get back to a countdown state, you must provide a definition for a resume button. The following code snippet describes how to schedule a timer that can pause and resume.

```swift
let paused = AlarmPresentation.Paused(
    title: "Timer paused",
    resumeButton: AlarmButton(text: "Resume", textColor: .blue, systemImageName: "play.circle"))
```

## Topics

### Creating a resume button
- [init(title: LocalizedStringResource, resumeButton: AlarmButton)](./paused-swift.struct/init%28title,resumebutton%29.md)
  Creates a pause presentation with a resume button.
- [var resumeButton: AlarmButton](./paused-swift.struct/resumebutton.md)
  The appearance of the resume button.
- [var title: LocalizedStringResource](./paused-swift.struct/title.md)
  The title of the paused UI.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Describing an alarm state
- [AlarmPresentation.Alert](./alert-swift.struct.md)
  An object that describes the UI of the alert that appears when an alarm fires.
- [AlarmPresentation.Countdown](./countdown-swift.struct.md)
  An object that describes the content required for the countdown UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentation/paused-swift.struct)*