# accessoryBar

**Framework**: SwiftUI  
**Kind**: property

A button style that is typically used in the context of an accessory toolbar (sometimes refererred to as a “scope bar”), for buttons that narrow the focus of a search or other operation.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency static var accessoryBar: AccessoryBarButtonStyle { get }
```

#### Discussion

This is the default button style for views in accessory toolbars, created with `ToolbarItemPlacement.init(id:_)`, and for searchable scopes.

This style will also affect button style `Toggle`s, as well as button style `Picker`s and `Menu`s.

```swift
HStack(alignment: .firstTextBaseline) {
    Button("Button") {}

    Toggle("Toggle", isOn: $isToggleOn)
        .toggleStyle(.button)

    Picker("Picker", selection: $selection) {
        Text("Option 1").tag(0)
        Text("Option 2").tag(1)
    }

    Picker("Inline Picker", selection: $selection) {
        Text("Option 1").tag(0)
        Text("Option 2").tag(1)
    }
    .pickerStyle(.inline)

    Menu("Menu") {
        Button("Item") {}
    }
}
.buttonStyle(.accessoryBar)
```

## See Also

- [static var automatic: DefaultButtonStyle](primitivebuttonstyle/automatic.md)
  The default button style, based on the button’s context.
- [static var accessoryBarAction: AccessoryBarActionButtonStyle](primitivebuttonstyle/accessorybaraction.md)
  A button style that you use for extra actions in an accessory toolbar.
- [static var bordered: BorderedButtonStyle](primitivebuttonstyle/bordered.md)
  A button style that applies standard border artwork based on the button’s context.
- [static var borderedProminent: BorderedProminentButtonStyle](primitivebuttonstyle/borderedprominent.md)
  A button style that applies standard border prominent artwork based on the button’s context.
- [static var borderless: BorderlessButtonStyle](primitivebuttonstyle/borderless.md)
  A button style that doesn’t apply a border.
- [static var card: CardButtonStyle](primitivebuttonstyle/card.md)
  A button style that doesn’t pad the content, and applies a motion effect when a button has focus.
- [static var link: LinkButtonStyle](primitivebuttonstyle/link.md)
  A button style for buttons that emulate links.
- [static var plain: PlainButtonStyle](primitivebuttonstyle/plain.md)
  A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/primitivebuttonstyle/accessorybar)*