# requestThumbnailImages(atTimes:timeOption:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Captures one or more thumbnail images asynchronously from the current movie.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
func requestThumbnailImages(atTimes playbackTimes: [Any]!, timeOption option: MPMovieTimeOption)
```

```objc
- (void) requestThumbnailImagesAtTimes:(NSArray *) playbackTimes timeOption:(MPMovieTimeOption) option;
```

## Discussion

This method processes each thumbnail request separately and asynchronously. When the results for a single image arrive, the movie player posts a [`MPMoviePlayerThumbnailImageRequestDidFinishNotification`](../mpmovieplayerthumbnailimagerequestdidfinishnotification.md) notification with the results for that image. Notifications are posted regardless of whether the image capture was successful or failed. You should register for this notification prior to calling this method.

> **Note**:  This method is not not called when the source URL is an HTTP Live Streaming (HLS) content source. See [HTTP Live Streaming Overview](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StreamingMediaGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008332).

## Parameters

- `playbackTimes`: An array of [`NSNumber`](../../Foundation/nsnumber.md) objects containing the times at which to capture the thumbnail images. Each time value represents the number of seconds from the beginning of the current movie.
- `option`: The option to use when determining which specific frame to use for each thumbnail image. For a list of possible values, see [`MPMovieTimeOption`](../mpmovietimeoption.md).

## See Also

### Generating thumbnail images
- [func thumbnailImage(atTime: TimeInterval, timeOption: MPMovieTimeOption) -> UIImage!](./thumbnailimage%28attime,timeoption%29.md)
  Captures and returns a thumbnail image from the current movie.
- [func cancelAllThumbnailImageRequests()](./cancelallthumbnailimagerequests%28%29.md)
  Cancels all pending asynchronous thumbnail image requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/requestthumbnailimages(attimes:timeoption:))*