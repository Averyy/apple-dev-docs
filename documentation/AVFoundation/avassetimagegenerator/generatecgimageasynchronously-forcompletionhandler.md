# generateCGImageAsynchronously(for:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Generates an image asynchronously for a requested time, and returns the result in a callback.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func generateCGImageAsynchronously(for requestedTime: CMTime, completionHandler handler: @escaping (CGImage?, CMTime, (any Error)?) -> Void)
```

#### Discussion

Swift clients should use the asynchronous [`image(at:)`](avassetimagegenerator/image(at:).md) method instead.

## Parameters

- `requestedTime`: A time in the video timeline for which to generate an image. The requested time and actual time at which it generates an image may differ depending on the generator’s time tolerance settings.
- `handler`: A callback that the image generator invokes with the result of the request.

## Topics

### Data Types
- [typealias AVAssetImageGeneratorCompletionHandler](avassetimagegeneratorcompletionhandler.md)
  A type alias for a closure that provides the result of an image generation request.
- [AVAssetImageGenerator.Result](avassetimagegenerator/result.md)
  Constants that indicate the result of an image generation request.

## See Also

- [func image(at: CMTime) async throws -> (image: CGImage, actualTime: CMTime)](avassetimagegenerator/image(at:).md)
  Generates an image for a requested time.
- [func images(for: [CMTime]) -> sending AVAssetImageGenerator.Images](avassetimagegenerator/images(for:).md)
  Generates images for times within the video timeline.
- [func generateCGImagesAsynchronously(forTimes: [NSValue], completionHandler: AVAssetImageGeneratorCompletionHandler)](avassetimagegenerator/generatecgimagesasynchronously(fortimes:completionhandler:).md)
  Generates images asynchronously for an array of requested times, and returns the results in a callback.
- [typealias AVAssetImageGeneratorCompletionHandler](avassetimagegeneratorcompletionhandler.md)
  A type alias for a closure that provides the result of an image generation request.
- [func cancelAllCGImageGeneration()](avassetimagegenerator/cancelallcgimagegeneration.md)
  Cancels all pending image generation requests.
- [func copyCGImage(at: CMTime, actualTime: UnsafeMutablePointer<CMTime>?) throws -> CGImage](avassetimagegenerator/copycgimage(at:actualtime:).md)
  Returns an image for the asset at or near a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/generatecgimageasynchronously(for:completionhandler:))*