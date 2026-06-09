# isPlaying

**Framework**: RealityKit  
**Kind**: property

A Boolean value that indicates whether playback is currently active.

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
@preconcurrency var isPlaying: Bool { get }
```

#### Discussion

You may experience a small delay between when you call the [`play()`](audioplaybackgroupcontroller/play().md) method and when the [`isPlaying`](audioplaybackgroupcontroller/isplaying.md) property reports `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackgroupcontroller/isplaying)*