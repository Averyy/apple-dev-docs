# ButtonToggleStyle

**Framework**: SwiftUI  
**Kind**: struct

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
struct ButtonToggleStyle
```

#### Overview

You can also use [`button`](togglestyle/button.md) to construct this style.

```swift
Toggle(isOn: $isFlagged) {
    Label("Flag", systemImage: "flag.fill")
}
.toggleStyle(.button)
```

## Topics

### Creating the toggle style
- [init()](buttontogglestyle/init.md)
  Creates a button toggle style.
### Supporting types
- [func makeBody(configuration: ButtonToggleStyle.Configuration) -> some View](buttontogglestyle/makebody(configuration:).md)
  Creates a view that represents the body of a toggle button.

## Relationships

### Conforms To
- [ToggleStyle](togglestyle.md)

## See Also

- [struct DefaultToggleStyle](defaulttogglestyle.md)
  The default toggle style.
- [struct CheckboxToggleStyle](checkboxtogglestyle.md)
  A toggle style that displays a checkbox followed by its label.
- [struct SwitchToggleStyle](switchtogglestyle.md)
  A toggle style that displays a leading label and a trailing switch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/buttontogglestyle)*