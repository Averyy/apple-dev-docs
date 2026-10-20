# repeated(count:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Repeats an animation the number of times specified by an irrational number.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
func repeated(count: TimeInterval) -> Self
```

**Other overloads**:

```swift
func repeated(count: Int) -> Self
```

#### Return Value

A version of the calling animation repeated the given number of times.

## Parameters

- `count`: The number of times the animation repeats before stopping.

## See Also

### Repeating animation playback
- [var repeatMode: AnimationRepeatMode](./repeatmode.md)
  An option that determines how the animation repeats.
- [var fillMode: AnimationFillMode](./fillmode.md)
  An option that determines which data displays outside of the normal duration.
- [func repeated(count: Int) -> Self](./repeated%28count%29-941x8.md)
  Repeats an animation the number of times specified by a whole number.
- [func repeatingForever() -> Self](./repeatingforever%28%29.md)
  Repeats the animation infinitely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationdefinition/repeated(count:)-937w)*