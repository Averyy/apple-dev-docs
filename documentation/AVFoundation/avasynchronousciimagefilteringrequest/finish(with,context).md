# finish(with:context:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Provides the filtered video frame image to AVFoundation for further processing or display.

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
func finish(with filteredImage: CIImage, context: CIContext?)
```

```objc
- (void) finishWithImage:(CIImage *) filteredImage context:(CIContext *) context;
```

## Discussion

Call this method when your handler block has finished applying filters, passing the [`outputImage`](../../CoreImage/cifilter-swift.class/outputimage.md) object from the final filter in your filter chain for the `filteredImage` parameter. The pixel format for this image must be the [`BGRA8`](../../CoreImage/ciformat/bgra8.md) format (of the [`kCVPixelFormatType_32BGRA`](../../CoreVideo/kcvpixelformattype_32bgra.md) type).

You can pass the [`sourceImage`](./sourceimage.md) object to the `filteredImage` parameter to disable filtering for the current frame.

By default, you can pass `nil` for the `context` parameter to use a default rendering context provided by Core Image. In iOS and tvOS, the default context uses the Device RGB color space. In macOS, the default context uses the sRGB color space. AVFoundation automatically uses a GPU-accelerated context if possible. To use a different color space or control other rendering options, pass your own [`CIContext`](../../CoreImage/cicontext.md) object instead.

> ❗ **Important**:  A [`CIContext`](../../CoreImage/cicontext.md) instance is a heavyweight object that maintains expensive rendering state. Don’t create a new context object in the block where you call this method (which runs once per video frame); instead, create a [`CIContext`](../../CoreImage/cicontext.md) instance before create a composition with the [`init(asset:applyingCIFiltersWithHandler:)`](../avvideocomposition/init%28asset,applyingcifilterswithhandler%29.md) method, and use that instance in your handler block.

## Parameters

- `filteredImage`: A Core Image image representing the output of whatever filters you’ve applied to the source image.
- `context`: A Core Image context to be used for rendering the output image, or `nil` to use a default context provided by AVFoundation.

## See Also

### Returning the filtered image
- [func finish(with: any Error)](./finish%28with%29.md)
  Notifies AVFoundation that you cannot fulfill the image filtering request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/finish(with:context:))*