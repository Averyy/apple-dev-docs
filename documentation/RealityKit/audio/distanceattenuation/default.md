# default

**Framework**: RealityKit  
**Kind**: property

The default distance attenuation, which uses a rolloff model that mimics real-world physics.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
static let `default`: Audio.DistanceAttenuation
```

#### Discussion

The [`Audio.DistanceAttenuation.rolloff(factor:)`](audio/distanceattenuation/rolloff(factor:).md) model attenuates spatial audio with a factor of `1.0` as the listener moves away from the source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/distanceattenuation/default)*