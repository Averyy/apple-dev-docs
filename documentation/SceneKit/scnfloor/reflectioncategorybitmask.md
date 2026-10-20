# reflectionCategoryBitMask

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A mask that defines which categories of other objects show reflections on the floor.

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
var reflectionCategoryBitMask: Int { get set }
```

```objc
@property (nonatomic) NSUInteger reflectionCategoryBitMask;
```

## See Also

### Adding Reflections to a Floor
- [var reflectivity: CGFloat](./reflectivity.md)
  The intensity of the scene’s reflection on the floor. Animatable.
- [var reflectionFalloffEnd: CGFloat](./reflectionfalloffend.md)
  The distance from the floor at which scene contents are no longer reflected. Animatable.
- [var reflectionFalloffStart: CGFloat](./reflectionfalloffstart.md)
  The distance from the floor at which scene contents are reflected at full intensity. Animatable.
- [var reflectionResolutionScaleFactor: CGFloat](./reflectionresolutionscalefactor.md)
  The resolution scale factor of the offscreen buffer that SceneKit uses to render reflections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnfloor/reflectioncategorybitmask)*