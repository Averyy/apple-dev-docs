# copyCGImage(at:actualTime:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns an image for the asset at or near a specified time.

**Availability**:
- iOS 4.0+ - Deprecated in 18.0
- iPadOS 4.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Use [`image(at:)`](./image%28at%29.md) instead or [`generateCGImagesAsynchronously(forTimes:completionHandler:)`](./generatecgimagesasynchronously%28fortimes,completionhandler%29.md).

## Declaration

```swift
func copyCGImage(at requestedTime: CMTime, actualTime: UnsafeMutablePointer<CMTime>?) throws -> CGImage
```

```objc
- (CGImageRef) copyCGImageAtTime:(CMTime) requestedTime actualTime:(CMTime *) actualTime error:(NSError **) outError;
```

## Return Value

A [`CGImage`](../../CoreGraphics/cgimage.md) for the asset at or near a specified time, or `NULL` if the image could not be created.

## Discussion

This method returns the image synchronously.

## Parameters

- `requestedTime`: A time within the asset timeline for which to create an image.
- `actualTime`: Upon return, contains the time at which the image was actually generated.

  If you’re not interested in this information, pass `NULL`.

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
- [func cancelAllCGImageGeneration()](./cancelallcgimagegeneration%28%29.md)
  Cancels all pending image generation requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/copycgimage(at:actualtime:))*