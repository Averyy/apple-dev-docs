# NSCursor.FrameResizePosition

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The position along the perimeter of a rectangular frame (its edges and corners) from which it’s resized.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
@frozen
enum FrameResizePosition
```

```c
enum NSCursorFrameResizePosition : NSUInteger;
```

## Topics

### Enumeration Cases
- [NSCursor.FrameResizePosition.bottom](./frameresizeposition/bottom.md)
  The bottom edge of the frame.
- [NSCursor.FrameResizePosition.bottomLeft](./frameresizeposition/bottomleft.md)
  The bottom left corner of the frame.
- [NSCursor.FrameResizePosition.bottomRight](./frameresizeposition/bottomright.md)
  The bottom right corner of the frame.
- [NSCursor.FrameResizePosition.left](./frameresizeposition/left.md)
  The left edge of the frame.
- [NSCursor.FrameResizePosition.right](./frameresizeposition/right.md)
  The right edge of the frame.
- [NSCursor.FrameResizePosition.top](./frameresizeposition/top.md)
  The top edge of the frame.
- [NSCursor.FrameResizePosition.topLeft](./frameresizeposition/topleft.md)
  The top left corner of the frame.
- [NSCursor.FrameResizePosition.topRight](./frameresizeposition/topright.md)
  The top right corner of the frame.
### Initializers
- [init?(rawValue: UInt)](./frameresizeposition/init%28rawvalue%29.md)
### Type Methods
- [static func bottomLeading(relativeTo: NSUserInterfaceLayoutDirection) -> NSCursor.FrameResizePosition](./frameresizeposition/bottomleading%28relativeto%29.md)
  The bottom leading corner of the frame, in the given user interface layout direction.
- [static func bottomTrailing(relativeTo: NSUserInterfaceLayoutDirection) -> NSCursor.FrameResizePosition](./frameresizeposition/bottomtrailing%28relativeto%29.md)
  The bottom trailing corner of the frame, in the given user interface layout direction.
- [static func leading(relativeTo: NSUserInterfaceLayoutDirection) -> NSCursor.FrameResizePosition](./frameresizeposition/leading%28relativeto%29.md)
  The leading edge of the frame, in the given user interface layout direction.
- [static func topLeading(relativeTo: NSUserInterfaceLayoutDirection) -> NSCursor.FrameResizePosition](./frameresizeposition/topleading%28relativeto%29.md)
  The top leading corner of the frame, in the given user interface layout direction.
- [static func topTrailing(relativeTo: NSUserInterfaceLayoutDirection) -> NSCursor.FrameResizePosition](./frameresizeposition/toptrailing%28relativeto%29.md)
  The top trailing corner of the frame, in the given user interface layout direction.
- [static func trailing(relativeTo: NSUserInterfaceLayoutDirection) -> NSCursor.FrameResizePosition](./frameresizeposition/trailing%28relativeto%29.md)
  The trailing edge of the frame, in the given user interface layout direction.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [CaseIterable](../../Swift/caseiterable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [enum NSHorizontalDirection](../nshorizontaldirection.md)
  An absolute direction on the horizontal axis.
- [enum NSSharingCollaborationMode](../nssharingcollaborationmode.md)
  Represents the types of sharing (collaborating on an item vs. sending a copy of the item) The share picker supports up to two modes, each of which corresponds to one of these types
- [NSImage.DynamicRange](../nsimage/dynamicrange.md)
  Describes how High Dynamic Range (HDR) image content displays.
- [enum NSTextCursorAccessoryPlacement](../nstextcursoraccessoryplacement.md)
- [enum NSVerticalDirection](../nsverticaldirection.md)
  A direction on the vertical axis.
- [enum NSWritingToolsBehavior](../nswritingtoolsbehavior.md)
  Constants that specify the Writing Tools experience for the underlying view.
- [struct NSWritingToolsResultOptions](../nswritingtoolsresultoptions.md)
  Constants to specify what type of content to allow in Writing Tools suggestions or rewrites.
- [NSCursorFrameResizeDirections](../nscursorframeresizedirections.md)
  The directions in which a rectangular frame can be resized.
- [NSHorizontalDirections](../nshorizontaldirections.md)
  The absolute directions on the horizontal axis.
- [NSVerticalDirections](../nsverticaldirections.md)
  The directions on the vertical axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/frameresizeposition)*