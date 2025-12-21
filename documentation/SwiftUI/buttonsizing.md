# ButtonSizing

**Framework**: SwiftUI  
**Kind**: struct

The sizing behavior of `Button`s and other button-like controls.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct ButtonSizing
```

## Topics

### Type Properties
- [static var automatic: ButtonSizing](buttonsizing/automatic.md)
  The default button sizing behavior appropriate for the button’s contextual placement and platform.
- [static var fitted: ButtonSizing](buttonsizing/fitted.md)
  Sizes a button along its primary axis to fit its inner content, compressing if necessary.
- [static var flexible: ButtonSizing](buttonsizing/flexible.md)
  Sizes a button flexibly along its primary axis, filling its available space by expanding or compressing beyond its ideal size.

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
- [struct ButtonRepeatBehavior](buttonrepeatbehavior.md)
  The options for controlling the repeatability of button actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/buttonsizing)*