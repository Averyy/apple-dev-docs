# isPlaying

**Framework**: RealityKit  
**Kind**: property

A Boolean value that indicates whether playback is currently active.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@MainActor
var isPlaying: Bool { get }
```

#### Discussion

You may experience a small delay between when you call the [`play()`](audiogeneratorcontroller/play().md) method and when the [`isPlaying`](audiogeneratorcontroller/isplaying.md) property reports `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiogeneratorcontroller/isplaying)*