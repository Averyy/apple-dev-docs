# cancelAllCGImageGeneration()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Cancels all pending image generation requests.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func cancelAllCGImageGeneration()
```

```objc
- (void) cancelAllCGImageGeneration;
```

#### Discussion

Calling this method invokes the handler block with a result of [`AVAssetImageGenerator.Result.cancelled`](./result/cancelled.md) for all requested times for which the generator hasn’t yet produced an image.

## See Also

### Generating images
- [func image(at: CMTime) async throws -> (image: CGImage, actualTime: CMTime)](./image%28at%29.md)
  Generates an image for a requested time.
- [func images(for: [CMTime]) -> sending AVAssetImageGenerator.Images](./images%28for%29.md)
  Generates images for times within the video timeline.
- [AVAssetImageGenerator.Images](./images.md)
  An asynchronous sequence of images created by an image generator.
- [func generateCGImageAsynchronously(for: CMTime, completionHandler: (CGImage?, CMTime, (any Error)?) -> Void)](./generatecgimageasynchronously%28for,completionhandler%29.md)
  Generates an image asynchronously for a requested time, and returns the result in a callback.
- [func generateCGImagesAsynchronously(forTimes: [NSValue], completionHandler: AVAssetImageGeneratorCompletionHandler)](./generatecgimagesasynchronously%28fortimes,completionhandler%29.md)
  Generates images asynchronously for an array of requested times, and returns the results in a callback.
- [typealias AVAssetImageGeneratorCompletionHandler](../avassetimagegeneratorcompletionhandler.md)
  A type alias for a closure that provides the result of an image generation request.
- [func copyCGImage(at: CMTime, actualTime: UnsafeMutablePointer<CMTime>?) throws -> CGImage](./copycgimage%28at,actualtime%29.md)
  Returns an image for the asset at or near a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/cancelallcgimagegeneration())*