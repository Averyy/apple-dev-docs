# AlarmPresentation.Alert

**Framework**: AlarmKit  
**Kind**: struct

An object that describes the UI of the alert that appears when an alarm fires.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct Alert
```

#### Overview

`Alert` configures the title and buttons in the alarm UI. Use this object to define your alarm button behaviors. The code snippet below describes how to configure an `Alert` button.

```swift
let alert = AlarmPresentation.Alert(title: "Eggs are ready!",
   stopButton: AlarmButton(text: "Stop", textColor: .blue, systemImageName: "stop.circle"),
secondaryButton: AlarmButton(text: "Repeat", textColor: .blue, systemImageName: "repeat"),
secondaryButtonBehavior: .countdown)
```

## Topics

### Creating a button
- [init(title: LocalizedStringResource, stopButton: AlarmButton, secondaryButton: AlarmButton?, secondaryButtonBehavior: AlarmPresentation.Alert.SecondaryButtonBehavior?)](alarmpresentation/alert-swift.struct/init(title:stopbutton:secondarybutton:secondarybuttonbehavior:).md)
  Creates an alert for an alarm.
- [var stopButton: AlarmButton](alarmpresentation/alert-swift.struct/stopbutton.md)
  The appearance of the stop button.
- [var title: LocalizedStringResource](alarmpresentation/alert-swift.struct/title.md)
  The title of the alert.
### Creating a second button
- [var secondaryButton: AlarmButton?](alarmpresentation/alert-swift.struct/secondarybutton.md)
  The appearance of the secondary button.
- [var secondaryButtonBehavior: AlarmPresentation.Alert.SecondaryButtonBehavior?](alarmpresentation/alert-swift.struct/secondarybuttonbehavior-swift.property.md)
  The behavior of the second button.
- [AlarmPresentation.Alert.SecondaryButtonBehavior](alarmpresentation/alert-swift.struct/secondarybuttonbehavior-swift.enum.md)
  Describes the behaviour of the second button.
### Initializers
- [init(title: LocalizedStringResource, secondaryButton: AlarmButton?, secondaryButtonBehavior: AlarmPresentation.Alert.SecondaryButtonBehavior?)](alarmpresentation/alert-swift.struct/init(title:secondarybutton:secondarybuttonbehavior:).md)
  Creates an alert for an alarm, with a system-provided stop control and optionally a second button.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [AlarmPresentation.Countdown](alarmpresentation/countdown-swift.struct.md)
  An object that describes the content required for the countdown UI.
- [AlarmPresentation.Paused](alarmpresentation/paused-swift.struct.md)
  An object that describes the content required for the paused UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentation/alert-swift.struct)*