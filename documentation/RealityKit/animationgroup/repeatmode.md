# repeatMode

**Framework**: RealityKit  
**Kind**: property

An option that determines how the animations repeat.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var repeatMode: AnimationRepeatMode { get set }
```

#### Discussion

If you call `FromToByAnimation/trimmed(start:end:duration:)` with a `start` or `end` that lies outside of the timeline defined by [`duration`](animationgroup/duration.md), the animation fills the additional playback by applying this property.

## See Also

- [var fillMode: AnimationFillMode](animationgroup/fillmode.md)
  An option that determines which data displays outside of the normal duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgroup/repeatmode)*