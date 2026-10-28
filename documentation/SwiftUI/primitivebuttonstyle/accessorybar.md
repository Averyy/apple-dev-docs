# accessoryBar

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A button style that is typically used in the context of an accessory toolbar (sometimes refererred to as a “scope bar”), for buttons that narrow the focus of a search or other operation.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency static var accessoryBar: AccessoryBarButtonStyle { get }
```

Available when `Self` is `AccessoryBarButtonStyle`.

## Discussion

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

### Getting built-in button styles
- [static var automatic: DefaultButtonStyle](./automatic.md)
  The default button style, based on the button’s context.
- [static var accessoryBarAction: AccessoryBarActionButtonStyle](./accessorybaraction.md)
  A button style that you use for extra actions in an accessory toolbar.
- [static var bordered: BorderedButtonStyle](./bordered.md)
  A button style that applies the standard border style based on the button’s context.
- [static var borderedProminent: BorderedProminentButtonStyle](./borderedprominent.md)
  A button style that applies the standard bordered prominent style based on the button’s context.
- [static var borderless: BorderlessButtonStyle](./borderless.md)
  A button style that doesn’t apply a border.
- [static var card: CardButtonStyle](./card.md)
  A button style that doesn’t pad the content, and applies a Liquid Glass effect when the button has focus.
- [static var glass: GlassButtonStyle](./glass.md)
  A button style that applies a Liquid Glass effect based on the button’s context.
- [static var glassProminent: GlassProminentButtonStyle](./glassprominent.md)
  A button style that applies a prominent Liquid Glass effect based on the button’s context.
- [static func glass(Glass) -> Self](./glass%28_%29.md)
  A button style that applies a configurable Liquid Glass effect based on the button’s context.
- [static var link: LinkButtonStyle](./link.md)
  A button style for buttons that emulate links.
- [static var plain: PlainButtonStyle](./plain.md)
  A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/primitivebuttonstyle/accessorybar)*