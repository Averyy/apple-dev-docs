# depthData

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

Depth data associated with the image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var depthData: AVDepthData? { get }
```

```objc
@property (nonatomic, readonly, nullable) AVDepthData * depthData;
```

#### Discussion

Returns an [`AVDepthData`](../../AVFoundation/avdepthdata.md) if the [`CIImage`](../ciimage.md) was created with [`imageWithData:`](./imagewithdata_.md) or [`imageWithContentsOfURL:`](./imagewithcontentsofurl_.md) and one of the options [`auxiliaryDepth`](../ciimageoption/auxiliarydepth.md) or [`auxiliaryDisparity`](../ciimageoption/auxiliarydisparity.md), otherwise [`nil`](../../ObjectiveC/nil-227m0.md).

## See Also

### Accessing Original Image Content
- [var cgImage: CGImage?](./cgimage.md)
  The CoreGraphics image object this image was created from, if applicable.
- [var pixelBuffer: CVPixelBuffer?](./pixelbuffer.md)
  The CoreVideo pixel buffer this image was created from, if applicable.
- [var portraitEffectsMatte: AVPortraitEffectsMatte?](./portraiteffectsmatte.md)
  The portrait effects matte associated with the image.
- [var semanticSegmentationMatte: AVSemanticSegmentationMatte?](./semanticsegmentationmatte.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/depthdata)*