# stop()

**Framework**: RealityKit  
**Kind**: method

Stops playback of the audio resource and discards the location in the audio stream.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func stop()
```

#### Discussion

The next time you call [`play()`](audioplaybackgroupcontroller/play().md), playback starts at the beginning of the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackgroupcontroller/stop())*