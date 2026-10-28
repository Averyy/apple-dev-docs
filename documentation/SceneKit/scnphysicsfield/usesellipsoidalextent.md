# usesEllipsoidalExtent

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the field’s area of effect is shaped like a box or ellipsoid.

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
var usesEllipsoidalExtent: Bool { get set }
```

```objc
@property (nonatomic) BOOL usesEllipsoidalExtent;
```

## Discussion

If this value is [`false`](../../Swift/false.md) (the default), the field’s area of effect is the box-shaped region of space defined by its [`halfExtent`](./halfextent.md) property and the [`position`](../scnnode/position.md) property of the node containing the field.

If this value is [`true`](../../Swift/true.md), the field’s area of effect is the ellipsoid bounded by this box-shaped region. That is, if all components of the half-extent vector are equal, the field has a spherical area of effect.

## See Also

### Specifying a Field’s Area of Effect
- [var halfExtent: SCNVector3](./halfextent.md)
  A location marking the end of the field’s area of effect.
- [var scope: SCNPhysicsFieldScope](./scope.md)
  The area affected by the field, either inside or outside its region.
- [var offset: SCNVector3](./offset.md)
  The offset of the field’s center within its area of effect.
- [var direction: SCNVector3](./direction.md)
  The field’s directional axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/usesellipsoidalextent)*