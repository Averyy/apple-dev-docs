# AVPlaybackUserInterfaceContentArtwork

**Framework**: AVKit  
**Kind**: class

Base class representing artwork or cover art for media content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class AVPlaybackUserInterfaceContentArtwork
```

#### Overview

Use a concrete subclass such as [`AVPlaybackUserInterfaceContentURLArtwork`](avplaybackuserinterfacecontenturlartwork.md) to create artwork instances.

## Topics

### Initializers
- [init?(coder: NSCoder)](avplaybackuserinterfacecontentartwork/init(coder:).md)
### Instance Properties
- [var size: CGSize](avplaybackuserinterfacecontentartwork/size.md)
  The pixel dimensions of the artwork image.
### Type Methods
- [class func artwork(url: URL, contentType: UTType, size: CGSize) -> AVPlaybackUserInterfaceContentURLArtwork](avplaybackuserinterfacecontentartwork/artwork(url:contenttype:size:).md)
  Creates an artwork instance that references an image at the given URL.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVPlaybackUserInterfaceContentURLArtwork](avplaybackuserinterfacecontenturlartwork.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentartwork)*