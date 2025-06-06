# repeatMode

**Framework**: RealityKit  
**Kind**: property

An option that determines how the animation repeats.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
var repeatMode: AnimationRepeatMode { get set }
```

#### Discussion

If you call [`trimmed(start:end:duration:)`](sampledanimation/trimmed(start:end:duration:).md) with a `start` or `end` that lies outside of the timeline defined by [`duration`](sampledanimation/duration.md), the animation fills the additional playback by applying this property.

## See Also

- [var fillMode: AnimationFillMode](sampledanimation/fillmode.md)
  An option that determines which data displays outside of the normal duration.
- [func repeated(count: TimeInterval) -> Self](sampledanimation/repeated(count:)-3iijb.md)
  Repeats an animation the number of times specified by an irrational number.
- [func repeated(count: Int) -> Self](sampledanimation/repeated(count:)-ltbf.md)
  Repeats an animation the number of times specified by a whole number.
- [func repeatingForever() -> Self](sampledanimation/repeatingforever.md)
  Repeats the animation infinitely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/repeatmode)*