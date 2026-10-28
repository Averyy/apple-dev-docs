# UIPencilPreferredAction.ignore

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

An action that does nothing.

**Availability**:
- iOS 12.1+
- iPadOS 12.1+
- Mac Catalyst 13.1+
- visionOS 26.2+

## Declaration

```swift
case ignore
```

```c
UIPencilPreferredActionIgnore
```

## Discussion

The system returns this action if any of the following conditions are true:

- The Apple Pencil doesn’t have a configured preferred action.
- The iPad’s accessibility settings disable Apple Pencil interactions.

## See Also

### Preferred actions
- [UIPencilPreferredAction.switchEraser](./switcheraser.md)
  An action that switches between the current tool and the eraser.
- [UIPencilPreferredAction.switchPrevious](./switchprevious.md)
  An action that switches between the current tool and the last used tool.
- [UIPencilPreferredAction.showColorPalette](./showcolorpalette.md)
  An action that toggles the display of the color palette.
- [UIPencilPreferredAction.showInkAttributes](./showinkattributes.md)
  An action that toggles the display of the selected tool’s ink attributes.
- [UIPencilPreferredAction.showContextualPalette](./showcontextualpalette.md)
  An action that toggles shows a contextual palette of markup tools, or undo and redo options if tools aren’t available.
- [UIPencilPreferredAction.runSystemShortcut](./runsystemshortcut.md)
  An action that runs a system shortcut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilpreferredaction/ignore)*