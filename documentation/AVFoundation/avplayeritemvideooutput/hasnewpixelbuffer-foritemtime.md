# hasNewPixelBuffer(forItemTime:)

**Framework**: AVFoundation  
**Kind**: method

Returns a Boolean value that indicates whether video output is available for the specified item time.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func hasNewPixelBuffer(forItemTime itemTime: CMTime) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if there is available video output that has not been previously acquired or [`false`](https://developer.apple.com/documentation/Swift/false) if there is not.

#### Discussion

This method returns [`true`](https://developer.apple.com/documentation/Swift/true) if the video data at the specified time has not yet been acquired or is different from the video that was acquired previously. If you require multiple objects to acquire video output from the same [`AVPlayerItem`](avplayeritem.md) object, you should create separate `AVPlayerItemVideoOutput` objects for each.

## Parameters

- `itemTime`: The item time to query. The time value is relative to the   object with which the receiver is associated.

## See Also

- [func copyPixelBuffer(forItemTime: CMTime, itemTimeForDisplay: UnsafeMutablePointer<CMTime>?) -> CVPixelBuffer?](avplayeritemvideooutput/copypixelbuffer(foritemtime:itemtimefordisplay:).md)
  Retrieves an image that is appropriate for display at the specified item time, and marks the image as acquired.
- [func pixelBufferAndDisplayTime(forItemTime: CMTime) -> (pixelBuffer: CVReadOnlyPixelBuffer?, itemTimeForDisplay: CMTime)](avplayeritemvideooutput/pixelbufferanddisplaytime(foritemtime:).md)
  Retrieves an image that is appropriate for display at the specified item time, and marks the image as acquired


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/hasnewpixelbuffer(foritemtime:))*