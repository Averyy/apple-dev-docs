# halfExtent

**Framework**: SceneKit  
**Kind**: property

A location marking the end of the field’s area of effect.

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
var halfExtent: SCNVector3 { get set }
```

#### Discussion

To define a field’s area of effect, use the [`position`](scnnode/position.md) property of the node that contains the field and the field’s [`halfExtent`](scnphysicsfield/halfextent.md) property. The center of the area of effect is the node’s position. The half-extent, a position vector in the local coordinate space of the node containing the field, marks one corner of a box, and the negative of the half-extent vector marks the opposite corner of the box. For example, if a node’s position is the vector `{2.0, 2.0, 2.0}` and it contains a physics field whose half-extent is the vector `{0.5, 0.5, 0.5}`, the field’s area of effect is the box extending from `1.5` to `2.5` along each axis of the scene’s coordinate system.

By default, a field’s area of effect is the interior of this box shape. Use the [`usesEllipsoidalExtent`](scnphysicsfield/usesellipsoidalextent.md) property to instead make the area of effect an ellipsoid bounded by this box. Use the [`scope`](scnphysicsfield/scope.md) property to choose whether the area of effect is the interior or exterior of the box (or ellipsoid).

The default half-extent is the vector `{INFINITY, INFINITY, INFINITY}`, specifying that the field affects bodies located anywhere in the scene.

## See Also

- [var scope: SCNPhysicsFieldScope](scnphysicsfield/scope.md)
  The area affected by the field, either inside or outside its region.
- [var usesEllipsoidalExtent: Bool](scnphysicsfield/usesellipsoidalextent.md)
  A Boolean value that determines whether the field’s area of effect is shaped like a box or ellipsoid.
- [var offset: SCNVector3](scnphysicsfield/offset.md)
  The offset of the field’s center within its area of effect.
- [var direction: SCNVector3](scnphysicsfield/direction.md)
  The field’s directional axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/halfextent)*