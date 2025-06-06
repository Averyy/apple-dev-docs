# MenuStyleConfiguration

**Framework**: SwiftUI  
**Kind**: struct

A configuration of a menu.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct MenuStyleConfiguration
```

#### Overview

Use the [`init(_:)`](menu/init(_:).md) initializer of [`Menu`](menu.md) to create an instance using the current menu style, which you can modify to create a custom style.

For example, the following code creates a new, custom style that adds a red border to the current menu style:

```swift
struct RedBorderMenuStyle: MenuStyle {
    func makeBody(configuration: Configuration) -> some View {
        Menu(configuration)
            .border(Color.red)
    }
}
```

## Topics

### Setting the label and content
- [MenuStyleConfiguration.Label](menustyleconfiguration/label.md)
  A type-erased label of a menu.
- [MenuStyleConfiguration.Content](menustyleconfiguration/content.md)
  A type-erased content of a menu.

## See Also

- [func menuStyle<S>(S) -> some View](view/menustyle(_:).md)
  Sets the style for menus within this view.
- [protocol MenuStyle](menustyle.md)
  A type that applies standard interaction behavior and a custom appearance to all menus within a view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menustyleconfiguration)*