# AccessoryBarActionButtonStyle

**Framework**: SwiftUI  
**Kind**: struct

A button style that you use for extra actions in an accessory toolbar.

**Availability**:
- macOS 14.0+

## Declaration

```swift
struct AccessoryBarActionButtonStyle
```

#### Overview

Use this style for buttons that perform extra actions relative to the accessory toolbar’s main functions, like adding or editing filters. This style also affects other view types that you apply a button style to, like [`Toggle`](toggle.md), [`Picker`](picker.md), and [`Menu`](menu.md) instances.

Use [`accessoryBarAction`](primitivebuttonstyle/accessorybaraction.md) to construct this style.

## Topics

### Creating the button style
- [init()](accessorybaractionbuttonstyle/init.md)
  Creates an accessory toolbar action button style
### Supporting types
- [func makeBody(configuration: AccessoryBarActionButtonStyle.Configuration) -> some View](accessorybaractionbuttonstyle/makebody(configuration:).md)
  Creates a view that represents the body of a button.

## Relationships

### Conforms To
- [PrimitiveButtonStyle](primitivebuttonstyle.md)

## See Also

- [struct DefaultButtonStyle](defaultbuttonstyle.md)
  The default button style, based on the button’s context.
- [struct AccessoryBarButtonStyle](accessorybarbuttonstyle.md)
  A button style that you use for actions in an accessory toolbar that narrow the focus of a search or other operation.
- [struct BorderedButtonStyle](borderedbuttonstyle.md)
  A button style that applies standard border artwork based on the button’s context.
- [struct BorderedProminentButtonStyle](borderedprominentbuttonstyle.md)
  A button style that applies standard border prominent artwork based on the button’s context.
- [struct BorderlessButtonStyle](borderlessbuttonstyle.md)
  A button style that doesn’t apply a border.
- [struct CardButtonStyle](cardbuttonstyle.md)
  A button style that doesn’t pad the content, and applies a motion effect when a button has focus.
- [struct LinkButtonStyle](linkbuttonstyle.md)
  A button style for buttons that emulate links.
- [struct PlainButtonStyle](plainbuttonstyle.md)
  A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessorybaractionbuttonstyle)*