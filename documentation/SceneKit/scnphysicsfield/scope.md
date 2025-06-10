# scope

**Framework**: SceneKit  
**Kind**: property

The area affected by the field, either inside or outside its region.

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
var scope: SCNPhysicsFieldScope { get set }
```

#### Discussion

First, define a field’s region using its [`halfExtent`](scnphysicsfield/halfextent.md) property and the [`position`](scnnode/position.md) property of the node containing the field. Then, use the [`scope`](scnphysicsfield/scope.md) property to choose whether the field’s area of effect is the interior of the region (the default) or all space outside the region.

## See Also

- [var halfExtent: SCNVector3](scnphysicsfield/halfextent.md)
  A location marking the end of the field’s area of effect.
- [var usesEllipsoidalExtent: Bool](scnphysicsfield/usesellipsoidalextent.md)
  A Boolean value that determines whether the field’s area of effect is shaped like a box or ellipsoid.
- [var offset: SCNVector3](scnphysicsfield/offset.md)
  The offset of the field’s center within its area of effect.
- [var direction: SCNVector3](scnphysicsfield/direction.md)
  The field’s directional axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/scope)*