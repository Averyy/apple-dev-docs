# localFront

**Framework**: SceneKit  
**Kind**: property

The unit vector SceneKit treats as “forward” in local space for all nodes.

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
class var localFront: SCNVector3 { get }
```

#### Discussion

The “forward” direction of a node affects cameras and directional lighting attached to a node, as well as relative orientation and movement effects such as [`look(at:)`](scnnode/look(at:).md), [`SCNLookAtConstraint`](scnlookatconstraint.md), and [`SCNBillboardConstraint`](scnbillboardconstraint.md).

This vector is always `(0, 0, -1)` for all nodes, but you can use this class property when it’s convenient to refer to directions symbolically.

## See Also

- [class var simdLocalFront: simd_float3](scnnode/simdlocalfront.md)
  The unit vector SceneKit treats as “forward” in local space for all nodes.
- [class var localRight: SCNVector3](scnnode/localright.md)
  The direction SceneKit treats as “right” in local space for all nodes.
- [class var localUp: SCNVector3](scnnode/localup.md)
  The direction SceneKit treats as “up” in local space for all nodes.
- [var worldRight: SCNVector3](scnnode/worldright.md)
  The “right” (+X) direction vector relative to the node, expressed in world space.
- [var worldUp: SCNVector3](scnnode/worldup.md)
  The “up” (+Y) direction vector relative to the node, expressed in world space.
- [var worldFront: SCNVector3](scnnode/worldfront.md)
  The “forward” (-Z) direction vector relative to the node, expressed in world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/localfront)*