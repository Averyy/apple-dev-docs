# AVAssetImageGeneratorCompletionHandler

**Framework**: AVFoundation  
**Kind**: typealias

A type alias for a closure that provides the result of an image generation request.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias AVAssetImageGeneratorCompletionHandler = (CMTime, CGImage?, CMTime, AVAssetImageGenerator.Result, (any Error)?) -> Void
```

## Parameters

- `requestedTime`: A time in the video timeline for which to generate an image.
- `image`: A generated image for the requested time.
- `actualTime`: The actual time in the video timeline at which it generated an image. The requested and actual times may differ depending on your image generator configuration including its time tolerance values.
- `result`: A value that indicates the result of the image generation request.
- `error`: An optional error. If an error occurs the system provides an error object that provides the details of the failure.

## See Also

- [func image(at: CMTime) async throws -> (image: CGImage, actualTime: CMTime)](avassetimagegenerator/image(at:).md)
  Generates an image for a requested time.
- [func images(for: [CMTime]) -> sending AVAssetImageGenerator.Images](avassetimagegenerator/images(for:).md)
  Generates images for times within the video timeline.
- [AVAssetImageGenerator.Images](avassetimagegenerator/images.md)
  An asynchronous sequence of images created by an image generator.
- [func generateCGImageAsynchronously(for: CMTime, completionHandler: (CGImage?, CMTime, (any Error)?) -> Void)](avassetimagegenerator/generatecgimageasynchronously(for:completionhandler:).md)
  Generates an image asynchronously for a requested time, and returns the result in a callback.
- [func generateCGImagesAsynchronously(forTimes: [NSValue], completionHandler: AVAssetImageGeneratorCompletionHandler)](avassetimagegenerator/generatecgimagesasynchronously(fortimes:completionhandler:).md)
  Generates images asynchronously for an array of requested times, and returns the results in a callback.
- [func cancelAllCGImageGeneration()](avassetimagegenerator/cancelallcgimagegeneration.md)
  Cancels all pending image generation requests.
- [func copyCGImage(at: CMTime, actualTime: UnsafeMutablePointer<CMTime>?) throws -> CGImage](avassetimagegenerator/copycgimage(at:actualtime:).md)
  Returns an image for the asset at or near a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegeneratorcompletionhandler)*