# NSHorizontalDirection

**Framework**: AppKit  
**Kind**: enum

An absolute direction on the horizontal axis.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
@frozen
enum NSHorizontalDirection
```

## Topics

### Structures
- [NSHorizontalDirection.Set](nshorizontaldirection/set.md)
  An efficient set of horizontal directions.
### Enumeration Cases
- [NSHorizontalDirection.left](nshorizontaldirection/left.md)
  The left direction.
- [NSHorizontalDirection.right](nshorizontaldirection/right.md)
  The right direction.
### Type Methods
- [static func leading(relativeTo: NSUserInterfaceLayoutDirection) -> NSHorizontalDirection](nshorizontaldirection/leading(relativeto:).md)
  Returns the leading direction in the given user interface layout direction.
- [static func trailing(relativeTo: NSUserInterfaceLayoutDirection) -> NSHorizontalDirection](nshorizontaldirection/trailing(relativeto:).md)
  Returns the trailing direction in the given user interface layout direction.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSCursor.FrameResizePosition](nscursor/frameresizeposition.md)
  The position along the perimeter of a rectangular frame (its edges and corners) from which it’s resized.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshorizontaldirection)*