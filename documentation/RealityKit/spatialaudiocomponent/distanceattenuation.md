# distanceAttenuation

**Framework**: RealityKit  
**Kind**: property

A value that specifies the way that the sound level decreases as the distance between the listener and the sound source increases.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
var distanceAttenuation: Audio.DistanceAttenuation { get set }
```

#### Discussion

> **Note**: You can’t update the `distanceAttenuation` property dynamically. Set it before you prepare or play an audio resource on an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spatialaudiocomponent/distanceattenuation)*