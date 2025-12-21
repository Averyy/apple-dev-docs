# buttonBorderShape(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the border shape for buttons in this view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func buttonBorderShape(_ shape: ButtonBorderShape) -> some View
```

#### Discussion

The border shape is used to draw the platter for a bordered button.

The border shape affects buttons of the [`bordered`](primitivebuttonstyle/bordered.md) and [`borderedProminent`](primitivebuttonstyle/borderedprominent.md) styles.

> **Note**: In macOS 15 and earlier, some border shapes are only applicable to bordered buttons in widgets.

## Parameters

- `shape`: The shape to use.

## See Also

- [struct Button](button.md)
  A control that initiates an action.
- [func buttonStyle(_:)](view/buttonstyle(_:).md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
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
- [struct ButtonSizing](buttonsizing.md)
  The sizing behavior of `Button`s and other button-like controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/buttonbordershape(_:))*