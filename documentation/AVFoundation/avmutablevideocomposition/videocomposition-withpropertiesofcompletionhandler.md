# videoComposition(withPropertiesOf:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Returns a new video composition that’s configured to present the video tracks of the specified asset.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class func videoComposition(withPropertiesOf asset: AVAsset) async throws -> AVMutableVideoComposition
```

#### Discussion

This method creates the video composition object and configures it with the values and instructions suitable for presenting the video tracks of the specified asset. The returned object contains instructions that respect the spatial properties and time ranges of the specified asset’s video tracks. It also configures the object properties in the following way:

- The value of the [`frameDuration`](avvideocomposition/frameduration.md) property is short enough to accommodate the greatest nominal frame rate value among the asset’s video tracks, as indicated by the [`nominalFrameRate`](avpartialasyncproperty/nominalframerate.md) property of each track. If all its tracks have a nominal frame rate of `0`, it uses a frame rate of 30 frames per second, with the frame duration set accordingly.
- The value of the [`renderSize`](avvideocomposition/rendersize.md) property depends on whether the asset is an [`AVComposition`](avcomposition.md) object. For an [`AVComposition`](avcomposition.md), the render size is the composition’s [`naturalSize`](avcomposition/naturalsize.md) value, and for other assets, its a size large enough to encompass all of its video tracks.
- The value of the [`renderScale`](avvideocomposition/renderscale.md) property is `1.0`.
- The value of the [`animationTool`](avvideocomposition/animationtool.md) property is `nil`.

> **Note**:  If you specify an asset that doesn’t contain video tracks, this method returns a video composition with no instructions.

## Parameters

- `asset`: An asset to create a video composition for.
- `completionHandler`: A callback the system invokes with the created video composition, or an error if a failure occurs.

## See Also

- [class func videoComposition(withPropertiesOf: AVAsset, prototypeInstruction: AVVideoCompositionInstruction, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](avmutablevideocomposition/videocomposition(withpropertiesof:prototypeinstruction:completionhandler:).md)
  Returns a new mutable video composition with the specified asset properties and a prototype video composition instruction.
- [class func videoComposition(with: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](avmutablevideocomposition/videocomposition(with:applyingcifilterswithhandler:completionhandler:).md)
  Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [init(propertiesOf: AVAsset)](avmutablevideocomposition/init(propertiesof:).md)
  Creates a mutable video composition with the specified asset properties.
- [init(propertiesOf: AVAsset, prototypeInstruction: AVVideoCompositionInstruction)](avmutablevideocomposition/init(propertiesof:prototypeinstruction:).md)
  Creates a mutable video composition with the specified asset properties and a prototype video composition instruction.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](avmutablevideocomposition/init(asset:applyingcifilterswithhandler:).md)
  Creates a mutable video composition configured to apply Core Image filters to each video frame of the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/videocomposition(withpropertiesof:completionhandler:))*