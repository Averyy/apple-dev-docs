# scope

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The area affected by the field, either inside or outside its region.

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
var scope: SCNPhysicsFieldScope { get set }
```

```objc
@property (nonatomic) SCNPhysicsFieldScope scope;
```

#### Discussion

First, define a field’s region using its [`halfExtent`](./halfextent.md) property and the [`position`](../scnnode/position.md) property of the node containing the field. Then, use the [`scope`](./scope.md) property to choose whether the field’s area of effect is the interior of the region (the default) or all space outside the region.

## See Also

### Specifying a Field’s Area of Effect
- [var halfExtent: SCNVector3](./halfextent.md)
  A location marking the end of the field’s area of effect.
- [var usesEllipsoidalExtent: Bool](./usesellipsoidalextent.md)
  A Boolean value that determines whether the field’s area of effect is shaped like a box or ellipsoid.
- [var offset: SCNVector3](./offset.md)
  The offset of the field’s center within its area of effect.
- [var direction: SCNVector3](./direction.md)
  The field’s directional axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/scope)*