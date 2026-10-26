# videoCompositionWithVideoComposition:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Pass-through initializer, for internal use in AVFoundation only

## Declaration

```objc
+ (AVVideoComposition *) videoCompositionWithVideoComposition:(AVVideoComposition *) videoComposition;
```

## See Also

### Creating a video composition
- [class func videoComposition(with: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: (AVVideoComposition?, (any Error)?) -> Void)](./videocomposition%28with,applyingcifilterswithhandler,completionhandler%29.md)
  Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [class AVAsynchronousCIImageFilteringRequest](../avasynchronousciimagefilteringrequest.md)
  An object that supports using Core Image filters to process an individual video frame in a video composition.
- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVVideoComposition?, (any Error)?) -> Void)](./videocomposition%28withpropertiesof,completionhandler%29.md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [init(propertiesOf: AVAsset)](./init%28propertiesof%29.md)
  Creates a video composition object configured to present the video tracks of the specified asset.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](./init%28asset,applyingcifilterswithhandler%29.md)
  Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/videocompositionwithvideocomposition:)*