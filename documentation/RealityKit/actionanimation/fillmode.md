# fillMode

**Framework**: RealityKit  
**Kind**: property

An option that determines which data displays outside of the normal duration.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var fillMode: AnimationFillMode { get set }
```

#### Discussion

This property determines what to display when the framework samples the animation outside of the range defined by its underlying duration. The animation applies this property when:

- Playback progresses toward, but hasn’t yet reached, a nonzero [`offset`](animationdefinition/offset.md). - A range determined by [`trimStart`](animationdefinition/trimstart.md), [`trimEnd`](animationdefinition/trimend.md), or [`trimDuration`](animationdefinition/trimduration.md) exceeds the animation’s underlying duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionanimation/fillmode)*