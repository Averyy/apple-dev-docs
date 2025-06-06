# bindTarget

**Framework**: RealityKit  
**Kind**: property

A textual name that identifies the particular property that animates.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
var bindTarget: BindTarget { get set }
```

#### Discussion

The property name is a key path. For more information on key paths, see [`Key-Path Expressions`](https://developer.apple.com/documentation/Swift/key-path-expressions).

## See Also

- [var name: String](fromtobyanimation/name.md)
  A textual name for the animation.
- [var blendLayer: Int32](fromtobyanimation/blendlayer.md)
  The order in which the framework composites the animation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyanimation/bindtarget)*