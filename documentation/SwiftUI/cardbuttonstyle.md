# CardButtonStyle

**Framework**: SwiftUI  
**Kind**: struct

A button style that doesn’t pad the content, and applies a motion effect when a button has focus.

**Availability**:
- tvOS 14.0+

## Declaration

```swift
struct CardButtonStyle
```

#### Overview

You can also use [`card`](primitivebuttonstyle/card.md) to construct this style.

## Topics

### Creating the button style
- [init()](cardbuttonstyle/init.md)
  Creates a style that doesn’t pad a button’s content and applies a motion effect to a focused button.
### Supporting types
- [func makeBody(configuration: CardButtonStyle.Configuration) -> some View](cardbuttonstyle/makebody(configuration:).md)
  Creates a view that represents the body of a button.

## Relationships

### Conforms To
- [PrimitiveButtonStyle](primitivebuttonstyle.md)

## See Also

- [class TVCardView](../TVUIKit/TVCardView.md)
  A view that responds to focus interaction with a motion effect it applies to all of its subviews.
- [struct DefaultButtonStyle](defaultbuttonstyle.md)
  The default button style, based on the button’s context.
- [struct AccessoryBarButtonStyle](accessorybarbuttonstyle.md)
  A button style that you use for actions in an accessory toolbar that narrow the focus of a search or other operation.
- [struct AccessoryBarActionButtonStyle](accessorybaractionbuttonstyle.md)
  A button style that you use for extra actions in an accessory toolbar.
- [struct BorderedButtonStyle](borderedbuttonstyle.md)
  A button style that applies standard border artwork based on the button’s context.
- [struct BorderedProminentButtonStyle](borderedprominentbuttonstyle.md)
  A button style that applies standard border prominent artwork based on the button’s context.
- [struct BorderlessButtonStyle](borderlessbuttonstyle.md)
  A button style that doesn’t apply a border.
- [struct LinkButtonStyle](linkbuttonstyle.md)
  A button style for buttons that emulate links.
- [struct PlainButtonStyle](plainbuttonstyle.md)
  A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/cardbuttonstyle)*