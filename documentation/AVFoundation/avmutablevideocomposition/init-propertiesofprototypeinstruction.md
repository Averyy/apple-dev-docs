# init(propertiesOf:prototypeInstruction:)

**Framework**: AVFoundation  
**Kind**: init

Creates a mutable video composition with the specified asset properties and a prototype video composition instruction.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+

## Declaration

```swift
init(propertiesOf asset: AVAsset, prototypeInstruction: AVVideoCompositionInstruction)
```

## Parameters

- `asset`: The asset for which to create a video composition. Load the asset’s   and   properties before invoking this method.
- `prototypeInstruction`: A video composition instruction to use as a prototype.

## See Also

- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](avmutablevideocomposition/videocomposition(withpropertiesof:completionhandler:).md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [class func videoComposition(withPropertiesOf: AVAsset, prototypeInstruction: AVVideoCompositionInstruction, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](avmutablevideocomposition/videocomposition(withpropertiesof:prototypeinstruction:completionhandler:).md)
  Returns a new mutable video composition with the specified asset properties and a prototype video composition instruction.
- [class func videoComposition(with: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](avmutablevideocomposition/videocomposition(with:applyingcifilterswithhandler:completionhandler:).md)
  Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [init(propertiesOf: AVAsset)](avmutablevideocomposition/init(propertiesof:).md)
  Creates a mutable video composition with the specified asset properties.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](avmutablevideocomposition/init(asset:applyingcifilterswithhandler:).md)
  Creates a mutable video composition configured to apply Core Image filters to each video frame of the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/init(propertiesof:prototypeinstruction:))*