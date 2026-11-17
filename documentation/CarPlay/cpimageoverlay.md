# CPImageOverlay

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A type that manages content you layer on top of a thumbnail image.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
@MainActor
class CPImageOverlay
```

```objc
@interface CPImageOverlay : NSObject
```

## Overview

Use a `CPImageOverlay` object to place text or a small image on top of the main image in a [`CPThumbnailImage`](./cpthumbnailimage.md) object. Add text content when you want to display a badge on one of the thumbnail images you display in a list interface. Add an image to display an icon or other indicator on top of the thumbnail image instead. Because overlay content is separate from the thumbnail image, you can update it periodically. For example, you might update the badge value when someone reads some messages or plays some songs.

You can add a `CPImageOverlay` object to a thumbnail image at creation time or any time later. Configure the content for the overlay and specify how you want to align the content. Overlays appear inside the top edge of the thumbnail image and with the alignment you specify.

## Topics

### Creating an image overlay
- [init(image: UIImage, alignment: CPImageOverlay.Alignment)](./cpimageoverlay/init%28image,alignment%29.md)
  Creates an overlay that displays an image.
- [init(text: String, textColor: UIColor, backgroundColor: UIColor, alignment: CPImageOverlay.Alignment)](./cpimageoverlay/init%28text,textcolor,backgroundcolor,alignment%29.md)
  Creates an overlay that displays text in a colored badge.
- [init?(coder: NSCoder)](./cpimageoverlay/init%28coder%29.md)
### Getting the overlay details
- [var image: UIImage?](./cpimageoverlay/image.md)
  The image to display at top of the thumbnail.
- [var text: String?](./cpimageoverlay/text.md)
  The text to display in a badge at the top of the thumbnail.
- [var textColor: UIColor?](./cpimageoverlay/textcolor.md)
  The color to apply to the badge’s text.
- [var backgroundColor: UIColor?](./cpimageoverlay/backgroundcolor.md)
  The color to display behind the badge’s text.
### Getting the overlay position
- [var alignment: CPImageOverlay.Alignment](./cpimageoverlay/alignment-swift.property.md)
  The alignment of the overlay inside the top edge of the thumbnail.
- [CPImageOverlay.Alignment](./cpimageoverlay/alignment-swift.enum.md)
  Constants that specify the placement of overlay images in a thumbnail.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Element overlays
- [class CPSportsOverlay](./cpsportsoverlay.md)
  A type that displays sporting event details on top of a thumbnail image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpimageoverlay)*