# localUp

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

The direction SceneKit treats as “up” in local space for all nodes.

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
class var localUp: SCNVector3 { get }
```

```objc
@property (class, nonatomic, readonly) SCNVector3 localUp;
```

#### Discussion

The “up” direction of a node affects cameras attached to a node, as well as relative orientation and movement effects such as [`look(at:)`](./look%28at%29.md), [`SCNLookAtConstraint`](../scnlookatconstraint.md), and [`SCNBillboardConstraint`](../scnbillboardconstraint.md).

This vector is always `(0, 1, 0)` for all nodes, but you can use this class property when it’s convenient to refer to directions symbolically.

## See Also

### Related Documentation
- [class var simdLocalUp: simd_float3](./simdlocalup.md)
  The direction SceneKit treats as “up” in local space for all nodes.
### Calculating Node-Relative Transforms (SceneKit Types)
- [class var localRight: SCNVector3](./localright.md)
  The direction SceneKit treats as “right” in local space for all nodes.
- [class var localFront: SCNVector3](./localfront.md)
  The unit vector SceneKit treats as “forward” in local space for all nodes.
- [var worldRight: SCNVector3](./worldright.md)
  The “right” (+X) direction vector relative to the node, expressed in world space.
- [var worldUp: SCNVector3](./worldup.md)
  The “up” (+Y) direction vector relative to the node, expressed in world space.
- [var worldFront: SCNVector3](./worldfront.md)
  The “forward” (-Z) direction vector relative to the node, expressed in world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/localup)*