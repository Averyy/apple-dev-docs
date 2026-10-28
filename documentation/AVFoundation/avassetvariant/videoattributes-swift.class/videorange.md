# videoRange

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The video range of the variant.

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
var videoRange: AVVideoRange { get }
```

```objc
@property (nonatomic, readonly) AVVideoRange videoRange;
```

## Discussion

The property defaults to [`sdr`](../../avvideorange/sdr.md).

## See Also

### Inspecting the attributes
- [var codecTypes: [CMVideoCodecType]](./codectypes.md)
  The video sample codec types present in the variant’s renditions.
- [var nominalFrameRate: Double?](./nominalframerate.md)
  The nominal frame rate of the variant’s renditions.
- [var presentationSize: CGSize](./presentationsize.md)
  The presentation size of the variant’s renditions.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant/videoattributes-swift.class/videorange)*