# videoComposition(withPropertiesOf:prototypeInstruction:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new mutable video composition with the specified asset properties and a prototype video composition instruction.

**Availability**:
- iOS 16.0+ - Deprecated in 26.0
- iPadOS 16.0+ - Deprecated in 26.0
- Mac Catalyst 16.0+ - Deprecated in 26.0
- macOS 13.0+ - Deprecated in 26.0
- tvOS 16.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
class func videoComposition(withPropertiesOf asset: AVAsset, prototypeInstruction: AVVideoCompositionInstruction, completionHandler: @escaping @Sendable (AVMutableVideoComposition?, (any Error)?) -> Void)
```

```swift
class func videoComposition(withPropertiesOf asset: AVAsset, prototypeInstruction: AVVideoCompositionInstruction) async throws -> AVMutableVideoComposition
```

```objc
+ (void) videoCompositionWithPropertiesOfAsset:(AVAsset *) asset prototypeInstruction:(AVVideoCompositionInstruction *) prototypeInstruction completionHandler:(void (^)(AVMutableVideoComposition *videoComposition, NSError *error)) completionHandler;
```

## Parameters

- `asset`: The asset for which to create a video composition. Load the asset’s [`duration`](../avasset/duration.md) and [`tracks`](../avasset/tracks.md) properties before invoking this method.
- `prototypeInstruction`: A video composition instruction to use as a prototype.
- `completionHandler`: A block the system calls when it finishes creating the new video composition.

## See Also

### Creating a video composition
- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](./videocomposition%28withpropertiesof,completionhandler%29.md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [class func videoComposition(with: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](./videocomposition%28with,applyingcifilterswithhandler,completionhandler%29.md)
  Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [init(propertiesOf: AVAsset)](./init%28propertiesof%29.md)
  Creates a mutable video composition with the specified asset properties.
- [init(propertiesOf: AVAsset, prototypeInstruction: AVVideoCompositionInstruction)](./init%28propertiesof,prototypeinstruction%29.md)
  Creates a mutable video composition with the specified asset properties and a prototype video composition instruction.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](./init%28asset,applyingcifilterswithhandler%29.md)
  Creates a mutable video composition configured to apply Core Image filters to each video frame of the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/videocomposition(withpropertiesof:prototypeinstruction:completionhandler:))*