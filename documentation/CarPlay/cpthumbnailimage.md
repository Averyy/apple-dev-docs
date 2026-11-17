# CPThumbnailImage

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

An image that can display overlays and metadata on top of the image.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
@MainActor
class CPThumbnailImage
```

```objc
@interface CPThumbnailImage : NSObject
```

## Overview

A `CPThumbnailImage` provides an alternative to a plain image in the rows or header of a list. A thumbnail image contains a base image and optional overlay content. Use the overlays to add a badge to the image, tag it with a specific icon, or display information from a sporting event.

When creating a list, configure row elements with `CPThumbnailImage` objects if you think you might need overlays later. You can add overlays at creation time or after you create the thumbnail image. For example, a sports app might create thumbnail images for different sports events and update the overlays each time the scores change.

## Topics

### Creating a thumbnail image
- [init(image: UIImage)](./cpthumbnailimage/init%28image%29.md)
  Creates a thumbnail with an image object.
- [init(image: UIImage, imageOverlay: CPImageOverlay?, sportsOverlay: CPSportsOverlay?)](./cpthumbnailimage/init%28image,imageoverlay,sportsoverlay%29.md)
  Creates a thumbnail with an image object and optional overlays.
- [init?(coder: NSCoder)](./cpthumbnailimage/init%28coder%29.md)
### Getting the thumbnail content
- [var image: UIImage](./cpthumbnailimage/image.md)
  The main image to display.
- [var imageOverlay: CPImageOverlay?](./cpthumbnailimage/imageoverlay.md)
  An overlay with a custom image or text badge.
- [var sportsOverlay: CPSportsOverlay?](./cpthumbnailimage/sportsoverlay.md)
  An overlay with sporting event details, including the teams and current score.
### Getting the supported image size
- [class func maximumImageSize(forAspectRatio: CGFloat) -> CGSize](./cpthumbnailimage/maximumimagesize%28foraspectratio%29.md)
  Calculates the maximum image size for a thumbnail image with the specified aspect ratio.

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

### Common types
- [class CPListImageRowItemElement](./cplistimagerowitemelement.md)
  An abstract class for an element in a row of a list.
- [protocol CPSelectableListItem](./cpselectablelistitem.md)
  An interface for responding to selections in list items.
- [protocol CPListTemplateItem](./cplisttemplateitem.md)
  An interface that describes the common properties of all list item types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpthumbnailimage)*