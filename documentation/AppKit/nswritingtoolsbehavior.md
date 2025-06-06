# NSWritingToolsBehavior

**Framework**: AppKit  
**Kind**: enum

Constants that specify the Writing Tools experience for the underlying view.

**Availability**:
- macOS 15.0+

## Declaration

```swift
enum NSWritingToolsBehavior
```

#### Overview

Writing Tools provide proofreading and rewriting support for the content of text views. On devices that support Writing Tools features, people engage the system UI to choose how to rewrite all or part of the available text. These constants indicate whether people experience Writing Tools inline with their text, in an overlay panel, or not at all.

## Topics

### Getting the Writing Tools behaviors
- [NSWritingToolsBehavior.none](nswritingtoolsbehavior/none.md)
  An option to prevent Writing Tools from modifying the text in the view.
- [NSWritingToolsBehavior.default](nswritingtoolsbehavior/default.md)
  An option to let the system determine the best way to enable Writing Tools for the view.
- [NSWritingToolsBehavior.complete](nswritingtoolsbehavior/complete.md)
  An option to provide the complete Writing Tools experience for the text view.
- [NSWritingToolsBehavior.limited](nswritingtoolsbehavior/limited.md)
  An option to provide a limited, overlay-panel experience for the text view.
### Initializers
- [init?(rawValue: Int)](nswritingtoolsbehavior/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSCursor.FrameResizePosition](nscursor/frameresizeposition.md)
  The position along the perimeter of a rectangular frame (its edges and corners) from which it’s resized.
- [enum NSHorizontalDirection](nshorizontaldirection.md)
  An absolute direction on the horizontal axis.
- [enum NSSharingCollaborationMode](nssharingcollaborationmode.md)
  Represents the types of sharing (collaborating on an item vs. sending a copy of the item) The share picker supports up to two modes, each of which corresponds to one of these types
- [NSImage.DynamicRange](nsimage/dynamicrange.md)
  Describes how High Dynamic Range (HDR) image content displays.
- [enum NSTextCursorAccessoryPlacement](nstextcursoraccessoryplacement.md)
- [enum NSVerticalDirection](nsverticaldirection.md)
  A direction on the vertical axis.
- [struct NSWritingToolsResultOptions](nswritingtoolsresultoptions.md)
  Constants to specify what type of content to allow in Writing Tools suggestions or rewrites.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolsbehavior)*