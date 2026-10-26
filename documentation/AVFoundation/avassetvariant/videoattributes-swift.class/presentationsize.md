# presentationSize

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The presentation size of the variant’s renditions.

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
var presentationSize: CGSize { get }
```

```objc
@property (nonatomic, readonly) CGSize presentationSize;
```

## See Also

### Inspecting the attributes
- [var codecTypes: [CMVideoCodecType]](./codectypes.md)
  The video sample codec types present in the variant’s renditions.
- [var nominalFrameRate: Double?](./nominalframerate.md)
  The nominal frame rate of the variant’s renditions.
- [var videoRange: AVVideoRange](./videorange.md)
  The video range of the variant.
- [struct AVVideoRange](../../avvideorange.md)
  Constants that describe a video variant’s dynamic range.
- [var videoLayoutAttributes: [AVAssetVariant.VideoAttributes.LayoutAttributes]](./videolayoutattributes.md)
  Attributes that describe the layout of the video content.
- [AVAssetVariant.VideoAttributes.LayoutAttributes](./layoutattributes.md)
  Attributes that describe the layout of video content.
- [codecTypes](../../avassetvariantvideoattributes/codectypes.md)
  The video sample codec types present in the variant’s renditions.
- [nominalFrameRate](../../avassetvariantvideoattributes/nominalframerate.md)
  The nominal frame rate of the variant’s renditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant/videoattributes-swift.class/presentationsize)*