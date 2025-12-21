# AVCIImageFilteringResult

**Framework**: AVFoundation  
**Kind**: struct

An output video frame processed with Core Image filtering.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct AVCIImageFilteringResult
```

## Topics

### Creating a result
- [init(resultImage: CIImage, ciContext: CIContext?)](avciimagefilteringresult/init(resultimage:cicontext:).md)
### Inspecting the result
- [let ciContext: CIContext?](avciimagefilteringresult/cicontext.md)
  The core image context used to render the image
- [let resultImage: CIImage](avciimagefilteringresult/resultimage.md)
  Provides the filtered video frame image to AVFoundation for further processing or display.

## See Also

- [convenience init(configuration: AVVideoComposition.Configuration)](avvideocomposition/init(configuration:).md)
  Initialize an AVVideoComposition with a configuration.
- [AVVideoComposition.Configuration](avvideocomposition/configuration.md)
  Configurable properties for initializing a new AVVideoComposition instance.
- [convenience init(applyingFiltersTo: AVAsset, applier: (AVCIImageFilteringParameters) async throws -> AVCIImageFilteringResult) async throws](avvideocomposition/init(applyingfiltersto:applier:).md)
  Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.
- [class func videoComposition(with: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: (AVVideoComposition?, (any Error)?) -> Void)](avvideocomposition/videocomposition(with:applyingcifilterswithhandler:completionhandler:).md)
  Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [class AVAsynchronousCIImageFilteringRequest](avasynchronousciimagefilteringrequest.md)
  An object that supports using Core Image filters to process an individual video frame in a video composition.
- [struct AVCIImageFilteringParameters](avciimagefilteringparameters.md)
- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVVideoComposition?, (any Error)?) -> Void)](avvideocomposition/videocomposition(withpropertiesof:completionhandler:).md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [init(propertiesOf: AVAsset)](avvideocomposition/init(propertiesof:).md)
  Creates a video composition object configured to present the video tracks of the specified asset.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](avvideocomposition/init(asset:applyingcifilterswithhandler:).md)
  Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avciimagefilteringresult)*