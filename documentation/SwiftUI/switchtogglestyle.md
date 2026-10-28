# SwitchToggleStyle

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A toggle style that displays a leading label and a trailing switch.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
struct SwitchToggleStyle
```

## Overview

Use the [`switch`](./togglestyle/switch.md) static variable to create this style:

```swift
Toggle("Enhance Sound", isOn: $isEnhanced)
    .toggleStyle(.switch)
```

## Topics

### Creating the toggle style
- [init()](./switchtogglestyle/init%28%29.md)
  Creates a switch toggle style.
- [init(tint: Color)](./switchtogglestyle/init%28tint%29.md)
  Creates a switch style with a tint color.
### Supporting types
- [func makeBody(configuration: SwitchToggleStyle.Configuration) -> some View](./switchtogglestyle/makebody%28configuration%29.md)
  Creates a view that represents the body of a toggle switch.

## Relationships

### Conforms To
- [ToggleStyle](./togglestyle.md)

## See Also

### Supporting types
- [struct DefaultToggleStyle](./defaulttogglestyle.md)
  The default toggle style.
- [struct ButtonToggleStyle](./buttontogglestyle.md)
  A toggle style that displays as a button with its label as the title.
- [struct CheckboxToggleStyle](./checkboxtogglestyle.md)
  A toggle style that displays a checkbox followed by its label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/switchtogglestyle)*