# AlarmButton

**Framework**: AlarmKit  
**Kind**: struct

A structure that defines the appearance of buttons.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
struct AlarmButton
```

#### Overview

The folllowing example uses `AlarmButton` to define the appearance of the alarm.

```swift
let alert = AlarmPresentation.Alert(title: "Eggs are ready!",
stopButton: AlarmButton
(text: "Stop", textColor: .blue, systemImageName: "stop.circle"),
secondaryButton: AlarmButton
(text: "Repeat", textColor: .blue, systemImageName: "repeat"),
secondaryButtonBehavior: .countdown)
```

## Topics

### Creating a button
- [init(text: LocalizedStringResource, textColor: Color, systemImageName: String)](alarmbutton/init(text:textcolor:systemimagename:).md)
  Creates an alarm button.
- [var systemImageName: String](alarmbutton/systemimagename.md)
  The name of the icon you use on the button.
- [var textColor: Color](alarmbutton/textcolor.md)
  The color for the text on the button.
- [var text: LocalizedStringResource](alarmbutton/text.md)
  Text to show in a label on the button.
### Encoding and decoding
- [func encode(to: any Encoder) throws](alarmbutton/encode(to:).md)
  Performs encoding to a given encoder.
- [init(from: any Decoder) throws](alarmbutton/init(from:).md)
  Creates an alarm button from a decoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmbutton)*