# CPThumbnailImage

**Framework**: CarPlay  
**Kind**: class

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
@MainActor
class CPThumbnailImage
```

## Topics

### Initializers
- [init?(coder: NSCoder)](cpthumbnailimage/init(coder:).md)
- [init(image: UIImage)](cpthumbnailimage/init(image:).md)
  Initialize a thumbnail with an image.
- [init(image: UIImage, imageOverlay: CPImageOverlay?, sportsOverlay: CPSportsOverlay?)](cpthumbnailimage/init(image:imageoverlay:sportsoverlay:).md)
  Initialize a thumbnail with a combination of properties.
### Instance Properties
- [var image: UIImage](cpthumbnailimage/image.md)
  The image displayed in the thumbnail.
- [var imageOverlay: CPImageOverlay?](cpthumbnailimage/imageoverlay.md)
  An optional overlay for the thumbnail.
- [var sportsOverlay: CPSportsOverlay?](cpthumbnailimage/sportsoverlay.md)
  An optional sports overlay for the thumbnail.
### Type Methods
- [class func maximumImageSize(forAspectRatio: CGFloat) -> CGSize](cpthumbnailimage/maximumimagesize(foraspectratio:).md)
  Returns the recommended maximum image size for a @c CPThumbnailImage with the given aspect ratio.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpthumbnailimage)*