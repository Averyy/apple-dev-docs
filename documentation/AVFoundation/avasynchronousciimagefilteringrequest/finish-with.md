# finish(with:)

**Framework**: AVFoundation  
**Kind**: method

Notifies AVFoundation that you cannot fulfill the image filtering request.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func finish(with error: any Error)
```

#### Discussion

Call this method if you cannot process the input image and wish to abort playback as a result—for example, if the [`outputImage`](https://developer.apple.com/documentation/CoreImage/CIFilter-swift.class/outputImage) object from your filter chain is nil. (If instead you want to fall back to rendering an unfiltered image, call the [`finish(with:context:)`](avasynchronousciimagefilteringrequest/finish(with:context:).md) and pass the [`sourceImage`](avasynchronousciimagefilteringrequest/sourceimage.md) object to the `filteredImage` parameter.)

Calling this method causes AVFoundation to post a notification named [`failedToPlayToEndTimeNotification`](avplayeritem/failedtoplaytoendtimenotification.md). Observers of this notification can use the [`AVPlayerItemFailedToPlayToEndTimeErrorKey`](avplayeritemfailedtoplaytoendtimeerrorkey.md) key to examine the error you provide.

## Parameters

- `error`: An error object describing the reason to

## See Also

- [func finish(with: CIImage, context: CIContext?)](avasynchronousciimagefilteringrequest/finish(with:context:).md)
  Provides the filtered video frame image to AVFoundation for further processing or display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/finish(with:))*