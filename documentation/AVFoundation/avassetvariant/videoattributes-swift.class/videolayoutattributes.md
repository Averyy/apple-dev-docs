# videoLayoutAttributes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Attributes that describe the layout of the video content.

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
var videoLayoutAttributes: [AVAssetVariant.VideoAttributes.LayoutAttributes] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVAssetVariantVideoLayoutAttributes *> * videoLayoutAttributes;
```

#### Discussion

This property may contain more that one element if the variant contains a collection of differing video layout media attributes over time.

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
- [AVAssetVariant.VideoAttributes.LayoutAttributes](./layoutattributes.md)
  Attributes that describe the layout of video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant/videoattributes-swift.class/videolayoutattributes)*