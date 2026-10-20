# menu

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A control group style that presents its content as a menu when the user presses the control, or as a submenu when nested within a larger menu.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated static var menu: MenuControlGroupStyle { get }
```

Available when `Self` is `MenuControlGroupStyle`.

#### Discussion

To apply this style to a control group, or to a view that contains control groups, use the [`controlGroupStyle(_:)`](../view/controlgroupstyle%28_%29.md) modifier.

## See Also

### Getting built-in control group styles
- [static var automatic: AutomaticControlGroupStyle](./automatic.md)
  The default control group style.
- [static var compactMenu: CompactMenuControlGroupStyle](./compactmenu.md)
  A control group style that presents its content as a compact menu when the user presses the control, or as a submenu when nested within a larger menu.
- [static var navigation: NavigationControlGroupStyle](./navigation.md)
  The navigation control group style.
- [static var palette: PaletteControlGroupStyle](./palette.md)
  A control group style that presents its content as a palette.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlgroupstyle/menu)*