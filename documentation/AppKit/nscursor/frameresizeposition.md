# NSCursor.FrameResizePosition

**Framework**: AppKit  
**Kind**: enum

The position along the perimeter of a rectangular frame (its edges and corners) from which it’s resized.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
@frozen
enum FrameResizePosition
```

## Topics

### Enumeration Cases
- [NSCursor.FrameResizePosition.bottom](nscursor/frameresizeposition/bottom.md)
  The bottom edge of the frame.
- [NSCursor.FrameResizePosition.bottomLeft](nscursor/frameresizeposition/bottomleft.md)
  The bottom left corner of the frame.
- [NSCursor.FrameResizePosition.bottomRight](nscursor/frameresizeposition/bottomright.md)
  The bottom right corner of the frame.
- [NSCursor.FrameResizePosition.left](nscursor/frameresizeposition/left.md)
  The left edge of the frame.
- [NSCursor.FrameResizePosition.right](nscursor/frameresizeposition/right.md)
  The right edge of the frame.
- [NSCursor.FrameResizePosition.top](nscursor/frameresizeposition/top.md)
  The top edge of the frame.
- [NSCursor.FrameResizePosition.topLeft](nscursor/frameresizeposition/topleft.md)
  The top left corner of the frame.
- [NSCursor.FrameResizePosition.topRight](nscursor/frameresizeposition/topright.md)
  The top right corner of the frame.
### Initializers
- [init?(rawValue: UInt)](nscursor/frameresizeposition/init(rawvalue:).md)
### Type Methods
- [static func bottomLeading(relativeTo: NSUserInterfaceLayoutDirection) -> NSCursor.FrameResizePosition](nscursor/frameresizeposition/bottomleading(relativeto:).md)
  The bottom leading corner of the frame, in the given user interface layout direction.
- [static func bottomTrailing(relativeTo: NSUserInterfaceLayoutDirection) -> NSCursor.FrameResizePosition](nscursor/frameresizeposition/bottomtrailing(relativeto:).md)
  The bottom trailing corner of the frame, in the given user interface layout direction.
- [static func leading(relativeTo: NSUserInterfaceLayoutDirection) -> NSCursor.FrameResizePosition](nscursor/frameresizeposition/leading(relativeto:).md)
  The leading edge of the frame, in the given user interface layout direction.
- [static func topLeading(relativeTo: NSUserInterfaceLayoutDirection) -> NSCursor.FrameResizePosition](nscursor/frameresizeposition/topleading(relativeto:).md)
  The top leading corner of the frame, in the given user interface layout direction.
- [static func topTrailing(relativeTo: NSUserInterfaceLayoutDirection) -> NSCursor.FrameResizePosition](nscursor/frameresizeposition/toptrailing(relativeto:).md)
  The top trailing corner of the frame, in the given user interface layout direction.
- [static func trailing(relativeTo: NSUserInterfaceLayoutDirection) -> NSCursor.FrameResizePosition](nscursor/frameresizeposition/trailing(relativeto:).md)
  The trailing edge of the frame, in the given user interface layout direction.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum NSHorizontalDirection](nshorizontaldirection.md)
  An absolute direction on the horizontal axis.
- [enum NSSharingCollaborationMode](nssharingcollaborationmode.md)
  Represents the types of sharing (collaborating on an item vs. sending a copy of the item) The share picker supports up to two modes, each of which corresponds to one of these types
- [NSImage.DynamicRange](nsimage/dynamicrange.md)
  Describes how High Dynamic Range (HDR) image content displays.
- [enum NSTextCursorAccessoryPlacement](nstextcursoraccessoryplacement.md)
- [enum NSVerticalDirection](nsverticaldirection.md)
  A direction on the vertical axis.
- [enum NSWritingToolsBehavior](nswritingtoolsbehavior.md)
  Constants that specify the Writing Tools experience for the underlying view.
- [struct NSWritingToolsResultOptions](nswritingtoolsresultoptions.md)
  Constants to specify what type of content to allow in Writing Tools suggestions or rewrites.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/frameresizeposition)*