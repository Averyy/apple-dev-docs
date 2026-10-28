# portraitEffectsMatte

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The portrait effects matte associated with the image.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var portraitEffectsMatte: AVPortraitEffectsMatte? { get }
```

```objc
@property (nonatomic, readonly, nullable) AVPortraitEffectsMatte * portraitEffectsMatte;
```

## Discussion

[`AVPortraitEffectsMatte`](../../AVFoundation/avportraiteffectsmatte.md) representation of portrait effects.

## See Also

### Accessing Original Image Content
- [var cgImage: CGImage?](./cgimage.md)
  The CoreGraphics image object this image was created from, if applicable.
- [var pixelBuffer: CVPixelBuffer?](./pixelbuffer.md)
  The CoreVideo pixel buffer this image was created from, if applicable.
- [var depthData: AVDepthData?](./depthdata.md)
  Depth data associated with the image.
- [var semanticSegmentationMatte: AVSemanticSegmentationMatte?](./semanticsegmentationmatte.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/portraiteffectsmatte)*