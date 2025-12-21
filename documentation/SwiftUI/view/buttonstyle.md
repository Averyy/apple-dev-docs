# buttonStyle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func buttonStyle<S>(_ style: S) -> some View where S : ButtonStyle
```

#### Discussion

Use this modifier to set a specific style for all button instances within a view:

```swift
HStack {
    Button("Sign In", action: signIn)
    Button("Register", action: register)
}
.buttonStyle(.bordered)
```

You can also use this modifier to set the style for controls that acquire a button style through composition, like the [`Menu`](menu.md) and [`Toggle`](toggle.md) views in the following example:

```swift
VStack {
    Menu("Terms and Conditions") {
        Button("Open in Preview", action: openInPreview)
        Button("Save as PDF", action: saveAsPDF)
    }
    Toggle("Remember Password", isOn: $isToggleOn)
    Toggle("Flag", isOn: $flagged)
    Button("Sign In", action: signIn)
}
.menuStyle(.button)
.toggleStyle(.button)
.buttonStyle(.bordered)
```

The [`menuStyle(_:)`](view/menustyle(_:).md) modifier causes the Terms and Conditions menu to render as a button. Similarly, the [`toggleStyle(_:)`](view/togglestyle(_:).md) modifier causes the two toggles to render as buttons. The button style modifier then causes not only the explicit Sign In [`Button`](button.md), but also the menu and toggles with button styling, to render with the bordered button style.

## See Also

- [struct Button](button.md)
  A control that initiates an action.
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
- [struct ButtonSizing](buttonsizing.md)
  The sizing behavior of `Button`s and other button-like controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/buttonstyle(_:))*