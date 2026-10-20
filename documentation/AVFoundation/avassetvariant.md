# AVAssetVariant

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that represents a bit rate variant.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class AVAssetVariant
```

```objc
@interface AVAssetVariant : NSObject
```

## Topics

### Configuring attributes
- [var audioAttributes: AVAssetVariant.AudioAttributes?](./avassetvariant/audioattributes-swift.property.md)
  The audio rendition attributes for the variant.
- [AVAssetVariant.AudioAttributes](./avassetvariant/audioattributes-swift.class.md)
  An object that defines the audio attributes for an asset variant.
- [var videoAttributes: AVAssetVariant.VideoAttributes?](./avassetvariant/videoattributes-swift.property.md)
  The video rendition attributes for the variant.
- [AVAssetVariant.VideoAttributes](./avassetvariant/videoattributes-swift.class.md)
  An object that defines the video attributes for an asset variant.
### Configuring bit rate
- [var averageBitRate: Double?](./avassetvariant/averagebitrate-5p1oh.md)
  The average bit rate for the variant.
- [var peakBitRate: Double?](./avassetvariant/peakbitrate-9hzpi.md)
  The peak bit rate for the variant.
### Accessing the URL
- [var url: URL](./avassetvariant/url.md)
  Provides URL to media playlist corresponding to variant

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a variant qualifier
- [convenience init(variant: AVAssetVariant)](./avassetvariantqualifier/init%28variant%29.md)
  Creates a variant qualifier with an asset variant.
- [convenience init(predicate: NSPredicate)](./avassetvariantqualifier/init%28predicate%29.md)
  Creates a variant qualifier with a predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant)*