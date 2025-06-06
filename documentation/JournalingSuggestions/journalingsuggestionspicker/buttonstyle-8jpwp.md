# buttonStyle(_:)

**Framework**: Journaling Suggestions  
**Kind**: method

Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func buttonStyle<S>(_ style: S) -> some View where S : ButtonStyle
```

#### Discussion

Use this modifier to set a specific style for all button instances within a view:

```None
HStack {
    Button("Sign In", action: signIn)
    Button("Register", action: register)
}
.buttonStyle(.bordered)
```

You can also use this modifier to set the style for controls that acquire a button style through composition, like the `Menu` and `Toggle` views in the following example:

```None
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

The `View/menuStyle(_:)` modifier causes the Terms and Conditions menu to render as a button. Similarly, the `View/toggleStyle(_:)` modifier causes the two toggles to render as buttons. The button style modifier then causes not only the explicit Sign In `Button`, but also the menu and toggles with button styling, to render with the bordered button style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/buttonstyle(_:)-8jpwp)*