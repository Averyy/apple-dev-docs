# pixelBuffer

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The CoreVideo pixel buffer this image was created from, if applicable.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var pixelBuffer: CVPixelBuffer? { get }
```

```objc
@property (nonatomic, readonly, nullable) CVPixelBufferRef pixelBuffer;
```

## Discussion

If this image was create using the [`init(cvPixelBuffer:)`](./init%28cvpixelbuffer%29-3wng7.md) initializer, this property’s value is the [`CVPixelBuffer`](../../CoreVideo/cvpixelbuffer.md) object that provides the image’s underlying image data. Do not modify the contents of this pixel buffer; doing so will cause undefined rendering results.

Otherwise, this property’s value is `nil`—in this case you can obtain a pixel buffer by rendering the image with the [`CIContext`](../cicontext.md) [`render(_:to:)`](../cicontext/render%28_,to%29.md) method.

## See Also

### Accessing Original Image Content
- [var cgImage: CGImage?](./cgimage.md)
  The CoreGraphics image object this image was created from, if applicable.
- [var depthData: AVDepthData?](./depthdata.md)
  Depth data associated with the image.
- [var portraitEffectsMatte: AVPortraitEffectsMatte?](./portraiteffectsmatte.md)
  The portrait effects matte associated with the image.
- [var semanticSegmentationMatte: AVSemanticSegmentationMatte?](./semanticsegmentationmatte.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/pixelbuffer)*