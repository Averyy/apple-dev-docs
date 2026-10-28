# copyPixelBuffer(forItemTime:itemTimeForDisplay:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Retrieves an image that is appropriate for display at the specified item time, and marks the image as acquired.

**Availability**:
- iOS 6.0+ - Deprecated in 27.0
- iPadOS 6.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.8+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use pixelBufferAndDisplayTime(forItemTime:) instead

## Declaration

```swift
func copyPixelBuffer(forItemTime itemTime: CMTime, itemTimeForDisplay outItemTimeForDisplay: UnsafeMutablePointer<CMTime>?) -> CVPixelBuffer?
```

```objc
- (CVPixelBufferRef) copyPixelBufferForItemTime:(CMTime) itemTime itemTimeForDisplay:(CMTime *) outItemTimeForDisplay;
```

## Return Value

A pixel buffer containing the image data to display or `nil` if nothing should be displayed at the specified time. The caller is responsible for calling [`CVBufferRelease`](../../CoreVideo/cvbufferrelease.md) on the returned data when it is no longer needed.

## Discussion

Typically, you call this method in response to a CVDisplayLink callback or a [`CADisplayLink`](../../QuartzCore/cadisplaylink.md) delegate method call when the [`hasNewPixelBuffer(forItemTime:)`](./hasnewpixelbuffer%28foritemtime%29.md) method also returns [`true`](../../Swift/true.md).

After calling this method, the video output object marks the pixel buffer data as having been acquired. This causes the [`hasNewPixelBuffer(forItemTime:)`](./hasnewpixelbuffer%28foritemtime%29.md) method to return [`false`](../../Swift/false.md) unless newer data becomes available.

## Parameters

- `itemTime`: The time at which you want to retrieve the image from the item.
- `outItemTimeForDisplay`: The time by which you intend to use the returned pixel buffer. You may specify `nil` for this parameter if you do not have a specific deadline.

## See Also

### Getting pixel buffer data
- [func hasNewPixelBuffer(forItemTime: CMTime) -> Bool](./hasnewpixelbuffer%28foritemtime%29.md)
  Returns a Boolean value that indicates whether video output is available for the specified item time.
- [func pixelBufferAndDisplayTime(forItemTime: CMTime) -> (pixelBuffer: CVReadOnlyPixelBuffer?, itemTimeForDisplay: CMTime)](./pixelbufferanddisplaytime%28foritemtime%29.md)
  Retrieves an image that is appropriate for display at the specified item time, and marks the image as acquired


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/copypixelbuffer(foritemtime:itemtimefordisplay:))*