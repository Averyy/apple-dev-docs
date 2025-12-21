# usesEllipsoidalExtent

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether the field’s area of effect is shaped like a box or ellipsoid.

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
var usesEllipsoidalExtent: Bool { get set }
```

#### Discussion

If this value is [`false`](https://developer.apple.com/documentation/Swift/false) (the default), the field’s area of effect is the box-shaped region of space defined by its [`halfExtent`](scnphysicsfield/halfextent.md) property and the [`position`](scnnode/position.md) property of the node containing the field.

If this value is [`true`](https://developer.apple.com/documentation/Swift/true), the field’s area of effect is the ellipsoid bounded by this box-shaped region. That is, if all components of the half-extent vector are equal, the field has a spherical area of effect.

## See Also

- [var halfExtent: SCNVector3](scnphysicsfield/halfextent.md)
  A location marking the end of the field’s area of effect.
- [var scope: SCNPhysicsFieldScope](scnphysicsfield/scope.md)
  The area affected by the field, either inside or outside its region.
- [var offset: SCNVector3](scnphysicsfield/offset.md)
  The offset of the field’s center within its area of effect.
- [var direction: SCNVector3](scnphysicsfield/direction.md)
  The field’s directional axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/usesellipsoidalextent)*