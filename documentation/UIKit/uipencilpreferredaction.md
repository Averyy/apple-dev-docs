# UIPencilPreferredAction

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The actions Apple Pencil can perform after a person performs a double tap or squeeze.

**Availability**:
- iOS 12.1+
- iPadOS 12.1+
- Mac Catalyst 13.1+
- visionOS 26.2+

## Declaration

```swift
enum UIPencilPreferredAction
```

```c
enum UIPencilPreferredAction : NSInteger;
```

## Topics

### Preferred actions
- [UIPencilPreferredAction.ignore](./uipencilpreferredaction/ignore.md)
  An action that does nothing.
- [UIPencilPreferredAction.switchEraser](./uipencilpreferredaction/switcheraser.md)
  An action that switches between the current tool and the eraser.
- [UIPencilPreferredAction.switchPrevious](./uipencilpreferredaction/switchprevious.md)
  An action that switches between the current tool and the last used tool.
- [UIPencilPreferredAction.showColorPalette](./uipencilpreferredaction/showcolorpalette.md)
  An action that toggles the display of the color palette.
- [UIPencilPreferredAction.showInkAttributes](./uipencilpreferredaction/showinkattributes.md)
  An action that toggles the display of the selected tool’s ink attributes.
- [UIPencilPreferredAction.showContextualPalette](./uipencilpreferredaction/showcontextualpalette.md)
  An action that toggles shows a contextual palette of markup tools, or undo and redo options if tools aren’t available.
- [UIPencilPreferredAction.runSystemShortcut](./uipencilpreferredaction/runsystemshortcut.md)
  An action that runs a system shortcut.
### Initializers
- [init?(rawValue: Int)](./uipencilpreferredaction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Determining preferences for actions
- [class var preferredTapAction: UIPencilPreferredAction](./uipencilinteraction/preferredtapaction.md)
  A person’s preferred double-tap action for Apple Pencil, as specified in the Settings app.
- [class var preferredSqueezeAction: UIPencilPreferredAction](./uipencilinteraction/preferredsqueezeaction.md)
  A person’s preferred squeeze action for Apple Pencil, as specified in the Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilpreferredaction)*