# MenuStyle

**Framework**: SwiftUI  
**Kind**: protocol

A type that applies standard interaction behavior and a custom appearance to all menus within a view hierarchy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol MenuStyle
```

#### Overview

To configure the current menu style for a view hierarchy, use the [`menuStyle(_:)`](view/menustyle(_:).md) modifier.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Topics

### Getting built-in menu styles
- [static var automatic: DefaultMenuStyle](menustyle/automatic.md)
  The default menu style, based on the menu’s context.
- [static var button: ButtonMenuStyle](menustyle/button.md)
  A menu style that displays a button that toggles the display of the menu’s contents when pressed.
- [static var borderedButton: BorderedButtonMenuStyle](menustyle/borderedbutton.md)
  A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed.
- [static var borderlessButton: BorderlessButtonMenuStyle](menustyle/borderlessbutton.md)
  A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed.
### Creating custom menu styles
- [func makeBody(configuration: Self.Configuration) -> Self.Body](menustyle/makebody(configuration:).md)
  Creates a view that represents the body of a menu.
- [MenuStyle.Configuration](menustyle/configuration.md)
  The properties of a menu.
- [associatedtype Body : View](menustyle/body.md)
  A view that represents the body of a menu.
### Supporting types
- [struct DefaultMenuStyle](defaultmenustyle.md)
  The default menu style, based on the menu’s context.
- [struct ButtonMenuStyle](buttonmenustyle.md)
  A menu style that displays a button that toggles the display of the menu’s contents when pressed.
- [struct BorderlessButtonMenuStyle](borderlessbuttonmenustyle.md)
  A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed.
- [struct BorderedButtonMenuStyle](borderedbuttonmenustyle.md)
  A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed.

## Relationships

### Conforming Types
- [BorderedButtonMenuStyle](borderedbuttonmenustyle.md)
- [BorderlessButtonMenuStyle](borderlessbuttonmenustyle.md)
- [ButtonMenuStyle](buttonmenustyle.md)
- [DefaultMenuStyle](defaultmenustyle.md)

## See Also

- [func menuStyle<S>(S) -> some View](view/menustyle(_:).md)
  Sets the style for menus within this view.
- [struct MenuStyleConfiguration](menustyleconfiguration.md)
  A configuration of a menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menustyle)*