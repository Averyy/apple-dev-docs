# anechoic

**Framework**: RealityKit  
**Kind**: property

A reverb instance that applies no reverberation to spatial audio sources.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
static let anechoic: Reverb
```

#### Discussion

> ⚠️ **Warning**: [`anechoic`](reverb/anechoic.md) will cause spatial audio sources to lose externalization, or the sense that an audio source is in a person’s space. Only use this case when when the immersive environment is abstract or otherwise unrealistic.

[`anechoic`](reverb/anechoic.md) will cause spatial audio sources to lose externalization, or the sense that an audio source is in a person’s space. Only use this case when when the immersive environment is abstract or otherwise unrealistic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/reverb/anechoic)*