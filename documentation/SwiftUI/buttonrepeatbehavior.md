# ButtonRepeatBehavior

**Framework**: SwiftUI  
**Kind**: struct

The options for controlling the repeatability of button actions.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct ButtonRepeatBehavior
```

#### Overview

Use values of this type with the [`buttonRepeatBehavior(_:)`](view/buttonrepeatbehavior(_:).md) modifier.

## Topics

### Getting repeat behaviors
- [static let automatic: ButtonRepeatBehavior](buttonrepeatbehavior/automatic.md)
  The automatic repeat behavior.
- [static let enabled: ButtonRepeatBehavior](buttonrepeatbehavior/enabled.md)
  Repeating button actions will be enabled.
- [static let disabled: ButtonRepeatBehavior](buttonrepeatbehavior/disabled.md)
  Repeating button actions will be disabled.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Button](button.md)
  A control that initiates an action.
- [func buttonStyle(_:)](view/buttonstyle(_:).md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [func buttonBorderShape(ButtonBorderShape) -> some View](view/buttonbordershape(_:).md)
  Sets the border shape for buttons in this view.
- [func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View](view/buttonrepeatbehavior(_:).md)
  Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.
- [var buttonRepeatBehavior: ButtonRepeatBehavior](environmentvalues/buttonrepeatbehavior.md)
  Whether buttons with this associated environment should repeatedly trigger their actions on prolonged interactions.
- [struct ButtonBorderShape](buttonbordershape.md)
  A shape used to draw a button’s border.
- [struct ButtonRole](buttonrole.md)
  A value that describes the purpose of a button.
- [struct ButtonSizing](buttonsizing.md)
  The sizing behavior of `Button`s and other button-like controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/buttonrepeatbehavior)*