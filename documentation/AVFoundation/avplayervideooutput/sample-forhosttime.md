# sample(forHostTime:)

**Framework**: AVFoundation  
**Kind**: method

Retrieves a video sample along with auxiliary information for display at the specified host time.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func sample(forHostTime hostTime: CMTime) -> AVPlayerVideoOutput.Sample?
```

#### Return Value

A sample containing the frame, presentation timestamp, and active configuration for the specified host time, or nil if no sample was available for that host time.

## Parameters

- `hostTime`: A CMTime that expresses a desired host time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayervideooutput/sample(forhosttime:))*