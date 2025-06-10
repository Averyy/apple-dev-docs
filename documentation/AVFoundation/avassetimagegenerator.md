# AVAssetImageGenerator

**Framework**: AVFoundation  
**Kind**: class

An object that generates images from a video asset.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetImageGenerator
```

## Mentions

- [Creating images from a video asset](creating-images-from-a-video-asset.md)

#### Overview

Use an image generator to extract images from a video asset at particular times within its timeline.

## Topics

### Creating an Image Generator
- [init(asset: AVAsset)](avassetimagegenerator/init(asset:).md)
  Creates an object that generates images for times within a video asset.
### Configuring Image Generation
- [var maximumSize: CGSize](avassetimagegenerator/maximumsize.md)
  The maximum size of images to generate.
- [var requestedTimeToleranceBefore: CMTime](avassetimagegenerator/requestedtimetolerancebefore.md)
  A maximum length of time before the requested time to allow image generation to occur.
- [var requestedTimeToleranceAfter: CMTime](avassetimagegenerator/requestedtimetoleranceafter.md)
  A maximum length of time after the requested time to allow image generation to occur.
- [var dynamicRangePolicy: AVAssetImageGenerator.DynamicRangePolicy](avassetimagegenerator/dynamicrangepolicy-swift.property.md)
  The dynamic range policy to use when generating images.
- [AVAssetImageGenerator.DynamicRangePolicy](avassetimagegenerator/dynamicrangepolicy-swift.struct.md)
  A type that specifies the dynamic range policy to apply when generating images.
- [var appliesPreferredTrackTransform: Bool](avassetimagegenerator/appliespreferredtracktransform.md)
  A Boolean value that specifies whether to apply the track matrix or matrices when generating an image from the asset.
- [var apertureMode: AVAssetImageGenerator.ApertureMode?](avassetimagegenerator/aperturemode-swift.property.md)
  Specifies the aperture mode for the generated image.
- [AVAssetImageGenerator.ApertureMode](avassetimagegenerator/aperturemode-swift.struct.md)
  Constants that define aperture modes to use when generating images.
### Configuring Compositing
- [var videoComposition: AVVideoComposition?](avassetimagegenerator/videocomposition.md)
  A video composition to use when extracting images from assets with multiple video tracks.
- [var customVideoCompositor: (any AVVideoCompositing)?](avassetimagegenerator/customvideocompositor.md)
  A custom video compositor to use when extracting images from assets with multiple video tracks.
### Generating Images
- [func image(at: CMTime) async throws -> (image: CGImage, actualTime: CMTime)](avassetimagegenerator/image(at:).md)
  Generates an image for a requested time.
- [func images(for: [CMTime]) -> sending AVAssetImageGenerator.Images](avassetimagegenerator/images(for:).md)
  Generates images for times within the video timeline.
- [func generateCGImageAsynchronously(for: CMTime, completionHandler: (CGImage?, CMTime, (any Error)?) -> Void)](avassetimagegenerator/generatecgimageasynchronously(for:completionhandler:).md)
  Generates an image asynchronously for a requested time, and returns the result in a callback.
- [func generateCGImagesAsynchronously(forTimes: [NSValue], completionHandler: AVAssetImageGeneratorCompletionHandler)](avassetimagegenerator/generatecgimagesasynchronously(fortimes:completionhandler:).md)
  Generates images asynchronously for an array of requested times, and returns the results in a callback.
- [typealias AVAssetImageGeneratorCompletionHandler](avassetimagegeneratorcompletionhandler.md)
  A type alias for a closure that provides the result of an image generation request.
- [func cancelAllCGImageGeneration()](avassetimagegenerator/cancelallcgimagegeneration.md)
  Cancels all pending image generation requests.
- [func copyCGImage(at: CMTime, actualTime: UnsafeMutablePointer<CMTime>?) throws -> CGImage](avassetimagegenerator/copycgimage(at:actualtime:).md)
  Returns an image for the asset at or near a specified time.
### Accessing the Asset
- [var asset: AVAsset](avassetimagegenerator/asset.md)
  The asset that initialized the image generator.
### Structures
- [AVAssetImageGenerator.Images](avassetimagegenerator/images.md)
  An asynchronous sequence of images created by an image generator.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating images from a video asset](creating-images-from-a-video-asset.md)
  Display images for specific times within the media timeline by generating images from a video’s frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator)*