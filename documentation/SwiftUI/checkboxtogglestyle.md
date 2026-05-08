# CheckboxToggleStyle

**Framework**: SwiftUI  
**Kind**: struct

A toggle style that displays a checkbox followed by its label.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct CheckboxToggleStyle
```

#### Overview

Use the [`checkbox`](togglestyle/checkbox.md) static variable to create this style:

```swift
Toggle("Close windows when quitting an app", isOn: $doesClose)
    .toggleStyle(.checkbox)
```

## Topics

### Creating the toggle style
- [init()](checkboxtogglestyle/init.md)
  Creates a checkbox toggle style.
### Supporting types
- [func makeBody(configuration: CheckboxToggleStyle.Configuration) -> some View](checkboxtogglestyle/makebody(configuration:).md)
  Creates a view that represents the body of a toggle checkbox.

## Relationships

### Conforms To
- [ToggleStyle](togglestyle.md)

## See Also

- [struct DefaultToggleStyle](defaulttogglestyle.md)
  The default toggle style.
- [struct ButtonToggleStyle](buttontogglestyle.md)
  A toggle style that displays as a button with its label as the title.
- [struct SwitchToggleStyle](switchtogglestyle.md)
  A toggle style that displays a leading label and a trailing switch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/checkboxtogglestyle)*