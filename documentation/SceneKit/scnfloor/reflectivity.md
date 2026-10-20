# reflectivity

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The intensity of the scene’s reflection on the floor. Animatable.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var reflectivity: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat reflectivity;
```

#### Discussion

If this property’s value is greater than zero, SceneKit renders a reflection for all contents of the scene located above the floor.

A lower reflectivity causes the rendered reflection to appear with less intensity, allowing the floor’s material to be more visible. At higher reflectivity values, the rendered reflection appears with greater intensity than the floor’s own material. The default reflectivity is `0.25`.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Adding Reflections to a Floor
- [var reflectionFalloffEnd: CGFloat](./reflectionfalloffend.md)
  The distance from the floor at which scene contents are no longer reflected. Animatable.
- [var reflectionFalloffStart: CGFloat](./reflectionfalloffstart.md)
  The distance from the floor at which scene contents are reflected at full intensity. Animatable.
- [var reflectionResolutionScaleFactor: CGFloat](./reflectionresolutionscalefactor.md)
  The resolution scale factor of the offscreen buffer that SceneKit uses to render reflections.
- [var reflectionCategoryBitMask: Int](./reflectioncategorybitmask.md)
  A mask that defines which categories of other objects show reflections on the floor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnfloor/reflectivity)*