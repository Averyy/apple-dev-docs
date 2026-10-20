# videoComposition(with:applyingCIFiltersWithHandler:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class func videoComposition(with asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping @Sendable (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: @escaping @Sendable (AVMutableVideoComposition?, (any Error)?) -> Void)
```

```swift
class func videoComposition(with asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping @Sendable (AVAsynchronousCIImageFilteringRequest) -> Void) async throws -> AVMutableVideoComposition
```

```objc
+ (void) videoCompositionWithAsset:(AVAsset *) asset applyingCIFiltersWithHandler:(void (^)(AVAsynchronousCIImageFilteringRequest *request)) applier completionHandler:(void (^)(AVMutableVideoComposition *videoComposition, NSError *error)) completionHandler;
```

#### Discussion

The composition calls the specified handler one time for each frame to display (or processed for export) from the asset’s first enabled video track. In that block, you access the video frame and return a filtered result using the provided [`AVAsynchronousCIImageFilteringRequest`](../avasynchronousciimagefilteringrequest.md) object. Use that object’s [`sourceImage`](../avasynchronousciimagefilteringrequest/sourceimage.md) property to get the video frame in the form of a [`CIImage`](../../CoreImage/ciimage.md) object you can apply filters to. Pass the result of your filters to the `request` object’s [`finish(with:context:)`](../avasynchronousciimagefilteringrequest/finish%28with,context%29.md) method. (If your filter rendering fails, call the `request` object’s [`finish(with:)`](../avasynchronousciimagefilteringrequest/finish%28with%29.md) method if you can’t apply filters).

Creating a composition with this method sets values for the following properties:

- The value of the [`frameDuration`](../avvideocomposition/frameduration.md) property accommodates the [`nominalFrameRate`](../avassettrack/nominalframerate.md) value for the asset’s first enabled video track. If the nominal frame rate is zero, AVFoundation uses a default frame rate of 30 fps.
- The [`renderSize`](../avvideocomposition/rendersize.md) property value a size that encompasses the asset’s first enabled video track, respecting the track’s [`preferredTransform`](../avassettrack/preferredtransform.md) property.
- The [`renderScale`](../avvideocomposition/renderscale.md) property value is `1.0`.

## Parameters

- `asset`: The asset whose configuration matches the intended use of the video composition.
- `applier`: A block that AVFoundation calls when processing each video frame.

  The block takes a single parameter and has no return value:

  - **request**: An [`AVAsynchronousCIImageFilteringRequest`](../avasynchronousciimagefilteringrequest.md) object representing the frame to be processed.
- `completionHandler`: A block the system calls when it finishes creating the new video composition.

## See Also

### Creating a video composition
- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](./videocomposition%28withpropertiesof,completionhandler%29.md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [class func videoComposition(withPropertiesOf: AVAsset, prototypeInstruction: AVVideoCompositionInstruction, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](./videocomposition%28withpropertiesof,prototypeinstruction,completionhandler%29.md)
  Returns a new mutable video composition with the specified asset properties and a prototype video composition instruction.
- [init(propertiesOf: AVAsset)](./init%28propertiesof%29.md)
  Creates a mutable video composition with the specified asset properties.
- [init(propertiesOf: AVAsset, prototypeInstruction: AVVideoCompositionInstruction)](./init%28propertiesof,prototypeinstruction%29.md)
  Creates a mutable video composition with the specified asset properties and a prototype video composition instruction.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](./init%28asset,applyingcifilterswithhandler%29.md)
  Creates a mutable video composition configured to apply Core Image filters to each video frame of the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/videocomposition(with:applyingcifilterswithhandler:completionhandler:))*