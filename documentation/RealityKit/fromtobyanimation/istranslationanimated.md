# isTranslationAnimated

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the animation interpolates changes to the target object’s position.

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

## See Also

### Configuring the animation
- [var name: String](./name.md)
  A textual name for the animation.
- [var bindTarget: BindTarget](./bindtarget.md)
  A textual name that identifies the particular property that animates.
- [var blendLayer: Int32](./blendlayer.md)
  The order in which the framework composites the animation.
- [var jointNames: [String]](./jointnames.md)
  Joint names that define the joints in the skeletal pose.
- [var isScaleAnimated: Bool](./isscaleanimated.md)
  A Boolean value that indicates whether that animation interpolates changes to the target’s size.
- [var isRotationAnimated: Bool](./isrotationanimated.md)
  A Boolean value that indicates whether the animation interpolates rotational changes.
- [var isAdditive: Bool](./isadditive.md)
  A Boolean value that indicates whether the animation blends additively with concurrent animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyanimation/istranslationanimated)*