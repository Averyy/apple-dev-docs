# thumbnailImage(atTime:timeOption:)

**Framework**: Media Player  
**Kind**: method

Captures and returns a thumbnail image from the current movie.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
func thumbnailImage(atTime playbackTime: TimeInterval, timeOption option: MPMovieTimeOption) -> UIImage!
```

#### Return Value

An image object containing the image from the movie or `nil` if the thumbnail could not be captured.

#### Discussion

This method captures the thumbnail image synchronously from the current movie (which is accessible from the [`MPMovieSourceType.unknown`](mpmoviesourcetype/unknown.md) property).

> **Note**:  This method is not successful when the source URL is an HTTP Live Streaming (HLS) content source. The returned value for an HLS source is an empty `UIImage` object. See [`HTTP Live Streaming Overview`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StreamingMediaGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008332).

 This method is not successful when the source URL is an HTTP Live Streaming (HLS) content source. The returned value for an HLS source is an empty `UIImage` object. See [`HTTP Live Streaming Overview`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StreamingMediaGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008332).

## Parameters

- `playbackTime`: The time at which to capture the thumbnail image. The time value represents the number of seconds from the beginning of the current movie.
- `option`: The option to use when determining which specific frame to use for the thumbnail image. For a list of possible values, see  .

## See Also

- [func requestThumbnailImages(atTimes: [Any]!, timeOption: MPMovieTimeOption)](mpmovieplayercontroller/requestthumbnailimages(attimes:timeoption:).md)
  Captures one or more thumbnail images asynchronously from the current movie.
- [func cancelAllThumbnailImageRequests()](mpmovieplayercontroller/cancelallthumbnailimagerequests.md)
  Cancels all pending asynchronous thumbnail image requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/thumbnailimage(attime:timeoption:))*