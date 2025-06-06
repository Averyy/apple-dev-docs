# init(propertiesOf:)

**Framework**: AVFoundation  
**Kind**: init

Creates a mutable video composition with the specified asset properties.

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

#### Discussion

The returned `AVMutableVideoComposition` has instructions that respect the spatial properties and time ranges of the specified asset’s video tracks.

It also has the following values for its properties:

- A value for [`frameDuration`](avmutablevideocomposition/frameduration.md) short enough to accommodate the greatest [`nominalFrameRate`](avassettrack/nominalframerate.md) among the asset’s video tracks. If the [`nominalFrameRate`](avassettrack/nominalframerate.md) of all of the asset’s video tracks is 0, a default frame rate of 30fps is used.
- If the specified asset is an instance of [`AVComposition`](avcomposition.md), the [`renderSize`](avmutablevideocomposition/rendersize.md) is set to the [`naturalSize`](avcomposition/naturalsize.md) of the [`AVComposition`](avcomposition.md); otherwise the [`renderSize`](avmutablevideocomposition/rendersize.md) will be set to a value that encompasses all of the asset’s video tracks.
- A [`renderScale`](avmutablevideocomposition/renderscale.md) of 1.0.
- The [`animationTool`](avmutablevideocomposition/animationtool.md) property set to `nil`.

## Parameters

- `asset`: An instance of  . Ensure that the duration and tracks properties of the asset are already loaded before invoking this method.

## See Also

- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](avmutablevideocomposition/videocomposition(withpropertiesof:completionhandler:).md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [class func videoComposition(withPropertiesOf: AVAsset, prototypeInstruction: AVVideoCompositionInstruction, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](avmutablevideocomposition/videocomposition(withpropertiesof:prototypeinstruction:completionhandler:).md)
  Returns a new mutable video composition with the specified asset properties and a prototype video composition instruction.
- [class func videoComposition(with: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](avmutablevideocomposition/videocomposition(with:applyingcifilterswithhandler:completionhandler:).md)
  Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [init(propertiesOf: AVAsset, prototypeInstruction: AVVideoCompositionInstruction)](avmutablevideocomposition/init(propertiesof:prototypeinstruction:).md)
  Creates a mutable video composition with the specified asset properties and a prototype video composition instruction.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](avmutablevideocomposition/init(asset:applyingcifilterswithhandler:).md)
  Creates a mutable video composition configured to apply Core Image filters to each video frame of the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/init(propertiesof:))*