# name

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

A textual name for the animation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var name: String { get set }
```

## See Also

### Configuring the animation
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
- [var isTranslationAnimated: Bool](./istranslationanimated.md)
  A Boolean value that indicates whether the animation interpolates changes to the target object’s position.
- [var isAdditive: Bool](./isadditive.md)
  A Boolean value that indicates whether the animation blends additively with concurrent animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyanimation/name)*