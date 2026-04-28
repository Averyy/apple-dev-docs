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
  An optional  overlay for the thumbnail.
- [var sportsOverlay: CPSportsOverlay?](cpthumbnailimage/sportsoverlay.md)
  An optional sports overlay for the thumbnail.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpthumbnailimage)*