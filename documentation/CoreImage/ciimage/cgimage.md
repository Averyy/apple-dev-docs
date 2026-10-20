# cgImage

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The CoreGraphics image object this image was created from, if applicable.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var cgImage: CGImage? { get }
```

```objc
@property (nonatomic, readonly, nullable) CGImageRef CGImage;
```

#### Discussion

If this image was created using the [`init(cgImage:)`](./init%28cgimage%29-2kvvb.md) or [`init(contentsOf:)`](./init%28contentsof%29.md) initializer, this property’s value is the [`CGImage`](../../CoreGraphics/cgimage.md) object that provides the image’s underlying image data. Otherwise, this property’s value is `nil`—in this case you can obtain a CoreGraphics image by rendering the image with the [`CIContext`](../cicontext.md) [`createCGImage(_:from:)`](../cicontext/createcgimage%28_,from%29.md) method.

## See Also

### Accessing Original Image Content
- [var pixelBuffer: CVPixelBuffer?](./pixelbuffer.md)
  The CoreVideo pixel buffer this image was created from, if applicable.
- [var depthData: AVDepthData?](./depthdata.md)
  Depth data associated with the image.
- [var portraitEffectsMatte: AVPortraitEffectsMatte?](./portraiteffectsmatte.md)
  The portrait effects matte associated with the image.
- [var semanticSegmentationMatte: AVSemanticSegmentationMatte?](./semanticsegmentationmatte.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/cgimage)*