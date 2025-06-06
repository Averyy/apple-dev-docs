# generateCGImagesAsynchronously(forTimes:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Generates images asynchronously for an array of requested times, and returns the results in a callback.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func generateCGImagesAsynchronously(forTimes requestedTimes: [NSValue], completionHandler handler: @escaping AVAssetImageGeneratorCompletionHandler)
```

#### Discussion

Swift clients should prefer the asynchronous `images(for:)` method instead.

## Parameters

- `requestedTimes`: An array of times, contained in NSValue objects, in the video timeline for which to generate images.
- `handler`: A callback that the image generator invokes for each requested image time.

## Topics

### Data Types
- [typealias AVAssetImageGeneratorCompletionHandler](avassetimagegeneratorcompletionhandler.md)
  A type alias for a closure that provides the result of an image generation request.
- [AVAssetImageGenerator.Result](avassetimagegenerator/result.md)
  Constants that indicate the result of an image generation request.

## See Also

- [func image(at: CMTime) async throws -> (image: CGImage, actualTime: CMTime)](avassetimagegenerator/image(at:).md)
  Generates an image for a requested time.
- [func images(for: [CMTime]) -> AVAssetImageGenerator.Images](avassetimagegenerator/images(for:).md)
  Generates images for times within the video timeline.
- [func generateCGImageAsynchronously(for: CMTime, completionHandler: (CGImage?, CMTime, (any Error)?) -> Void)](avassetimagegenerator/generatecgimageasynchronously(for:completionhandler:).md)
  Generates an image asynchronously for a requested time, and returns the result in a callback.
- [typealias AVAssetImageGeneratorCompletionHandler](avassetimagegeneratorcompletionhandler.md)
  A type alias for a closure that provides the result of an image generation request.
- [func cancelAllCGImageGeneration()](avassetimagegenerator/cancelallcgimagegeneration.md)
  Cancels all pending image generation requests.
- [func copyCGImage(at: CMTime, actualTime: UnsafeMutablePointer<CMTime>?) throws -> CGImage](avassetimagegenerator/copycgimage(at:actualtime:).md)
  Returns an image for the asset at or near a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/generatecgimagesasynchronously(fortimes:completionhandler:))*