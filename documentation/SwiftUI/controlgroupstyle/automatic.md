# automatic

**Framework**: SwiftUI  
**Kind**: property

The default control group style.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static var automatic: AutomaticControlGroupStyle { get }
```

#### Discussion

The default control group style can vary by platform. By default, both platforms use a momentary segmented control style that’s appropriate for the environment in which it is rendered.

You can override a control group’s style. To apply the default style to a control group or to a view that contains a control group, use the [`controlGroupStyle(_:)`](view/controlgroupstyle(_:).md) modifier.

## See Also

- [static var compactMenu: CompactMenuControlGroupStyle](controlgroupstyle/compactmenu.md)
  A control group style that presents its content as a compact menu when the user presses the control, or as a submenu when nested within a larger menu.
- [static var menu: MenuControlGroupStyle](controlgroupstyle/menu.md)
  A control group style that presents its content as a menu when the user presses the control, or as a submenu when nested within a larger menu.
- [static var navigation: NavigationControlGroupStyle](controlgroupstyle/navigation.md)
  The navigation control group style.
- [static var palette: PaletteControlGroupStyle](controlgroupstyle/palette.md)
  A control group style that presents its content as a palette.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlgroupstyle/automatic)*