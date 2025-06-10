# blendLayer

**Framework**: RealityKit  
**Kind**: property

The order in which the framework composites the animation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var blendLayer: Int32 { get set }
```

#### Discussion

The framework applies multiple animations on the same target in ascending order of this property’s value. Animations in a lower layer run before animations in a higher layer. Animations that share the same value apply in the order that they execute.

## See Also

- [var name: String](sampledanimation/name.md)
  A textual name for the animation.
- [var bindTarget: BindTarget](sampledanimation/bindtarget.md)
  A textual name that identifies the particular property that animates.
- [var jointNames: [String]](sampledanimation/jointnames.md)
  The names of the joints to animate.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/blendlayer)*