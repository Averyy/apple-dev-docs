# BorderlessButtonMenuStyle

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- tvOS 17.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`menuStyle(_:)`](./view/menustyle%28_%29.md) with [`button`](./menustyle/button.md) and [`buttonStyle(_:)`](./view/buttonstyle%28_%29-66fbx.md) with [`borderless`](./primitivebuttonstyle/borderless.md).

## Declaration

```swift
nonisolated
struct BorderlessButtonMenuStyle
```

## Overview

Use [`borderlessButton`](./menustyle/borderlessbutton.md) to construct this style.

## Topics

### Creating a bordeless button menu style
- [init()](./borderlessbuttonmenustyle/init%28%29.md)
  Creates a borderless button menu style.
- [init(showsMenuIndicator: Bool)](./borderlessbuttonmenustyle/init%28showsmenuindicator%29.md)
  Creates a borderless button menu style, specifying whether to show a visual menu indicator.

## Relationships

### Conforms To
- [MenuStyle](./menustyle.md)

## See Also

### Deprecated
- [static var borderedButton: BorderedButtonMenuStyle](./menustyle/borderedbutton.md)
  A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed.
- [static var borderlessButton: BorderlessButtonMenuStyle](./menustyle/borderlessbutton.md)
  A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed.
- [struct BorderedButtonMenuStyle](./borderedbuttonmenustyle.md)
  A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/borderlessbuttonmenustyle)*