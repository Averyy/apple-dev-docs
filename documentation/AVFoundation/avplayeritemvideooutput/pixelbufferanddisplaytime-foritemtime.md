# pixelBufferAndDisplayTime(forItemTime:)

**Framework**: AVFoundation  
**Kind**: method

Retrieves an image that is appropriate for display at the specified item time, and marks the image as acquired

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/pixelbufferanddisplaytime(foritemtime:))*