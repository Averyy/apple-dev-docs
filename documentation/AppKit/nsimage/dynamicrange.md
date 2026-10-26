# NSImage.DynamicRange

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Describes how High Dynamic Range (HDR) image content displays.

**Availability**:
- macOS 14.0+

## Declaration

```swift
enum DynamicRange
```

```c
enum NSImageDynamicRange : NSInteger;
```

#### Overview

Use this type to enable or constrain the display of High Dynamic Range (HDR) in an [`NSImageView`](../nsimageview.md). Displaying HDR content in an [`NSImageView`](../nsimageview.md) requires that the [`NSImage`](../nsimage.md) has HDR content in the ITU-R 2100 color space and that the output device has Extended Dynamic Range (EDR) capabilities.

## Topics

### Setting the dynamic range
- [NSImage.DynamicRange.standard](./dynamicrange/standard.md)
  Restricts the image content dynamic range to the standard range regardless of the actual range of the image content.
- [NSImage.DynamicRange.constrainedHigh](./dynamicrange/constrainedhigh.md)
  Allows for constrained High Dynamic Range (HDR) image content which is useful for mixing HDR and Standard Dynamic Range (SDR) content.
- [NSImage.DynamicRange.high](./dynamicrange/high.md)
  Allows image content to use extended dynamic range if it has dynamic range content.
- [NSImage.DynamicRange.unspecified](./dynamicrange/unspecified.md)
  Indicates that the dynamic range treatment of the image is unknown or otherwise unspecified.
### Initializers
- [init?(rawValue: Int)](./dynamicrange/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [NSCursor.FrameResizePosition](../nscursor/frameresizeposition.md)
  The position along the perimeter of a rectangular frame (its edges and corners) from which it’s resized.
- [enum NSHorizontalDirection](../nshorizontaldirection.md)
  An absolute direction on the horizontal axis.
- [enum NSSharingCollaborationMode](../nssharingcollaborationmode.md)
  Represents the types of sharing (collaborating on an item vs. sending a copy of the item) The share picker supports up to two modes, each of which corresponds to one of these types
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/dynamicrange)*