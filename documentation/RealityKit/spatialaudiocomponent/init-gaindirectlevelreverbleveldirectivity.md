# init(gain:directLevel:reverbLevel:directivity:)

**Framework**: RealityKit  
**Kind**: init

Creates a spatial audio component from a gain value, a direct level, a reverb level, and a directivity value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init(gain: Audio.Decibel = .zero, directLevel: Audio.Decibel = .zero, reverbLevel: Audio.Decibel = .zero, directivity: Audio.Directivity = .beam(focus: .zero))
```

## Parameters

- `gain`: The overall level for all sounds that an entity emits.
- `directLevel`: The level of the direct unreverberated signal that an entity emits.
- `reverbLevel`: The level of reverberated signal that an entity emits.
- `directivity`: The radiation pattern for sound that an entity emits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spatialaudiocomponent/init(gain:directlevel:reverblevel:directivity:))*