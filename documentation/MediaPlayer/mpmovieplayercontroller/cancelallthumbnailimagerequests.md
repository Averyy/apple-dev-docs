# cancelAllThumbnailImageRequests()

**Framework**: Media Player  
**Kind**: method

Cancels all pending asynchronous thumbnail image requests.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
func cancelAllThumbnailImageRequests()
```

#### Discussion

This method cancels only requests made using the [`requestThumbnailImages(atTimes:timeOption:)`](mpmovieplayercontroller/requestthumbnailimages(attimes:timeoption:).md) method. It does not cancel requests made synchronously using the [`thumbnailImage(atTime:timeOption:)`](mpmovieplayercontroller/thumbnailimage(attime:timeoption:).md) method.

## See Also

- [func thumbnailImage(atTime: TimeInterval, timeOption: MPMovieTimeOption) -> UIImage!](mpmovieplayercontroller/thumbnailimage(attime:timeoption:).md)
  Captures and returns a thumbnail image from the current movie.
- [func requestThumbnailImages(atTimes: [Any]!, timeOption: MPMovieTimeOption)](mpmovieplayercontroller/requestthumbnailimages(attimes:timeoption:).md)
  Captures one or more thumbnail images asynchronously from the current movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/cancelallthumbnailimagerequests())*