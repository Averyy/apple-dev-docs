# name

**Framework**: RealityKit  
**Kind**: property

The name of the animation resource.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency final let name: String?
```

#### Discussion

You can get an [`AnimationPlaybackController`](animationplaybackcontroller.md) instance ready to play a particular resource that you reference by its name using the `playAnimation(named:transitionDuration:startsPaused:)` method.

## See Also

- [var definition: any AnimationDefinition](animationresource/definition.md)
  The timeframe, target object, and visual semantics of the animation.
- [struct AnimationFillMode](animationfillmode.md)
  Options that determine which animation frames display outside of the normal duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationresource/name)*