# isTranslationAnimated

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the animation observes translational changes in the entity’s transform.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var isTranslationAnimated: Bool { get set }
```

Available when `Value` is `JointTransforms`.

#### Discussion

If you set this property to `true`, the animation accommodates translation differences in the entity’s transform by interpolating to the target translation across the animation timeline.

## See Also

### Configuring the animation
- [var name: String](./name.md)
  A textual name for the animation.
- [var bindTarget: BindTarget](./bindtarget.md)
  A textual name that identifies the particular property that animates.
- [var blendLayer: Int32](./blendlayer.md)
  The order in which the framework composites the animation.
- [var jointNames: [String]](./jointnames.md)
  The names of the joints to animate.
- [var isRotationAnimated: Bool](./isrotationanimated.md)
  A Boolean value that indicates whether the animation observes rotational changes in the entity’s transform.
- [var isScaleAnimated: Bool](./isscaleanimated.md)
  A Boolean value that indicates whether the animation observes changes in the entity’s size.
- [var additive: Bool](./additive.md)
  A Boolean value that indicates whether the animation builds on the current state of the target entity or resets the state before running.
- [var tweenMode: TweenMode](./tweenmode.md)
  An option that determines how animation frames transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/istranslationanimated)*