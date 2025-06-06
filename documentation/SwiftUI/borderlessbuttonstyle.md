# BorderlessButtonStyle

**Framework**: SwiftUI  
**Kind**: struct

A button style that doesn’t apply a border.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct BorderlessButtonStyle
```

#### Overview

You can also use [`borderless`](primitivebuttonstyle/borderless.md) to construct this style.

## Topics

### Creating the button style
- [init()](borderlessbuttonstyle/init.md)
  Creates a borderless button style.
### Supporting types
- [func makeBody(configuration: BorderlessButtonStyle.Configuration) -> some View](borderlessbuttonstyle/makebody(configuration:).md)
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
- [struct CardButtonStyle](cardbuttonstyle.md)
  A button style that doesn’t pad the content, and applies a motion effect when a button has focus.
- [struct LinkButtonStyle](linkbuttonstyle.md)
  A button style for buttons that emulate links.
- [struct PlainButtonStyle](plainbuttonstyle.md)
  A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/borderlessbuttonstyle)*