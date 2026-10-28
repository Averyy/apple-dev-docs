# AVAsynchronousCIImageFilteringRequest

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that supports using Core Image filters to process an individual video frame in a video composition.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.11+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVCIImageFilteringParameters instead

## Declaration

```swift
class AVAsynchronousCIImageFilteringRequest
```

```objc
@interface AVAsynchronousCIImageFilteringRequest : NSObject
```

## Overview

You use this class when creating a composition for Core Image filtering with the [`init(asset:applyingCIFiltersWithHandler:)`](./avvideocomposition/init%28asset,applyingcifilterswithhandler%29.md) method. In that method call, you provide a block to be called by AVFoundation as it processes each frame of video, and the block’s sole parameter is a [`AVAsynchronousCIImageFilteringRequest`](./avasynchronousciimagefilteringrequest.md) object. Use that object both to the video frame image to be filtered and allows you to return a filtered image to AVFoundation for display or export. The code listing below shows an example of applying a filter to an asset.

**Swift**:

```swift
guard let filter = CIFilter(name: "CIGaussianBlur") else { return }
let composition = AVVideoComposition(asset: asset) { request in
    // Clamp to avoid blurring transparent pixels at the image edges.
    let source = request.sourceImage.clampedToExtent()
    filter.setValue(source, forKey: kCIInputImageKey)

    // Vary filter parameters based on the video timing.
    let seconds = CMTimeGetSeconds(request.compositionTime)
    filter.setValue(seconds * 10.0, forKey: kCIInputRadiusKey)
            
    // Crop the blurred output to the bounds of the original image.
    if let output = filter.outputImage?.cropped(to: request.sourceImage.extent) {
        request.finish(with: output, context: nil)
    } else {
        request.finish(with: AppError.customError)
    }
}
```

**Objective-C**:

```objc
CIFilter *filter = [CIFilter filterWithName:@"CIGaussianBlur"];
AVVideoComposition *composition = [AVVideoComposition videoCompositionWithAsset: asset
    applyingCIFiltersWithHandler:^(AVAsynchronousCIImageFilteringRequest *request){
        // Clamp to avoid blurring transparent pixels at the image edges
        CIImage *source = [request.sourceImage imageByClampingToExtent];
        [filter setValue:source forKey:kCIInputImageKey];
 
        // Vary filter parameters based on video timing
        Float64 seconds = CMTimeGetSeconds(request.compositionTime);
        [filter setValue:seconds * 10.0 forKey:kCIInputRadiusKey];
 
        // Crop the blurred output to the bounds of the original image
        CIImage *output = [filter.outputImage imageByCroppingToRect:request.sourceImage.extent];
 
        // Provide the filter output to the composition
        [request finishWithImage:output context:nil];
    }];
```

> 💡 **Tip**:  To use the created video composition for playback, create an [`AVPlayerItem`](./avplayeritem.md) object from the same asset used as the composition’s source, then assign the composition to the player item’s [`videoComposition`](./avplayeritem/videocomposition.md) property. To export the composition to a new movie file, create an [`AVAssetExportSession`](./avassetexportsession.md) object from the same source asset, then assign the composition to the export session’s [`videoComposition`](./avassetexportsession/videocomposition.md) property.

## Topics

### Getting the image to be filtered
- [var sourceImage: CIImage](./avasynchronousciimagefilteringrequest/sourceimage.md)
  The current video frame image.
### Getting contextual information for filtering
- [var compositionTime: CMTime](./avasynchronousciimagefilteringrequest/compositiontime.md)
  The time in the video composition corresponding to the frame being processed.
- [var renderSize: CGSize](./avasynchronousciimagefilteringrequest/rendersize.md)
  The width and height, in pixels, of the frame being processed.
### Returning the filtered image
- [func finish(with: CIImage, context: CIContext?)](./avasynchronousciimagefilteringrequest/finish%28with,context%29.md)
  Provides the filtered video frame image to AVFoundation for further processing or display.
- [func finish(with: any Error)](./avasynchronousciimagefilteringrequest/finish%28with%29.md)
  Notifies AVFoundation that you cannot fulfill the image filtering request.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating a video composition
- [convenience init(configuration: AVVideoComposition.Configuration)](./avvideocomposition/init%28configuration%29.md)
  Initialize an AVVideoComposition with a configuration.
- [AVVideoComposition.Configuration](./avvideocomposition/configuration.md)
  Configurable properties for initializing a new AVVideoComposition instance.
- [convenience init(applyingFiltersTo: AVAsset, applier: (AVCIImageFilteringParameters) async throws -> AVCIImageFilteringResult) async throws](./avvideocomposition/init%28applyingfiltersto,applier%29.md)
  Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.
- [class func videoComposition(with: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: (AVVideoComposition?, (any Error)?) -> Void)](./avvideocomposition/videocomposition%28with,applyingcifilterswithhandler,completionhandler%29.md)
  Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [struct AVCIImageFilteringParameters](./avciimagefilteringparameters.md)
- [struct AVCIImageFilteringResult](./avciimagefilteringresult.md)
  An output video frame processed with Core Image filtering.
- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVVideoComposition?, (any Error)?) -> Void)](./avvideocomposition/videocomposition%28withpropertiesof,completionhandler%29.md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [init(propertiesOf: AVAsset)](./avvideocomposition/init%28propertiesof%29.md)
  Creates a video composition object configured to present the video tracks of the specified asset.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](./avvideocomposition/init%28asset,applyingcifilterswithhandler%29.md)
  Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.
- [+ videoCompositionWithVideoComposition:](./avvideocomposition/videocompositionwithvideocomposition_.md)
  Pass-through initializer, for internal use in AVFoundation only


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest)*