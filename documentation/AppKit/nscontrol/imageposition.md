# NSControl.ImagePosition

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

A constant for specifying the position of a button’s image relative to its title.

**Availability**:
- macOS

## Declaration

```swift
enum ImagePosition
```

```c
enum NSCellImagePosition : NSUInteger;
```

## Overview

Use these constants with the [`imagePosition`](../nsbutton/imageposition.md) property of [`NSButton`](../nsbutton.md) and [`NSButtonCell`](../nsbuttoncell.md).

## Topics

### Positioning a Control’s Image
- [NSControl.ImagePosition.noImage](./imageposition/noimage.md)
  The cell doesn’t display an image.
- [NSControl.ImagePosition.imageOnly](./imageposition/imageonly.md)
  The cell displays an image but not a title.
- [NSControl.ImagePosition.imageLeading](./imageposition/imageleading.md)
  The image is on the title’s leading edge.
- [NSControl.ImagePosition.imageTrailing](./imageposition/imagetrailing.md)
  The image is on the title’s trailing edge.
- [NSControl.ImagePosition.imageLeft](./imageposition/imageleft.md)
  The image is to the left of the title.
- [NSControl.ImagePosition.imageRight](./imageposition/imageright.md)
  The image is to the right of the title.
- [NSControl.ImagePosition.imageBelow](./imageposition/imagebelow.md)
  The image is below the title.
- [NSControl.ImagePosition.imageAbove](./imageposition/imageabove.md)
  The image is above the title.
- [NSControl.ImagePosition.imageOverlaps](./imageposition/imageoverlaps.md)
  The image overlaps the title.
### Initializers
- [init?(rawValue: UInt)](./imageposition/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring button images
- [var image: NSImage?](../nsbutton/image.md)
  The image that appears on the button when it’s in an off state, or `nil` if there is no such image.
- [var alternateImage: NSImage?](../nsbutton/alternateimage.md)
  An alternate image that appears on the button when the button is in an on state.
- [var imagePosition: NSControl.ImagePosition](../nsbutton/imageposition.md)
  The position of the button’s image relative to its title.
- [var isBordered: Bool](../nsbutton/isbordered.md)
  A Boolean value that determines whether the button has a border.
- [var isTransparent: Bool](../nsbutton/istransparent.md)
  A Boolean value that indicates whether the button is transparent.
- [var bezelStyle: NSButton.BezelStyle](../nsbutton/bezelstyle-swift.property.md)
  The appearance of the button’s border.
- [var bezelColor: NSColor?](../nsbutton/bezelcolor.md)
  The color of the button’s bezel, in appearances that support it.
- [var showsBorderOnlyWhileMouseInside: Bool](../nsbutton/showsborderonlywhilemouseinside.md)
  A Boolean value that determines whether the button displays its border only when the pointer is over it.
- [var imageHugsTitle: Bool](../nsbutton/imagehugstitle.md)
  A Boolean value that determines how the button’s image and title are positioned together within the button bezel.
- [var imageScaling: NSImageScaling](../nsbutton/imagescaling.md)
  The scaling mode applied to make the cell’s image fit the frame of the image view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/imageposition)*