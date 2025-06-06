# simdLocalUp

**Framework**: SceneKit  
**Kind**: property

The direction SceneKit treats as “up” in local space for all nodes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class var simdLocalUp: simd_float3 { get }
```

#### Discussion

The “up” direction of a node affects cameras attached to a node, as well as relative orientation and movement effects such as [`simdLook(at:)`](scnnode/simdlook(at:).md), [`SCNLookAtConstraint`](scnlookatconstraint.md), and [`SCNBillboardConstraint`](scnbillboardconstraint.md).

This vector is always `(0, 1, 0)` for all nodes, but you can use this class property when it’s convenient to refer to directions symbolically.

## See Also

- [class var localUp: SCNVector3](scnnode/localup.md)
  The direction SceneKit treats as “up” in local space for all nodes.
- [class var simdLocalRight: simd_float3](scnnode/simdlocalright.md)
  The direction SceneKit treats as “right” in local space for all nodes.
- [class var simdLocalFront: simd_float3](scnnode/simdlocalfront.md)
  The unit vector SceneKit treats as “forward” in local space for all nodes.
- [var simdWorldRight: simd_float3](scnnode/simdworldright.md)
  The “right” (+X) direction vector relative to the node, expressed in world space.
- [var simdWorldUp: simd_float3](scnnode/simdworldup.md)
  The “up” (+Y) direction vector relative to the node, expressed in world space.
- [var simdWorldFront: simd_float3](scnnode/simdworldfront.md)
  The “forward” (-Z) direction vector relative to the node, expressed in world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdlocalup)*