# offset

**Framework**: SceneKit  
**Kind**: property

The offset of the field’s center within its area of effect.

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
var offset: SCNVector3 { get set }
```

#### Discussion

Some types of fields apply forces whose magnitude is relative to the distance between an object and the field’s center. (For details on each type of field, see the methods listed in Creating Physics Fields.) Changing the offset changes the effects of these field types.

With the default offset vector `{0, 0, 0}`, the center of a field is the center of its area of effect.

## See Also

- [var halfExtent: SCNVector3](scnphysicsfield/halfextent.md)
  A location marking the end of the field’s area of effect.
- [var scope: SCNPhysicsFieldScope](scnphysicsfield/scope.md)
  The area affected by the field, either inside or outside its region.
- [var usesEllipsoidalExtent: Bool](scnphysicsfield/usesellipsoidalextent.md)
  A Boolean value that determines whether the field’s area of effect is shaped like a box or ellipsoid.
- [var direction: SCNVector3](scnphysicsfield/direction.md)
  The field’s directional axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/offset)*