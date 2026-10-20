# init(propertiesOf:prototypeInstruction:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a mutable video composition with the specified asset properties and a prototype video composition instruction.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0
- iPadOS 13.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.15+ - Deprecated in 15.0
- tvOS 13.0+ - Deprecated in 18.0

> **Deprecated**: Use videoCompositionWithPropertiesOfAsset:prototypeInstruction:completionHandler: instead

## Declaration

```swift
init(propertiesOf asset: AVAsset, prototypeInstruction: AVVideoCompositionInstruction)
```

```objc
+ (AVMutableVideoComposition *) videoCompositionWithPropertiesOfAsset:(AVAsset *) asset prototypeInstruction:(AVVideoCompositionInstruction *) prototypeInstruction;
```

## Parameters

- `asset`: The asset for which to create a video composition. Load the asset’s [`duration`](../avasset/duration.md) and [`tracks`](../avasset/tracks.md) properties before invoking this method.
- `prototypeInstruction`: A video composition instruction to use as a prototype.

## See Also

### Creating a video composition
- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](./videocomposition%28withpropertiesof,completionhandler%29.md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [class func videoComposition(withPropertiesOf: AVAsset, prototypeInstruction: AVVideoCompositionInstruction, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](./videocomposition%28withpropertiesof,prototypeinstruction,completionhandler%29.md)
  Returns a new mutable video composition with the specified asset properties and a prototype video composition instruction.
- [class func videoComposition(with: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](./videocomposition%28with,applyingcifilterswithhandler,completionhandler%29.md)
  Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [init(propertiesOf: AVAsset)](./init%28propertiesof%29.md)
  Creates a mutable video composition with the specified asset properties.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](./init%28asset,applyingcifilterswithhandler%29.md)
  Creates a mutable video composition configured to apply Core Image filters to each video frame of the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/init(propertiesof:prototypeinstruction:))*