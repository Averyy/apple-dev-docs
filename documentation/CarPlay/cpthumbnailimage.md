# CPThumbnailImage

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

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

## Topics

### Initializers
- [init?(coder: NSCoder)](./cpthumbnailimage/init%28coder%29.md)
- [init(image: UIImage)](./cpthumbnailimage/init%28image%29.md)
  Initialize a thumbnail with an image.
- [init(image: UIImage, imageOverlay: CPImageOverlay?, sportsOverlay: CPSportsOverlay?)](./cpthumbnailimage/init%28image,imageoverlay,sportsoverlay%29.md)
  Initialize a thumbnail with a combination of properties.
### Instance Properties
- [var image: UIImage](./cpthumbnailimage/image.md)
  The image displayed in the thumbnail.
- [var imageOverlay: CPImageOverlay?](./cpthumbnailimage/imageoverlay.md)
  An optional overlay for the thumbnail.
- [var sportsOverlay: CPSportsOverlay?](./cpthumbnailimage/sportsoverlay.md)
  An optional sports overlay for the thumbnail.
### Type Methods
- [class func maximumImageSize(forAspectRatio: CGFloat) -> CGSize](./cpthumbnailimage/maximumimagesize%28foraspectratio%29.md)
  Returns the recommended maximum image size for a @c CPThumbnailImage with the given aspect ratio.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpthumbnailimage)*