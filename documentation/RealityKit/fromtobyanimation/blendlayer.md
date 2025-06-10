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

- [var name: String](fromtobyanimation/name.md)
  A textual name for the animation.
- [var bindTarget: BindTarget](fromtobyanimation/bindtarget.md)
  A textual name that identifies the particular property that animates.
- [var jointNames: [String]](fromtobyanimation/jointnames.md)
  Joint names that define the joints in the skeletal pose.
- [var isScaleAnimated: Bool](fromtobyanimation/isscaleanimated.md)
  A Boolean value that indicates whether that animation interpolates changes to the target’s size.
- [var isRotationAnimated: Bool](fromtobyanimation/isrotationanimated.md)
  A Boolean value that indicates whether the animation interpolates rotational changes.
- [var isTranslationAnimated: Bool](fromtobyanimation/istranslationanimated.md)
  A Boolean value that indicates whether the animation interpolates changes to the target object’s position.
- [var isAdditive: Bool](fromtobyanimation/isadditive.md)
  A Boolean value that indicates whether the animation blends additively with concurrent animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyanimation/blendlayer)*