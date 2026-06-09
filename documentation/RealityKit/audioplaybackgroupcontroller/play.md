# play()

**Framework**: RealityKit  
**Kind**: method

Plays the audio resource.

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
@preconcurrency func play()
```

#### Discussion

The controller plays from the beginning of the resource, or from the point at which it was paused if you previously called the [`pause()`](audioplaybackgroupcontroller/pause().md) method during playback. The controller ignores calls to [`play()`](audioplaybackgroupcontroller/play().md) when audio is already playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackgroupcontroller/play())*