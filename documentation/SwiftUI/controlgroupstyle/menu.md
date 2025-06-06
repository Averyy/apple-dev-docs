# menu

**Framework**: SwiftUI  
**Kind**: property

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
@MainActor
@preconcurrency static var menu: MenuControlGroupStyle { get }
```

#### Discussion

To apply this style to a control group, or to a view that contains control groups, use the [`controlGroupStyle(_:)`](view/controlgroupstyle(_:).md) modifier.

## See Also

- [static var automatic: AutomaticControlGroupStyle](controlgroupstyle/automatic.md)
  The default control group style.
- [static var compactMenu: CompactMenuControlGroupStyle](controlgroupstyle/compactmenu.md)
  A control group style that presents its content as a compact menu when the user presses the control, or as a submenu when nested within a larger menu.
- [static var navigation: NavigationControlGroupStyle](controlgroupstyle/navigation.md)
  The navigation control group style.
- [static var palette: PaletteControlGroupStyle](controlgroupstyle/palette.md)
  A control group style that presents its content as a palette.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlgroupstyle/menu)*