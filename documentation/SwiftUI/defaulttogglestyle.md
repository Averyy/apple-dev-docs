# DefaultToggleStyle

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The default toggle style.

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
nonisolated
struct DefaultToggleStyle
```

## Overview

Use the [`automatic`](./togglestyle/automatic.md) static variable to create this style:

```swift
Toggle("Enhance Sound", isOn: $isEnhanced)
    .toggleStyle(.automatic)
```

## Topics

### Creating the toggle style
- [init()](./defaulttogglestyle/init%28%29.md)
  Creates a default toggle style.
### Supporting types
- [func makeBody(configuration: DefaultToggleStyle.Configuration) -> some View](./defaulttogglestyle/makebody%28configuration%29.md)
  Creates a view that represents the body of a toggle.

## Relationships

### Conforms To
- [ToggleStyle](./togglestyle.md)

## See Also

### Supporting types
- [struct ButtonToggleStyle](./buttontogglestyle.md)
  A toggle style that displays as a button with its label as the title.
- [struct CheckboxToggleStyle](./checkboxtogglestyle.md)
  A toggle style that displays a checkbox followed by its label.
- [struct SwitchToggleStyle](./switchtogglestyle.md)
  A toggle style that displays a leading label and a trailing switch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/defaulttogglestyle)*