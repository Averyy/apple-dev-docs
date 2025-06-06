# videoComposition(withPropertiesOf:prototypeInstruction:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Returns a new mutable video composition with the specified asset properties and a prototype video composition instruction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class func videoComposition(withPropertiesOf asset: AVAsset, prototypeInstruction: AVVideoCompositionInstruction) async throws -> AVMutableVideoComposition
```

## Parameters

- `asset`: The asset for which to create a video composition. Load the asset’s   and   properties before invoking this method.
- `prototypeInstruction`: A video composition instruction to use as a prototype.
- `completionHandler`: A block the system calls when it finishes creating the new video composition.

## See Also

- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](avmutablevideocomposition/videocomposition(withpropertiesof:completionhandler:).md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [class func videoComposition(with: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](avmutablevideocomposition/videocomposition(with:applyingcifilterswithhandler:completionhandler:).md)
  Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [init(propertiesOf: AVAsset)](avmutablevideocomposition/init(propertiesof:).md)
  Creates a mutable video composition with the specified asset properties.
- [init(propertiesOf: AVAsset, prototypeInstruction: AVVideoCompositionInstruction)](avmutablevideocomposition/init(propertiesof:prototypeinstruction:).md)
  Creates a mutable video composition with the specified asset properties and a prototype video composition instruction.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](avmutablevideocomposition/init(asset:applyingcifilterswithhandler:).md)
  Creates a mutable video composition configured to apply Core Image filters to each video frame of the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/videocomposition(withpropertiesof:prototypeinstruction:completionhandler:))*