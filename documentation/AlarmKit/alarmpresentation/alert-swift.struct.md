# AlarmPresentation.Alert

**Framework**: AlarmKit  
**Kind**: struct  
**Role**: Structure

An object that describes the UI of the alert that appears when an alarm fires.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct Alert
```

## Overview

`Alert` configures the title and buttons in the alarm UI. The system provides a stop button automatically. Use this object to optionally define a secondary button and its behavior. The code snippet below describes how to configure an `Alert` with a secondary button.

```swift
let alert = AlarmPresentation.Alert(title: "Eggs are ready!",
   secondaryButton: AlarmButton(text: "Repeat", textColor: .blue, systemImageName: "repeat"),
   secondaryButtonBehavior: .countdown)
```

## Topics

### Creating an alert
- [init(title: LocalizedStringResource, secondaryButton: AlarmButton?, secondaryButtonBehavior: AlarmPresentation.Alert.SecondaryButtonBehavior?)](./alert-swift.struct/init%28title,secondarybutton,secondarybuttonbehavior%29.md)
  Creates an alert for an alarm, with a system-provided stop control and optionally a second button.
- [var title: LocalizedStringResource](./alert-swift.struct/title.md)
  The title of the alert.
### Creating a second button
- [var secondaryButton: AlarmButton?](./alert-swift.struct/secondarybutton.md)
  The appearance of the secondary button.
- [var secondaryButtonBehavior: AlarmPresentation.Alert.SecondaryButtonBehavior?](./alert-swift.struct/secondarybuttonbehavior-swift.property.md)
  The defined behavior of the second button.
- [AlarmPresentation.Alert.SecondaryButtonBehavior](./alert-swift.struct/secondarybuttonbehavior-swift.enum.md)
  Describes the behaviour of the second button.
### Deprecated
- [init(title: LocalizedStringResource, stopButton: AlarmButton, secondaryButton: AlarmButton?, secondaryButtonBehavior: AlarmPresentation.Alert.SecondaryButtonBehavior?)](./alert-swift.struct/init%28title,stopbutton,secondarybutton,secondarybuttonbehavior%29.md)
  Creates an alert for an alarm.
- [var stopButton: AlarmButton](./alert-swift.struct/stopbutton.md)
  The appearance of the stop button.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Describing an alarm state
- [AlarmPresentation.Countdown](./countdown-swift.struct.md)
  An object that describes the content required for the countdown UI.
- [AlarmPresentation.Paused](./paused-swift.struct.md)
  An object that configures the UI for a paused timer state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentation/alert-swift.struct)*