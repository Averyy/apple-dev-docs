# buttonRepeatBehavior(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.

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
nonisolated
func buttonRepeatBehavior(_ behavior: ButtonRepeatBehavior) -> some View
```

#### Discussion

Apply this to buttons that increment or decrement a value or perform some other inherently iterative operation. Interactions such as pressing-and-holding on the button, holding the button’s keyboard shortcut, or holding down the space key while the button is focused will trigger this repeat behavior.

```swift
Button {
    playbackSpeed.advance(by: 1)
} label: {
    Label("Speed up", systemImage: "hare")
}
.buttonRepeatBehavior(.enabled)
```

This affects all system button styles, as well as automatically affects custom `ButtonStyle` conforming types. This does not automatically apply to custom `PrimitiveButtonStyle` conforming types, and the `EnvironmentValues.buttonRepeatBehavior` value should be used to adjust their custom gestures as appropriate.

## Parameters

- `behavior`: A value of   means that buttons should   enable repeating behavior and a value of   means that buttons   should disallow repeating behavior.

## See Also

- [struct Button](button.md)
  A control that initiates an action.
- [func buttonStyle(_:)](view/buttonstyle(_:).md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [func buttonBorderShape(ButtonBorderShape) -> some View](view/buttonbordershape(_:).md)
  Sets the border shape for buttons in this view.
- [var buttonRepeatBehavior: ButtonRepeatBehavior](environmentvalues/buttonrepeatbehavior.md)
  Whether buttons with this associated environment should repeatedly trigger their actions on prolonged interactions.
- [struct ButtonBorderShape](buttonbordershape.md)
  A shape used to draw a button’s border.
- [struct ButtonRole](buttonrole.md)
  A value that describes the purpose of a button.
- [struct ButtonRepeatBehavior](buttonrepeatbehavior.md)
  The options for controlling the repeatability of button actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/buttonrepeatbehavior(_:))*