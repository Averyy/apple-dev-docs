# codecTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The video sample codec types present in the variant’s renditions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * codecTypes;
```

## See Also

### Inspecting the attributes
- [nominalFrameRate](./nominalframerate.md)
  The nominal frame rate of the variant’s renditions.
- [var presentationSize: CGSize](../avassetvariant/videoattributes-swift.class/presentationsize.md)
  The presentation size of the variant’s renditions.
- [var videoRange: AVVideoRange](../avassetvariant/videoattributes-swift.class/videorange.md)
  The video range of the variant.
- [struct AVVideoRange](../avvideorange.md)
  Constants that describe a video variant’s dynamic range.
- [var videoLayoutAttributes: [AVAssetVariant.VideoAttributes.LayoutAttributes]](../avassetvariant/videoattributes-swift.class/videolayoutattributes.md)
  Attributes that describe the layout of the video content.
- [AVAssetVariant.VideoAttributes.LayoutAttributes](../avassetvariant/videoattributes-swift.class/layoutattributes.md)
  Attributes that describe the layout of video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariantvideoattributes/codectypes)*