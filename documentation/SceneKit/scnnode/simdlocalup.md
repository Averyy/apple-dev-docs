# simdLocalUp

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
class var simdLocalUp: simd_float3 { get }
```

```objc
@property (class, nonatomic, readonly) simd_float3 simdLocalUp;
```

#### Discussion

The “up” direction of a node affects cameras attached to a node, as well as relative orientation and movement effects such as [`simdLook(at:)`](./simdlook%28at%29.md), [`SCNLookAtConstraint`](../scnlookatconstraint.md), and [`SCNBillboardConstraint`](../scnbillboardconstraint.md).

This vector is always `(0, 1, 0)` for all nodes, but you can use this class property when it’s convenient to refer to directions symbolically.

## See Also

### Related Documentation
- [class var localUp: SCNVector3](./localup.md)
  The direction SceneKit treats as “up” in local space for all nodes.
### Calculating Node-Relative Transforms
- [class var simdLocalRight: simd_float3](./simdlocalright.md)
  The direction SceneKit treats as “right” in local space for all nodes.
- [class var simdLocalFront: simd_float3](./simdlocalfront.md)
  The unit vector SceneKit treats as “forward” in local space for all nodes.
- [var simdWorldRight: simd_float3](./simdworldright.md)
  The “right” (+X) direction vector relative to the node, expressed in world space.
- [var simdWorldUp: simd_float3](./simdworldup.md)
  The “up” (+Y) direction vector relative to the node, expressed in world space.
- [var simdWorldFront: simd_float3](./simdworldfront.md)
  The “forward” (-Z) direction vector relative to the node, expressed in world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdlocalup)*