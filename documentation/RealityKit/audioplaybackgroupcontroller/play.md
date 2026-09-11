# play()

**Framework**: RealityKit  
**Kind**: method

Plays the audio resource.

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
@preconcurrency func play()
```

#### Discussion

The controller plays from the beginning of the resource, or from the point at which it was paused if you previously called the [`pause()`](audioplaybackgroupcontroller/pause().md) method during playback. The controller ignores calls to [`play()`](audioplaybackgroupcontroller/play().md) when audio is already playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackgroupcontroller/play())*