# runSystemShortcut

**Framework**: SwiftUI  
**Kind**: property

An action that runs a system shortcut.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+
- visionOS 26.2+

## Declaration

```swift
static let runSystemShortcut: PencilPreferredAction
```

#### Discussion

If the user selects this as their preferred action to perform after double-tapping or squeezing their Apple Pencil, your app will never be notified when they do. Instead, you should only use this information to remind the user about their preference in your app’s UI.

## See Also

- [static let ignore: PencilPreferredAction](pencilpreferredaction/ignore.md)
  An action that does nothing.
- [static let showColorPalette: PencilPreferredAction](pencilpreferredaction/showcolorpalette.md)
  An action that toggles the display of the color palette.
- [static let showContextualPalette: PencilPreferredAction](pencilpreferredaction/showcontextualpalette.md)
  An action that toggles the display of the contextual palette, or the undo/redo panel if contextual palette is not available.
- [static let showInkAttributes: PencilPreferredAction](pencilpreferredaction/showinkattributes.md)
  An action that toggles the display of the current tool’s ink attributes.
- [static let switchEraser: PencilPreferredAction](pencilpreferredaction/switcheraser.md)
  An action that switches between the current tool and the eraser.
- [static let switchPrevious: PencilPreferredAction](pencilpreferredaction/switchprevious.md)
  An action that switches between the current tool and the last used tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pencilpreferredaction/runsystemshortcut)*