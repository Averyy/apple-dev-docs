# speed

**Framework**: RealityKit  
**Kind**: property

The rate of playback for all audio resources in the group, with a range of `[.25, 4]`

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
@preconcurrency var speed: Double { get set }
```

#### Discussion

Set the speed to `1` for a normal playback rate. All audio sources in the group will play at the same speed to maintain synchronization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackgroupcontroller/speed)*