# PlainButtonStyle

**Framework**: SwiftUI  
**Kind**: struct

A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.

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
struct PlainButtonStyle
```

#### Overview

You can also use [`plain`](primitivebuttonstyle/plain.md) to construct this style.

## Topics

### Creating the button style
- [init()](plainbuttonstyle/init.md)
  Creates a plain button style.
### Supporting types
- [func makeBody(configuration: PlainButtonStyle.Configuration) -> some View](plainbuttonstyle/makebody(configuration:).md)
  Creates a view that represents the body of a button.

## Relationships

### Conforms To
- [PrimitiveButtonStyle](primitivebuttonstyle.md)

## See Also

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
- [struct CardButtonStyle](cardbuttonstyle.md)
  A button style that doesn’t pad the content, and applies a motion effect when a button has focus.
- [struct LinkButtonStyle](linkbuttonstyle.md)
  A button style for buttons that emulate links.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/plainbuttonstyle)*