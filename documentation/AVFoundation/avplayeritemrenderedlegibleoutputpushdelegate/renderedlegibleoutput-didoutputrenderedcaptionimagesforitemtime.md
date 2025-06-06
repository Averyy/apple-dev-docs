# renderedLegibleOutput(_:didOutputRenderedCaptionImages:forItemTime:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate that new rendered caption images are available.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
optional func renderedLegibleOutput(_ output: AVPlayerItemRenderedLegibleOutput, didOutputRenderedCaptionImages captionImages: [AVRenderedCaptionImage], forItemTime itemTime: CMTime)
```

## Parameters

- `output`: The rendered legible output object.
- `captionImages`: An array of   objects. A caption object consists of a   and its associated position, in pixels, relative to the video frame.
- `itemTime`: The item time at which to present the caption images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutputpushdelegate/renderedlegibleoutput(_:didoutputrenderedcaptionimages:foritemtime:))*