# jointNames

**Framework**: RealityKit  
**Kind**: property

The names of the joints to animate.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var jointNames: [String] { get set }
```

## See Also

- [var name: String](sampledanimation/name.md)
  A textual name for the animation.
- [var bindTarget: BindTarget](sampledanimation/bindtarget.md)
  A textual name that identifies the particular property that animates.
- [var blendLayer: Int32](sampledanimation/blendlayer.md)
  The order in which the framework composites the animation.
- [var isRotationAnimated: Bool](sampledanimation/isrotationanimated.md)
  A Boolean value that indicates whether the animation observes rotational changes in the entity’s transform.
- [var isScaleAnimated: Bool](sampledanimation/isscaleanimated.md)
  A Boolean value that indicates whether the animation observes changes in the entity’s size.
- [var isTranslationAnimated: Bool](sampledanimation/istranslationanimated.md)
  A Boolean value that indicates whether the animation observes translational changes in the entity’s transform.
- [var additive: Bool](sampledanimation/additive.md)
  A Boolean value that indicates whether the animation builds on the current state of the target entity or resets the state before running.
- [var tweenMode: TweenMode](sampledanimation/tweenmode.md)
  An option that determines how animation frames transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/jointnames)*