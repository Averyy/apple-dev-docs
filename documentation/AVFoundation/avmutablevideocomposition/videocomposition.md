# videoComposition

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Creates a new mutable video composition.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (AVMutableVideoComposition *) videoComposition;
```

#### Return Value

A newly created and initialized instance of `AVMutableVideoComposition`.

#### Discussion

The returned `AVMutableVideoComposition` has the following properties:

- A [`frameDuration`](./frameduration.md) of [`zero`](../../CoreMedia/cmtime/zero.md).
- A [`renderSize`](./rendersize.md) of `{0.0, 0.0}`.
- A `nil` array of [`instructions`](./instructions.md).
- The [`animationTool`](./animationtool.md) property set to `nil`.

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
- [init(propertiesOf: AVAsset, prototypeInstruction: AVVideoCompositionInstruction)](./init%28propertiesof,prototypeinstruction%29.md)
  Creates a mutable video composition with the specified asset properties and a prototype video composition instruction.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](./init%28asset,applyingcifilterswithhandler%29.md)
  Creates a mutable video composition configured to apply Core Image filters to each video frame of the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/videocomposition)*