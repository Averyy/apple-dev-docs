# videoComposition(with:applyingCIFiltersWithHandler:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class func videoComposition(with asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping (AVAsynchronousCIImageFilteringRequest) -> Void) async throws -> AVVideoComposition
```

#### Discussion

The composition calls the specified handler one time for each frame to display (or processed for export) from the asset’s first enabled video track. In that block, you access the video frame and return a filtered result using the provided [`AVAsynchronousCIImageFilteringRequest`](avasynchronousciimagefilteringrequest.md) object. Use that object’s [`sourceImage`](avasynchronousciimagefilteringrequest/sourceimage.md) property to get the video frame in the form of a [`CIImage`](https://developer.apple.com/documentation/coreimage/ciimage) object you can apply filters to. Pass the result of your filters to the `request` object’s [`finish(with:context:)`](avasynchronousciimagefilteringrequest/finish(with:context:).md) method. (If your filter rendering fails, call the `request` object’s [`finish(with:)`](avasynchronousciimagefilteringrequest/finish(with:).md) method if you can’t apply filters).

```swift
guard let filter = CIFilter(name: "CIGaussianBlur") else { return }
let composition = try await AVVideoComposition.videoComposition(with: asset) { request in
    // Clamp to avoid blurring transparent pixels at the image edges.
    let source = request.sourceImage.clampedToExtent()
    filter.setValue(source, forKey: kCIInputImageKey)
            
    // Vary filter parameters based on the video timing.
    let seconds = CMTimeGetSeconds(request.compositionTime)
    filter.setValue(seconds * 10.0, forKey: kCIInputRadiusKey)
            
    // Crop the blurred output to the bounds of the original image.
    if let output = filter.outputImage?.cropped(to: request.sourceImage.extent) {
        request.finish(with: output, context: nil)
    } else {
        request.finish(with: AppError.customError)
    }
}
```

Creating a composition with this method sets values for the following properties:

- The value of the [`frameDuration`](avvideocomposition/frameduration.md) property accommodates the [`nominalFrameRate`](avassettrack/nominalframerate.md) value for the asset’s first enabled video track. If the nominal frame rate is zero, AVFoundation uses a default frame rate of 30 fps.
- The [`renderSize`](avvideocomposition/rendersize.md) property value a size that encompasses the asset’s first enabled video track, respecting the track’s [`preferredTransform`](avassettrack/preferredtransform.md) property.
- The [`renderScale`](avvideocomposition/renderscale.md) property value is `1.0`.

## Parameters

- `asset`: The asset whose configuration matches the intended use of the video composition.
- `applier`: The block takes a single parameter and has no return value:
- `completionHandler`: A block the system calls when it finishes creating the new video composition.

## See Also

- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVVideoComposition?, (any Error)?) -> Void)](avvideocomposition/videocomposition(withpropertiesof:completionhandler:).md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [class AVAsynchronousCIImageFilteringRequest](avasynchronousciimagefilteringrequest.md)
  An object that supports using Core Image filters to process an individual video frame in a video composition.
- [init(propertiesOf: AVAsset)](avvideocomposition/init(propertiesof:).md)
  Creates a video composition object configured to present the video tracks of the specified asset.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](avvideocomposition/init(asset:applyingcifilterswithhandler:).md)
  Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/videocomposition(with:applyingcifilterswithhandler:completionhandler:))*