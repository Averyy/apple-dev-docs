# stop()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Stops playback of the audio resource and discards the location in the audio stream.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency func stop()
```

#### Discussion

The next time you call [`play()`](./play%28%29.md), playback starts at the beginning of the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackgroupcontroller/stop())*