# accessoryBarAction

**Framework**: SwiftUI  
**Kind**: property

A button style that you use for extra actions in an accessory toolbar.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency static var accessoryBarAction: AccessoryBarActionButtonStyle { get }
```

#### Discussion

Use this style for buttons that perform extra actions relative to the accessory toolbar’s main functions, like adding or editing filters. This style also affects other view types that you apply a button style to, like [`Toggle`](toggle.md), [`Picker`](picker.md), and [`Menu`](menu.md) instances.

## See Also

- [static var automatic: DefaultButtonStyle](primitivebuttonstyle/automatic.md)
  The default button style, based on the button’s context.
- [static var accessoryBar: AccessoryBarButtonStyle](primitivebuttonstyle/accessorybar.md)
  A button style that is typically used in the context of an accessory toolbar (sometimes refererred to as a “scope bar”), for buttons that narrow the focus of a search or other operation.
- [static var bordered: BorderedButtonStyle](primitivebuttonstyle/bordered.md)
  A button style that applies the standard border style based on the button’s context.
- [static var borderedProminent: BorderedProminentButtonStyle](primitivebuttonstyle/borderedprominent.md)
  A button style that applies the standard bordered prominent style based on the button’s context.
- [static var borderless: BorderlessButtonStyle](primitivebuttonstyle/borderless.md)
  A button style that doesn’t apply a border.
- [static var card: CardButtonStyle](primitivebuttonstyle/card.md)
  A button style that doesn’t pad the content, and applies a Liquid Glass effect when the button has focus.
- [static var glass: GlassButtonStyle](primitivebuttonstyle/glass.md)
  A button style that applies a Liquid Glass effect based on the button’s context.
- [static var glassProminent: GlassProminentButtonStyle](primitivebuttonstyle/glassprominent.md)
  A button style that applies a prominent Liquid Glass effect based on the button’s context.
- [static func glass(Glass) -> Self](primitivebuttonstyle/glass(_:).md)
  A button style that applies a configurable Liquid Glass effect based on the button’s context.
- [static var link: LinkButtonStyle](primitivebuttonstyle/link.md)
  A button style for buttons that emulate links.
- [static var plain: PlainButtonStyle](primitivebuttonstyle/plain.md)
  A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/primitivebuttonstyle/accessorybaraction)*