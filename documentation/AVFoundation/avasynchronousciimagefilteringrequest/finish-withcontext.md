# finish(with:context:)

**Framework**: AVFoundation  
**Kind**: method

Provides the filtered video frame image to AVFoundation for further processing or display.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func finish(with filteredImage: CIImage, context: CIContext?)
```

#### Discussion

Call this method when your handler block has finished applying filters, passing the [`outputImage`](https://developer.apple.com/documentation/coreimage/cifilter/1438169-outputimage) object from the final filter in your filter chain for the `filteredImage` parameter. The pixel format for this image must be the [`BGRA8`](https://developer.apple.com/documentation/coreimage/ciformat/1438064-bgra8) format (of the [`kCVPixelFormatType_32BGRA`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_32BGRA) type).

You can pass the [`sourceImage`](avasynchronousciimagefilteringrequest/sourceimage.md) object to the `filteredImage` parameter to disable filtering for the current frame.

By default, you can pass `nil` for the `context` parameter to use a default rendering context provided by Core Image. In iOS and tvOS, the default context uses the Device RGB color space. In macOS, the default context uses the sRGB color space. AVFoundation automatically uses a GPU-accelerated context if possible. To use a different color space or control other rendering options, pass your own [`CIContext`](https://developer.apple.com/documentation/coreimage/cicontext) object instead.

> ❗ **Important**:  A [`CIContext`](https://developer.apple.com/documentation/coreimage/cicontext) instance is a heavyweight object that maintains expensive rendering state. Don’t create a new context object in the block where you call this method (which runs once per video frame); instead, create a [`CIContext`](https://developer.apple.com/documentation/coreimage/cicontext) instance before create a composition with the [`init(asset:applyingCIFiltersWithHandler:)`](avvideocomposition/init(asset:applyingcifilterswithhandler:).md) method, and use that instance in your handler block.

 A [`CIContext`](https://developer.apple.com/documentation/coreimage/cicontext) instance is a heavyweight object that maintains expensive rendering state. Don’t create a new context object in the block where you call this method (which runs once per video frame); instead, create a [`CIContext`](https://developer.apple.com/documentation/coreimage/cicontext) instance before create a composition with the [`init(asset:applyingCIFiltersWithHandler:)`](avvideocomposition/init(asset:applyingcifilterswithhandler:).md) method, and use that instance in your handler block.

## Parameters

- `filteredImage`: A Core Image image representing the output of whatever filters you’ve applied to the source image.
- `context`: A Core Image context to be used for rendering the output image, or   to use a default context provided by AVFoundation.

## See Also

- [func finish(with: any Error)](avasynchronousciimagefilteringrequest/finish(with:).md)
  Notifies AVFoundation that you cannot fulfill the image filtering request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/finish(with:context:))*