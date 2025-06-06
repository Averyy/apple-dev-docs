# direction

**Framework**: SceneKit  
**Kind**: property

The field’s directional axis.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var direction: SCNVector3 { get set }
```

#### Discussion

Some types of fields apply forces whose direction or magnitude is relative to an axis. (For details on each type of field, see the methods listed in Creating Physics Fields.) Changing the direction changes the effects of these field types.

The default direction is the vector `{0, -1, 0}`. With this direction, for example, linear gravity fields whose strength is positive cause objects to fall in the “down” direction of scene space.

## See Also

- [var halfExtent: SCNVector3](scnphysicsfield/halfextent.md)
  A location marking the end of the field’s area of effect.
- [var scope: SCNPhysicsFieldScope](scnphysicsfield/scope.md)
  The area affected by the field, either inside or outside its region.
- [var usesEllipsoidalExtent: Bool](scnphysicsfield/usesellipsoidalextent.md)
  A Boolean value that determines whether the field’s area of effect is shaped like a box or ellipsoid.
- [var offset: SCNVector3](scnphysicsfield/offset.md)
  The offset of the field’s center within its area of effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/direction)*