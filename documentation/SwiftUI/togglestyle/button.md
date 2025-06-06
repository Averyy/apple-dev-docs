# button

**Framework**: SwiftUI  
**Kind**: property

A toggle style that displays as a button with its label as the title.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency static var button: ButtonToggleStyle { get }
```

#### Discussion

Apply this style to a [`Toggle`](toggle.md) or to a view hierarchy that contains toggles using the [`toggleStyle(_:)`](view/togglestyle(_:).md) modifier:

```swift
Toggle(isOn: $isFlagged) {
    Label("Flag", systemImage: "flag.fill")
}
.toggleStyle(.button)
```

The style produces a button with a label that describes the purpose of the toggle. The user taps or clicks the button to change the toggle’s state. The button indicates the `on` state by filling in the background with its tint color. You can change the tint color using the [`tint(_:)`](view/tint(_:).md) modifier. SwiftUI uses this style as the default for toggles that appear in a toolbar.

The following table shows the toggle in both the `off` and `on` states, respectively:

| Platform | Appearance |
| --- | --- |
| iOS, iPadOS | ![A screenshot of two buttons with a flag icon and the word flag inside. The first button isn’t highlighted; the second one is.](https://docs-assets.developer.apple.com/published/29a2510c1ef1b33fa8b54c034916a1b8/ToggleStyle-button-1-iOS%402x.png) |
| macOS | ![A screenshot of two buttons with a flag icon and the word flag inside. The first button isn’t highlighted; the second one is.](https://docs-assets.developer.apple.com/published/7542554967f1ced9f6ae2d2808a60c84/ToggleStyle-button-1-macOS%402x.png) |

A [`Label`](label.md) instance is a good choice for a button toggle’s label. Based on the context, SwiftUI decides whether to display both the title and icon, as in the example above, or just the icon, like when the toggle appears in a toolbar. You can also control the label’s style by adding a [`labelStyle(_:)`](view/labelstyle(_:).md) modifier. In any case, SwiftUI always uses the title to identify the control using VoiceOver.

## See Also

- [static var automatic: DefaultToggleStyle](togglestyle/automatic.md)
  The default toggle style.
- [static var checkbox: CheckboxToggleStyle](togglestyle/checkbox.md)
  A toggle style that displays a checkbox followed by its label.
- [static var `switch`: SwitchToggleStyle](togglestyle/switch.md)
  A toggle style that displays a leading label and a trailing switch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/togglestyle/button)*