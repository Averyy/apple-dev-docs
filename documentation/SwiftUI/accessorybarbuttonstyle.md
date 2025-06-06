# AccessoryBarButtonStyle

**Framework**: SwiftUI  
**Kind**: struct

A button style that you use for actions in an accessory toolbar that narrow the focus of a search or other operation.

**Availability**:
- macOS 14.0+

## Declaration

```swift
struct AccessoryBarButtonStyle
```

#### Overview

This is the default button style for views in accessory toolbars, which you create with [`init(id:)`](toolbaritemplacement/init(id:).md), and for searchable scopes. This style also affects other view types that you apply a button style to, like [`Toggle`](toggle.md), [`Picker`](picker.md), and [`Menu`](menu.md) instances.

Use [`accessoryBar`](primitivebuttonstyle/accessorybar.md) to construct this style.

## Topics

### Creating the button style
- [init()](accessorybarbuttonstyle/init.md)
  Creates an accessory toolbar style
### Supporting types
- [func makeBody(configuration: AccessoryBarButtonStyle.Configuration) -> some View](accessorybarbuttonstyle/makebody(configuration:).md)
  Creates a view that represents the body of a button.

## Relationships

### Conforms To
- [PrimitiveButtonStyle](primitivebuttonstyle.md)

## See Also

- [struct DefaultButtonStyle](defaultbuttonstyle.md)
  The default button style, based on the button’s context.
- [struct AccessoryBarActionButtonStyle](accessorybaractionbuttonstyle.md)
  A button style that you use for extra actions in an accessory toolbar.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessorybarbuttonstyle)*