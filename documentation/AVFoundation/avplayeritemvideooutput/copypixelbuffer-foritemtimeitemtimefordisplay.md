# copyPixelBuffer(forItemTime:itemTimeForDisplay:)

**Framework**: AVFoundation  
**Kind**: method

Retrieves an image that is appropriate for display at the specified item time, and marks the image as acquired.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func copyPixelBuffer(forItemTime itemTime: CMTime, itemTimeForDisplay outItemTimeForDisplay: UnsafeMutablePointer<CMTime>?) -> CVPixelBuffer?
```

#### Return Value

A pixel buffer containing the image data to display or `nil` if nothing should be displayed at the specified time. The caller is responsible for calling [`CVBufferRelease`](https://developer.apple.com/documentation/CoreVideo/CVBufferRelease) on the returned data when it is no longer needed.

#### Discussion

Typically, you call this method in response to a CVDisplayLink callback or a [`CADisplayLink`](https://developer.apple.com/documentation/QuartzCore/CADisplayLink) delegate method call when the [`hasNewPixelBuffer(forItemTime:)`](avplayeritemvideooutput/hasnewpixelbuffer(foritemtime:).md) method also returns [`true`](https://developer.apple.com/documentation/Swift/true).

After calling this method, the video output object marks the pixel buffer data as having been acquired. This causes the [`hasNewPixelBuffer(forItemTime:)`](avplayeritemvideooutput/hasnewpixelbuffer(foritemtime:).md) method to return [`false`](https://developer.apple.com/documentation/Swift/false) unless newer data becomes available.

## Parameters

- `itemTime`: The time at which you want to retrieve the image from the item.
- `outItemTimeForDisplay`: The time by which you intend to use the returned pixel buffer. You may specify   for this parameter if you do not have a specific deadline.

## See Also

- [func hasNewPixelBuffer(forItemTime: CMTime) -> Bool](avplayeritemvideooutput/hasnewpixelbuffer(foritemtime:).md)
  Returns a Boolean value that indicates whether video output is available for the specified item time.
- [func pixelBufferAndDisplayTime(forItemTime: CMTime) -> (pixelBuffer: CVReadOnlyPixelBuffer?, itemTimeForDisplay: CMTime)](avplayeritemvideooutput/pixelbufferanddisplaytime(foritemtime:).md)
  Retrieves an image that is appropriate for display at the specified item time, and marks the image as acquired


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/copypixelbuffer(foritemtime:itemtimefordisplay:))*