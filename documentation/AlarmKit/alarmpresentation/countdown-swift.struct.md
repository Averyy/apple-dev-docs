# AlarmPresentation.Countdown

**Framework**: AlarmKit  
**Kind**: struct  
**Role**: Structure

An object that describes the content required for the countdown UI.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct Countdown
```

## Overview

The code snippet below describes how to configure a countdown UI with a pause and resume button.

```swift
let countdown = AlarmPresentation.Countdown(title: "Eggs are cooking")
let paused = AlarmPresentation.Paused(
    title: "Timer paused",
    resumeButton: AlarmButton(text: "Resume", textColor: .blue, systemImageName: "play.circle"))
```

## Topics

### Creates a pause button
- [init(title: LocalizedStringResource, pauseButton: AlarmButton?)](./countdown-swift.struct/init%28title,pausebutton%29.md)
  Creates a countdown with an optional pause button.
- [var pauseButton: AlarmButton?](./countdown-swift.struct/pausebutton.md)
  The pause button for a countdown timer.
- [var title: LocalizedStringResource](./countdown-swift.struct/title.md)
  The title of the countdown.

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
- [AlarmPresentation.Paused](./paused-swift.struct.md)
  An object that configures the UI for a paused timer state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentation/countdown-swift.struct)*