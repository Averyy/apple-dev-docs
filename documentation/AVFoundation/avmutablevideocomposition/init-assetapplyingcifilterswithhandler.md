# init(asset:applyingCIFiltersWithHandler:)

**Framework**: AVFoundation  
**Kind**: init

Creates a mutable video composition configured to apply Core Image filters to each video frame of the specified asset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+

## Declaration

```swift
init(asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping (AVAsynchronousCIImageFilteringRequest) -> Void)
```

#### Return Value

A new video composition object.

#### Discussion

To process video frames using Core Image filters—whether for display or export—create a composition with this method. AVFoundation calls your applier block once for each frame to be displayed (or processed for export) from the asset’s first enabled video track. In that block, you access the video frame and return a filtered result using the provided [`AVAsynchronousCIImageFilteringRequest`](avasynchronousciimagefilteringrequest.md) object. Use that object’s [`sourceImage`](avasynchronousciimagefilteringrequest/sourceimage.md) property to get the video frame in the form of a CIImage object you can apply filters to. Pass the result of your filters to the `request` object’s [`finish(with:context:)`](avasynchronousciimagefilteringrequest/finish(with:context:).md) method. (If your filter rendering fails, call the `request` object’s [`finish(with:)`](avasynchronousciimagefilteringrequest/finish(with:).md) method if you cannot apply filters.)

Creating a composition with this method sets values for the following properties:

- The [`frameDuration`](avmutablevideocomposition/frameduration.md) property is set to accommodate the [`nominalFrameRate`](avassettrack/nominalframerate.md) value for the asset’s first enabled video track. If the nominal frame rate is zero, AVFoundation uses a default framerate of 30 fps.
- The [`renderSize`](avmutablevideocomposition/rendersize.md) property is set to a size that encompasses the asset’s first enabled video track, respecting the track’s [`preferredTransform`](avassettrack/preferredtransform.md) property.
- The [`animationTool`](avmutablevideocomposition/animationtool.md) property is set to `1.0`.

## Parameters

- `asset`: The asset whose configuration matches the intended use of the video composition.
- `applier`: The block takes a single parameter and has no return value:

## See Also

- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](avmutablevideocomposition/videocomposition(withpropertiesof:completionhandler:).md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [class func videoComposition(withPropertiesOf: AVAsset, prototypeInstruction: AVVideoCompositionInstruction, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](avmutablevideocomposition/videocomposition(withpropertiesof:prototypeinstruction:completionhandler:).md)
  Returns a new mutable video composition with the specified asset properties and a prototype video composition instruction.
- [class func videoComposition(with: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](avmutablevideocomposition/videocomposition(with:applyingcifilterswithhandler:completionhandler:).md)
  Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [init(propertiesOf: AVAsset)](avmutablevideocomposition/init(propertiesof:).md)
  Creates a mutable video composition with the specified asset properties.
- [init(propertiesOf: AVAsset, prototypeInstruction: AVVideoCompositionInstruction)](avmutablevideocomposition/init(propertiesof:prototypeinstruction:).md)
  Creates a mutable video composition with the specified asset properties and a prototype video composition instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/init(asset:applyingcifilterswithhandler:))*