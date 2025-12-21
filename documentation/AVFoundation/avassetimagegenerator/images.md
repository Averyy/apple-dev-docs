# AVAssetImageGenerator.Images

**Framework**: AVFoundation  
**Kind**: struct

An asynchronous sequence of images created by an image generator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct Images
```

## Mentions

- [Creating images from a video asset](creating-images-from-a-video-asset.md)

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> AVAssetImageGenerator.Images](avassetimagegenerator/images/makeasynciterator.md)
  Creates an asynchronous iterator that produces elements of this type.
### Iterating elements
- [func next() async -> AVAssetImageGenerator.Images.Element?](avassetimagegenerator/images/next.md)
  Returns the next element in the sequence.
- [AVAssetImageGenerator.Images.Element](avassetimagegenerator/images/element.md)
  An element that provides the result of an image generation request.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images)*