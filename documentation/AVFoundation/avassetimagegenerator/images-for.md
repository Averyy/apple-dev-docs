# images(for:)

**Framework**: AVFoundation  
**Kind**: method

Generates images for times within the video timeline.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func images(for times: [CMTime]) -> AVAssetImageGenerator.Images
```

## Mentions

- [Creating images from a video asset](creating-images-from-a-video-asset.md)

#### Return Value

An asynchronous sequence of images.

## Parameters

- `times`: An array of times within the asset timeline to create images.

## Topics

### Generated Image Sequence
- [AVAssetImageGenerator.Images](avassetimagegenerator/images.md)
  An asynchronous sequence of images created by an image generator.

## See Also

- [func image(at: CMTime) async throws -> (image: CGImage, actualTime: CMTime)](avassetimagegenerator/image(at:).md)
  Generates an image for a requested time.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images(for:))*