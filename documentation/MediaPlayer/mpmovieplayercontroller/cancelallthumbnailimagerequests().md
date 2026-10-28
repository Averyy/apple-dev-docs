# cancelAllThumbnailImageRequests()

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Cancels all pending asynchronous thumbnail image requests.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
func cancelAllThumbnailImageRequests()
```

```objc
- (void) cancelAllThumbnailImageRequests;
```

## Discussion

This method cancels only requests made using the [`requestThumbnailImages(atTimes:timeOption:)`](./requestthumbnailimages%28attimes,timeoption%29.md) method. It does not cancel requests made synchronously using the [`thumbnailImage(atTime:timeOption:)`](./thumbnailimage%28attime,timeoption%29.md) method.

## See Also

### Generating thumbnail images
- [func thumbnailImage(atTime: TimeInterval, timeOption: MPMovieTimeOption) -> UIImage!](./thumbnailimage%28attime,timeoption%29.md)
  Captures and returns a thumbnail image from the current movie.
- [func requestThumbnailImages(atTimes: [Any]!, timeOption: MPMovieTimeOption)](./requestthumbnailimages%28attimes,timeoption%29.md)
  Captures one or more thumbnail images asynchronously from the current movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/cancelallthumbnailimagerequests())*