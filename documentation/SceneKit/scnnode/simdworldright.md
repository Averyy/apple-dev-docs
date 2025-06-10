# simdWorldRight

**Framework**: SceneKit  
**Kind**: property

The “right” (+X) direction vector relative to the node, expressed in world space.

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
var simdWorldRight: simd_float3 { get }
```

#### Discussion

Reading this property is equivalent to reading the [`simdLocalRight`](scnnode/simdlocalright.md) class property and using the [`simdConvertVector(_:to:)`](scnnode/simdconvertvector(_:to:).md) or [`simdConvertVector(_:from:)`](scnnode/simdconvertvector(_:from:).md) method to convert that vector from the node’s local coordinate space to the scene’s world coordinate space.

## See Also

- [var worldRight: SCNVector3](scnnode/worldright.md)
  The “right” (+X) direction vector relative to the node, expressed in world space.
- [class var simdLocalRight: simd_float3](scnnode/simdlocalright.md)
  The direction SceneKit treats as “right” in local space for all nodes.
- [class var simdLocalUp: simd_float3](scnnode/simdlocalup.md)
  The direction SceneKit treats as “up” in local space for all nodes.
- [class var simdLocalFront: simd_float3](scnnode/simdlocalfront.md)
  The unit vector SceneKit treats as “forward” in local space for all nodes.
- [var simdWorldUp: simd_float3](scnnode/simdworldup.md)
  The “up” (+Y) direction vector relative to the node, expressed in world space.
- [var simdWorldFront: simd_float3](scnnode/simdworldfront.md)
  The “forward” (-Z) direction vector relative to the node, expressed in world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdworldright)*