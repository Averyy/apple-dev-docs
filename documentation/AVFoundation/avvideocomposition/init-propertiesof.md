# init(propertiesOf:)

**Framework**: AVFoundation  
**Kind**: init

Creates a video composition object configured to present the video tracks of the specified asset.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+

## Declaration

```swift
init(propertiesOf asset: AVAsset)
```

#### Return Value

A new video composition object.

#### Discussion

Apple discourages using this method in iOS 16, tvOS 16, and macOS 13 or later. Create a video composition asynchronously using [`videoComposition(withPropertiesOf:completionHandler:)`](avvideocomposition/videocomposition(withpropertiesof:completionhandler:).md) instead.

This method creates the video composition object and configures it with the values and instructions suitable for presenting the video tracks of the specified asset. The returned object contains instructions that respect the spatial properties and time ranges of the specified asset’s video tracks. It also configures the object properties in the following way:

- The value of the [`frameDuration`](avvideocomposition/frameduration.md) property is short enough to accommodate the greatest nominal frame rate value among the asset’s video tracks, as indicated by the [`nominalFrameRate`](avpartialasyncproperty/nominalframerate.md) property of each track. If all its tracks have a nominal frame rate of `0`, it uses a frame rate of 30 frames per second, with the frame duration set accordingly.
- The value of the [`renderSize`](avvideocomposition/rendersize.md) property depends on whether the asset is an [`AVComposition`](avcomposition.md) object. For an [`AVComposition`](avcomposition.md), the render size is the composition’s [`naturalSize`](avcomposition/naturalsize.md) value, and for other assets, its a size large enough to encompass all of its video tracks.
- The value of the [`renderScale`](avvideocomposition/renderscale.md) property is `1.0`.
- The value of the [`animationTool`](avvideocomposition/animationtool.md) property is `nil`.

> **Note**:  If you specify an asset that doesn’t contain video tracks, this method returns a video composition with no instructions.

## Parameters

- `asset`: The asset whose configuration matches the intended use of the video composition.

## See Also

- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVVideoComposition?, (any Error)?) -> Void)](avvideocomposition/videocomposition(withpropertiesof:completionhandler:).md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [class func videoComposition(with: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: (AVVideoComposition?, (any Error)?) -> Void)](avvideocomposition/videocomposition(with:applyingcifilterswithhandler:completionhandler:).md)
  Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [class AVAsynchronousCIImageFilteringRequest](avasynchronousciimagefilteringrequest.md)
  An object that supports using Core Image filters to process an individual video frame in a video composition.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](avvideocomposition/init(asset:applyingcifilterswithhandler:).md)
  Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/init(propertiesof:))*