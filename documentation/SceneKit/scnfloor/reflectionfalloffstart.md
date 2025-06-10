# reflectionFalloffStart

**Framework**: SceneKit  
**Kind**: property

The distance from the floor at which scene contents are reflected at full intensity. Animatable.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var reflectionFalloffStart: CGFloat { get set }
```

#### Discussion

SceneKit can render reflections on a floor using an opacity gradient (or falloff). With this gradient, the reflections of scene contents closer to the floor are more visible than those of scene contents farther from it. This property marks the distance at which the opacity gradient begins. Scene contents closer to the floor than this distance appear in the reflection with full intensity.

The default value of this property is `0.0`, indicating that the falloff gradient begins immediately.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var reflectivity: CGFloat](scnfloor/reflectivity.md)
  The intensity of the scene’s reflection on the floor. Animatable.
- [var reflectionFalloffEnd: CGFloat](scnfloor/reflectionfalloffend.md)
  The distance from the floor at which scene contents are no longer reflected. Animatable.
- [var reflectionResolutionScaleFactor: CGFloat](scnfloor/reflectionresolutionscalefactor.md)
  The resolution scale factor of the offscreen buffer that SceneKit uses to render reflections.
- [var reflectionCategoryBitMask: Int](scnfloor/reflectioncategorybitmask.md)
  A mask that defines which categories of other objects show reflections on the floor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnfloor/reflectionfalloffstart)*