# PencilPreferredAction

**Framework**: SwiftUI  
**Kind**: struct

An action that the user prefers to perform after double-tapping their Apple Pencil.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+
- visionOS 26.2+

## Declaration

```swift
struct PencilPreferredAction
```

## Topics

### Getting the preffered actions
- [static let ignore: PencilPreferredAction](pencilpreferredaction/ignore.md)
  An action that does nothing.
- [static let showColorPalette: PencilPreferredAction](pencilpreferredaction/showcolorpalette.md)
  An action that toggles the display of the color palette.
- [static let showInkAttributes: PencilPreferredAction](pencilpreferredaction/showinkattributes.md)
  An action that toggles the display of the current tool’s ink attributes.
- [static let switchEraser: PencilPreferredAction](pencilpreferredaction/switcheraser.md)
  An action that switches between the current tool and the eraser.
- [static let switchPrevious: PencilPreferredAction](pencilpreferredaction/switchprevious.md)
  An action that switches between the current tool and the last used tool.
### Type Properties
- [static let runSystemShortcut: PencilPreferredAction](pencilpreferredaction/runsystemshortcut.md)
  An action that runs a system shortcut.
- [static let showContextualPalette: PencilPreferredAction](pencilpreferredaction/showcontextualpalette.md)
  An action that toggles the display of the contextual palette, or the undo/redo panel if contextual palette is not available.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func onPencilDoubleTap(perform: (PencilDoubleTapGestureValue) -> Void) -> some View](view/onpencildoubletap(perform:).md)
  Adds an action to perform after the user double-taps their Apple Pencil.
- [func onPencilSqueeze(perform: (PencilSqueezeGesturePhase) -> Void) -> some View](view/onpencilsqueeze(perform:).md)
  Adds an action to perform when the user squeezes their Apple Pencil.
- [var preferredPencilDoubleTapAction: PencilPreferredAction](environmentvalues/preferredpencildoubletapaction.md)
  The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.
- [var preferredPencilSqueezeAction: PencilPreferredAction](environmentvalues/preferredpencilsqueezeaction.md)
  The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.
- [struct PencilDoubleTapGestureValue](pencildoubletapgesturevalue.md)
  Describes the value of an Apple Pencil double-tap gesture.
- [struct PencilSqueezeGestureValue](pencilsqueezegesturevalue.md)
  Describes the value of an Apple Pencil squeeze gesture.
- [enum PencilSqueezeGesturePhase](pencilsqueezegesturephase.md)
  Describes the phase and value of an Apple Pencil squeeze gesture.
- [struct PencilHoverPose](pencilhoverpose.md)
  A value describing the location and distance of an Apple Pencil hovering in the area above a view’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pencilpreferredaction)*