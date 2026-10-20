# sourceImage

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The current video frame image.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.11+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVCIImageFilteringParameters instead

## Declaration

```swift
var sourceImage: CIImage { get }
```

```objc
@property (nonatomic, readonly) CIImage * sourceImage;
```

#### Discussion

To apply a Core Image filter to this image, assign it to the `inputImage` parameter of a [`CIFilter`](../../CoreImage/cifilter-swift.class.md) object, or use a [`CIImage`](../../CoreImage/ciimage.md) convenience method such as the [`applyingFilter(_:parameters:)`](../../CoreImage/ciimage/applyingfilter%28_,parameters%29.md) method.

The pixel format for this image is the [`BGRA8`](../../CoreImage/ciformat/bgra8.md) format (of the [`kCVPixelFormatType_32BGRA`](../../CoreVideo/kcvpixelformattype_32bgra.md) type). Unlike when processing video with the [`AVAsynchronousVideoCompositionRequest`](../avasynchronousvideocompositionrequest.md) class, the [`renderContext`](../avasynchronousvideocompositionrequest/rendercontext.md) object’s [`renderTransform`](../avvideocompositionrendercontext/rendertransform.md) property is already applied to this image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/sourceimage)*