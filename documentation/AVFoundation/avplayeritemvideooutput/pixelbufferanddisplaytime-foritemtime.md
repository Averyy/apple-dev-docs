# pixelBufferAndDisplayTime(forItemTime:)

**Framework**: AVFoundation  
**Kind**: method

Retrieves an image that is appropriate for display at the specified item time, and marks the image as acquired

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func pixelBufferAndDisplayTime(forItemTime itemTime: CMTime) -> (pixelBuffer: CVReadOnlyPixelBuffer?, itemTimeForDisplay: CMTime)
```

#### Return Value

A tuple containing the image to be displayed and a CMTime representing the true display deadline for the pixel buffer

#### Discussion

- itemTime: A CMTime that expresses a desired item time

Typically you would call this method in response to a CADisplayLink delegate invocation and if hasNewPixelBuffer(forItemTime:) also returns true.

The buffer retrieved from pixelBufferAndDisplayTime(forItemTime:) may itself be nil. A nil pixel buffer communicates that nothing should be displayed for the supplied item time.

## See Also

- [func hasNewPixelBuffer(forItemTime: CMTime) -> Bool](avplayeritemvideooutput/hasnewpixelbuffer(foritemtime:).md)
  Returns a Boolean value that indicates whether video output is available for the specified item time.
- [func copyPixelBuffer(forItemTime: CMTime, itemTimeForDisplay: UnsafeMutablePointer<CMTime>?) -> CVPixelBuffer?](avplayeritemvideooutput/copypixelbuffer(foritemtime:itemtimefordisplay:).md)
  Retrieves an image that is appropriate for display at the specified item time, and marks the image as acquired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/pixelbufferanddisplaytime(foritemtime:))*