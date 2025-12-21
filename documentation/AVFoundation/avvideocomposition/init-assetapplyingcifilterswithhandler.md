# init(asset:applyingCIFiltersWithHandler:)

**Framework**: AVFoundation  
**Kind**: init

Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+

## Declaration

```swift
init(asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping (AVAsynchronousCIImageFilteringRequest) -> Void)
```

#### Return Value

A new video composition object.

#### Discussion

Apple discourages using this method in iOS 16, tvOS 16, and macOS 13 or later. Create a video composition asynchronously using [`videoComposition(with:applyingCIFiltersWithHandler:completionHandler:)`](avvideocomposition/videocomposition(with:applyingcifilterswithhandler:completionhandler:).md) instead.

To process video frames using Core Image filters—whether for display or export—create a composition with this method. AVFoundation calls your applier block one time for each frame to display (or processed for export) from the asset’s first enabled video track. In that block, you access the video frame and return a filtered result using the provided [`AVAsynchronousCIImageFilteringRequest`](avasynchronousciimagefilteringrequest.md) object. Use that object’s [`sourceImage`](avasynchronousciimagefilteringrequest/sourceimage.md) property to get the video frame in the form of a [`CIImage`](https://developer.apple.com/documentation/CoreImage/CIImage) object you can apply filters to. Pass the result of your filters to the `request` object’s [`finish(with:context:)`](avasynchronousciimagefilteringrequest/finish(with:context:).md) method. (If your filter rendering fails, call the `request` object’s [`finish(with:)`](avasynchronousciimagefilteringrequest/finish(with:).md) method if you can’t apply filters).

Creating a composition with this method sets values for the following properties:

- The value of the [`frameDuration`](avvideocomposition/frameduration.md) property accommodates the [`nominalFrameRate`](avassettrack/nominalframerate.md) value for the asset’s first enabled video track. If the nominal frame rate is zero, AVFoundation uses a default frame rate of 30 fps.
- The [`renderSize`](avvideocomposition/rendersize.md) property value a size that encompasses the asset’s first enabled video track, respecting the track’s [`preferredTransform`](avassettrack/preferredtransform.md) property.
- The [`renderScale`](avvideocomposition/renderscale.md) property value is `1.0`.

## Parameters

- `asset`: The asset whose configuration matches the intended use of the video composition.
- `applier`: The block takes a single parameter and has no return value:

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
- [struct AVCIImageFilteringResult](avciimagefilteringresult.md)
  An output video frame processed with Core Image filtering.
- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVVideoComposition?, (any Error)?) -> Void)](avvideocomposition/videocomposition(withpropertiesof:completionhandler:).md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [init(propertiesOf: AVAsset)](avvideocomposition/init(propertiesof:).md)
  Creates a video composition object configured to present the video tracks of the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/init(asset:applyingcifilterswithhandler:))*