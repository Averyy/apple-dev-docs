# AVAssetVariant.VideoAttributes.LayoutAttributes

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

Attributes that describe the layout of video content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
class LayoutAttributes
```

```objc
@interface AVAssetVariantVideoLayoutAttributes : NSObject
```

## Topics

### Accessing attributes
- [var stereoViewComponents: CMStereoViewComponents](./layoutattributes/stereoviewcomponents.md)
  Attributes that describe the video’s stereo components.
- [var projectionType: CMProjectionType](./layoutattributes/projectiontype.md)
  Describes the video projection.

## Relationships

### Inherits From
- [NSObject](../../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [NSObjectProtocol](../../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Inspecting the attributes
- [var codecTypes: [CMVideoCodecType]](./codectypes.md)
  The video sample codec types present in the variant’s renditions.
- [var nominalFrameRate: Double?](./nominalframerate.md)
  The nominal frame rate of the variant’s renditions.
- [var presentationSize: CGSize](./presentationsize.md)
  The presentation size of the variant’s renditions.
- [var videoRange: AVVideoRange](./videorange.md)
  The video range of the variant.
- [struct AVVideoRange](../../avvideorange.md)
  Constants that describe a video variant’s dynamic range.
- [var videoLayoutAttributes: [AVAssetVariant.VideoAttributes.LayoutAttributes]](./videolayoutattributes.md)
  Attributes that describe the layout of the video content.
- [codecTypes](../../avassetvariantvideoattributes/codectypes.md)
  The video sample codec types present in the variant’s renditions.
- [nominalFrameRate](../../avassetvariantvideoattributes/nominalframerate.md)
  The nominal frame rate of the variant’s renditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant/videoattributes-swift.class/layoutattributes)*