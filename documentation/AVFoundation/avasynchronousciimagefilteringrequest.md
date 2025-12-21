# AVAsynchronousCIImageFilteringRequest

**Framework**: AVFoundation  
**Kind**: class

An object that supports using Core Image filters to process an individual video frame in a video composition.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAsynchronousCIImageFilteringRequest
```

#### Overview

You use this class when creating a composition for Core Image filtering with the [`init(asset:applyingCIFiltersWithHandler:)`](avvideocomposition/init(asset:applyingcifilterswithhandler:).md) method. In that method call, you provide a block to be called by AVFoundation as it processes each frame of video, and the block’s sole parameter is a [`AVAsynchronousCIImageFilteringRequest`](avasynchronousciimagefilteringrequest.md) object. Use that object both to the video frame image to be filtered and allows you to return a filtered image to AVFoundation for display or export. The code listing below shows an example of applying a filter to an asset.

> 💡 **Tip**:  To use the created video composition for playback, create an [`AVPlayerItem`](avplayeritem.md) object from the same asset used as the composition’s source, then assign the composition to the player item’s [`videoComposition`](avplayeritem/videocomposition.md) property. To export the composition to a new movie file, create an [`AVAssetExportSession`](avassetexportsession.md) object from the same source asset, then assign the composition to the export session’s [`videoComposition`](avassetexportsession/videocomposition.md) property.

## Topics

### Getting the image to be filtered
- [var sourceImage: CIImage](avasynchronousciimagefilteringrequest/sourceimage.md)
  The current video frame image.
### Getting contextual information for filtering
- [var compositionTime: CMTime](avasynchronousciimagefilteringrequest/compositiontime.md)
  The time in the video composition corresponding to the frame being processed.
- [var renderSize: CGSize](avasynchronousciimagefilteringrequest/rendersize.md)
  The width and height, in pixels, of the frame being processed.
### Returning the filtered image
- [func finish(with: CIImage, context: CIContext?)](avasynchronousciimagefilteringrequest/finish(with:context:).md)
  Provides the filtered video frame image to AVFoundation for further processing or display.
- [func finish(with: any Error)](avasynchronousciimagefilteringrequest/finish(with:).md)
  Notifies AVFoundation that you cannot fulfill the image filtering request.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [convenience init(configuration: AVVideoComposition.Configuration)](avvideocomposition/init(configuration:).md)
  Initialize an AVVideoComposition with a configuration.
- [AVVideoComposition.Configuration](avvideocomposition/configuration.md)
  Configurable properties for initializing a new AVVideoComposition instance.
- [convenience init(applyingFiltersTo: AVAsset, applier: (AVCIImageFilteringParameters) async throws -> AVCIImageFilteringResult) async throws](avvideocomposition/init(applyingfiltersto:applier:).md)
  Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.
- [class func videoComposition(with: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: (AVVideoComposition?, (any Error)?) -> Void)](avvideocomposition/videocomposition(with:applyingcifilterswithhandler:completionhandler:).md)
  Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [struct AVCIImageFilteringParameters](avciimagefilteringparameters.md)
- [struct AVCIImageFilteringResult](avciimagefilteringresult.md)
  An output video frame processed with Core Image filtering.
- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVVideoComposition?, (any Error)?) -> Void)](avvideocomposition/videocomposition(withpropertiesof:completionhandler:).md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [init(propertiesOf: AVAsset)](avvideocomposition/init(propertiesof:).md)
  Creates a video composition object configured to present the video tracks of the specified asset.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](avvideocomposition/init(asset:applyingcifilterswithhandler:).md)
  Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest)*