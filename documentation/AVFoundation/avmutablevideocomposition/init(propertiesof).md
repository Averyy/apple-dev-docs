# init(propertiesOf:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a mutable video composition with the specified asset properties.

**Availability**:
- iOS 6.0+ - Deprecated in 18.0
- iPadOS 6.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.9+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Use videoCompositionWithPropertiesOfAsset:completionHandler: instead

## Declaration

```swift
init(propertiesOf asset: AVAsset)
```

```objc
+ (AVMutableVideoComposition *) videoCompositionWithPropertiesOfAsset:(AVAsset *) asset;
```

#### Discussion

The returned `AVMutableVideoComposition` has instructions that respect the spatial properties and time ranges of the specified asset’s video tracks.

It also has the following values for its properties:

- A value for [`frameDuration`](./frameduration.md) short enough to accommodate the greatest [`nominalFrameRate`](../avassettrack/nominalframerate.md) among the asset’s video tracks. If the [`nominalFrameRate`](../avassettrack/nominalframerate.md) of all of the asset’s video tracks is 0, a default frame rate of 30fps is used.
- If the specified asset is an instance of [`AVComposition`](../avcomposition.md), the [`renderSize`](./rendersize.md) is set to the [`naturalSize`](../avcomposition/naturalsize.md) of the [`AVComposition`](../avcomposition.md); otherwise the [`renderSize`](./rendersize.md) will be set to a value that encompasses all of the asset’s video tracks.
- A [`renderScale`](./renderscale.md) of 1.0.
- The [`animationTool`](./animationtool.md) property set to `nil`.

## Parameters

- `asset`: An instance of [`AVAsset`](../avasset.md). Ensure that the duration and tracks properties of the asset are already loaded before invoking this method.

## See Also

### Creating a video composition
- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](./videocomposition%28withpropertiesof,completionhandler%29.md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [class func videoComposition(withPropertiesOf: AVAsset, prototypeInstruction: AVVideoCompositionInstruction, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](./videocomposition%28withpropertiesof,prototypeinstruction,completionhandler%29.md)
  Returns a new mutable video composition with the specified asset properties and a prototype video composition instruction.
- [class func videoComposition(with: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](./videocomposition%28with,applyingcifilterswithhandler,completionhandler%29.md)
  Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [init(propertiesOf: AVAsset, prototypeInstruction: AVVideoCompositionInstruction)](./init%28propertiesof,prototypeinstruction%29.md)
  Creates a mutable video composition with the specified asset properties and a prototype video composition instruction.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](./init%28asset,applyingcifilterswithhandler%29.md)
  Creates a mutable video composition configured to apply Core Image filters to each video frame of the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/init(propertiesof:))*