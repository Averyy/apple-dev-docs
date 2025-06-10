# palette

**Framework**: SwiftUI  
**Kind**: property

A control group style that presents its content as a palette.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static var palette: PaletteControlGroupStyle { get }
```

#### Discussion

> **Note**: When used outside of menus, this style is rendered as a segmented control.

Use this style to render a multi-select or a stateless palette. The following example creates a control group that contains both type of shelves:

```swift
Menu {
    // A multi select palette
    ControlGroup {
        ForEach(ColorTags.allCases) { colorTag in
            Toggle(isOn: $selectedColorTags[colorTag]) {
                Label(colorTag.name, systemImage: "circle")
            }
            .tint(colorTag.color)
        }
    }
    .controlGroupStyle(.palette)
    .paletteSelectionEffect(.symbolVariant(.fill))

    // A momentary / stateless palette
    ControlGroup {
        ForEach(Emotes.allCases) { emote in
            Button {
                sendEmote(emote)
            } label: {
                Label(emote.name, systemImage: emote.systemImage)
            }
        }
    }
    .controlGroupStyle(.palette)
}
```

To apply this style to a control group, or to a view that contains control groups, use the [`controlGroupStyle(_:)`](view/controlgroupstyle(_:).md) modifier.

## See Also

- [static var automatic: AutomaticControlGroupStyle](controlgroupstyle/automatic.md)
  The default control group style.
- [static var compactMenu: CompactMenuControlGroupStyle](controlgroupstyle/compactmenu.md)
  A control group style that presents its content as a compact menu when the user presses the control, or as a submenu when nested within a larger menu.
- [static var menu: MenuControlGroupStyle](controlgroupstyle/menu.md)
  A control group style that presents its content as a menu when the user presses the control, or as a submenu when nested within a larger menu.
- [static var navigation: NavigationControlGroupStyle](controlgroupstyle/navigation.md)
  The navigation control group style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlgroupstyle/palette)*