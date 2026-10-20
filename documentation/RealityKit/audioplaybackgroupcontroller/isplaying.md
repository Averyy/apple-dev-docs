# isPlaying

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether playback is currently active.

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
@preconcurrency var isPlaying: Bool { get }
```

#### Discussion

You may experience a small delay between when you call the [`play()`](./play%28%29.md) method and when the [`isPlaying`](./isplaying.md) property reports `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackgroupcontroller/isplaying)*