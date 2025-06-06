# ControlGroupStyle

**Framework**: SwiftUI  
**Kind**: protocol

Defines the implementation of all control groups within a view hierarchy.

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
@preconcurrency protocol ControlGroupStyle
```

#### Overview

To configure the current `ControlGroupStyle` for a view hierarchy, use the [`controlGroupStyle(_:)`](view/controlgroupstyle(_:).md) modifier.

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

### Getting built-in control group styles
- [static var automatic: AutomaticControlGroupStyle](controlgroupstyle/automatic.md)
  The default control group style.
- [static var compactMenu: CompactMenuControlGroupStyle](controlgroupstyle/compactmenu.md)
  A control group style that presents its content as a compact menu when the user presses the control, or as a submenu when nested within a larger menu.
- [static var menu: MenuControlGroupStyle](controlgroupstyle/menu.md)
  A control group style that presents its content as a menu when the user presses the control, or as a submenu when nested within a larger menu.
- [static var navigation: NavigationControlGroupStyle](controlgroupstyle/navigation.md)
  The navigation control group style.
- [static var palette: PaletteControlGroupStyle](controlgroupstyle/palette.md)
  A control group style that presents its content as a palette.
### Creating custom control group styles
- [func makeBody(configuration: Self.Configuration) -> Self.Body](controlgroupstyle/makebody(configuration:).md)
  Creates a view representing the body of a control group.
- [ControlGroupStyle.Configuration](controlgroupstyle/configuration.md)
  The properties of a `ControlGroup` instance being created.
- [associatedtype Body : View](controlgroupstyle/body.md)
  A view representing the body of a control group.
### Supporting types
- [struct AutomaticControlGroupStyle](automaticcontrolgroupstyle.md)
  The default control group style.
- [struct CompactMenuControlGroupStyle](compactmenucontrolgroupstyle.md)
  A control group style that presents its content as a compact menu when the user presses the control, or as a submenu when nested within a larger menu.
- [struct MenuControlGroupStyle](menucontrolgroupstyle.md)
  A control group style that presents its content as a menu when the user presses the control, or as a submenu when nested within a larger menu.
- [struct NavigationControlGroupStyle](navigationcontrolgroupstyle.md)
  The navigation control group style.
- [struct PaletteControlGroupStyle](palettecontrolgroupstyle.md)
  A control group style that presents its content as a palette.

## Relationships

### Conforming Types
- [AutomaticControlGroupStyle](automaticcontrolgroupstyle.md)
- [CompactMenuControlGroupStyle](compactmenucontrolgroupstyle.md)
- [MenuControlGroupStyle](menucontrolgroupstyle.md)
- [NavigationControlGroupStyle](navigationcontrolgroupstyle.md)
- [PaletteControlGroupStyle](palettecontrolgroupstyle.md)

## See Also

- [func controlGroupStyle<S>(S) -> some View](view/controlgroupstyle(_:).md)
  Sets the style for control groups within this view.
- [struct ControlGroupStyleConfiguration](controlgroupstyleconfiguration.md)
  The properties of a control group.
- [func formStyle<S>(S) -> some View](view/formstyle(_:).md)
  Sets the style for forms in a view hierarchy.
- [protocol FormStyle](formstyle.md)
  The appearance and behavior of a form.
- [struct FormStyleConfiguration](formstyleconfiguration.md)
  The properties of a form instance.
- [func groupBoxStyle<S>(S) -> some View](view/groupboxstyle(_:).md)
  Sets the style for group boxes within this view.
- [protocol GroupBoxStyle](groupboxstyle.md)
  A type that specifies the appearance and interaction of all group boxes within a view hierarchy.
- [struct GroupBoxStyleConfiguration](groupboxstyleconfiguration.md)
  The properties of a group box instance.
- [func indexViewStyle<S>(S) -> some View](view/indexviewstyle(_:).md)
  Sets the style for the index view within the current environment.
- [protocol IndexViewStyle](indexviewstyle.md)
  Defines the implementation of all `IndexView` instances within a view hierarchy.
- [func labeledContentStyle<S>(S) -> some View](view/labeledcontentstyle(_:).md)
  Sets a style for labeled content.
- [protocol LabeledContentStyle](labeledcontentstyle.md)
  The appearance and behavior of a labeled content instance..
- [struct LabeledContentStyleConfiguration](labeledcontentstyleconfiguration.md)
  The properties of a labeled content instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlgroupstyle)*