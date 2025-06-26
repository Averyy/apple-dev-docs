# sourceImage

**Framework**: AVFoundation  
**Kind**: property

The current video frame image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sourceImage: CIImage { get }
```

#### Discussion

To apply a Core Image filter to this image, assign it to the `inputImage` parameter of a [`CIFilter`](https://developer.apple.com/documentation/CoreImage/CIFilter-swift.class) object, or use a [`CIImage`](https://developer.apple.com/documentation/CoreImage/CIImage) convenience method such as the [`applyingFilter(_:parameters:)`](https://developer.apple.com/documentation/CoreImage/CIImage/applyingFilter(_:parameters:)) method.

The pixel format for this image is the [`BGRA8`](https://developer.apple.com/documentation/CoreImage/CIFormat/BGRA8) format (of the [`kCVPixelFormatType_32BGRA`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_32BGRA) type). Unlike when processing video with the [`AVAsynchronousVideoCompositionRequest`](avasynchronousvideocompositionrequest.md) class, the [`renderContext`](avasynchronousvideocompositionrequest/rendercontext.md) object’s [`renderTransform`](avvideocompositionrendercontext/rendertransform.md) property is already applied to this image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/sourceimage)*