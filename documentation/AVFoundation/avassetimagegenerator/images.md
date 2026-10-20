# AVAssetImageGenerator.Images

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence of images created by an image generator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct Images
```

## Mentions

- [Creating images from a video asset](../creating-images-from-a-video-asset.md)

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> AVAssetImageGenerator.Images](./images/makeasynciterator%28%29.md)
  Creates an asynchronous iterator that produces elements of this type.
### Iterating elements
- [func next() async -> AVAssetImageGenerator.Images.Element?](./images/next%28%29.md)
  Returns the next element in the sequence.
- [AVAssetImageGenerator.Images.Element](./images/element.md)
  An element that provides the result of an image generation request.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../Swift/asynciteratorprotocol.md)
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Generating images
- [func image(at: CMTime) async throws -> (image: CGImage, actualTime: CMTime)](./image%28at%29.md)
  Generates an image for a requested time.
- [func images(for: [CMTime]) -> sending AVAssetImageGenerator.Images](./images%28for%29.md)
  Generates images for times within the video timeline.
- [func generateCGImageAsynchronously(for: CMTime, completionHandler: (CGImage?, CMTime, (any Error)?) -> Void)](./generatecgimageasynchronously%28for,completionhandler%29.md)
  Generates an image asynchronously for a requested time, and returns the result in a callback.
- [func generateCGImagesAsynchronously(forTimes: [NSValue], completionHandler: AVAssetImageGeneratorCompletionHandler)](./generatecgimagesasynchronously%28fortimes,completionhandler%29.md)
  Generates images asynchronously for an array of requested times, and returns the results in a callback.
- [typealias AVAssetImageGeneratorCompletionHandler](../avassetimagegeneratorcompletionhandler.md)
  A type alias for a closure that provides the result of an image generation request.
- [func cancelAllCGImageGeneration()](./cancelallcgimagegeneration%28%29.md)
  Cancels all pending image generation requests.
- [func copyCGImage(at: CMTime, actualTime: UnsafeMutablePointer<CMTime>?) throws -> CGImage](./copycgimage%28at,actualtime%29.md)
  Returns an image for the asset at or near a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images)*