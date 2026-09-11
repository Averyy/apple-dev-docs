# speed

**Framework**: RealityKit  
**Kind**: property

The rate of playback for all audio resources in the group, with a range of `[.25, 4]`

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
@preconcurrency var speed: Double { get set }
```

#### Discussion

Set the speed to `1` for a normal playback rate. All audio sources in the group will play at the same speed to maintain synchronization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackgroupcontroller/speed)*