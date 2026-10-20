# enqueue(_:)

**Framework**: AVFoundation  
**Kind**: method

Sends a sample buffer in order to render its contents.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func enqueue(_ sampleBuffer: CMSampleBuffer)
```

#### Discussion

The audio in the sample buffer is rendered at the sample buffer’s output presentation timestamp, as interpreted by the timebase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/enqueue(_:))*