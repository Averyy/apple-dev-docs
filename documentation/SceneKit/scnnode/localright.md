# localRight

**Framework**: SceneKit  
**Kind**: property

The direction SceneKit treats as “right” in local space for all nodes.

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
class var localRight: SCNVector3 { get }
```

#### Discussion

No SceneKit features depend directly on this direction’s definition—it’s simply a natural consequence of recognizing “forward” and “up” directions for use with cameras, directional lighting, and relative orientation operations.

This vector is always `(1, 0, 0)` for all nodes, but you can use this class property when it’s convenient to refer to directions symbolically.

## See Also

- [class var simdLocalRight: simd_float3](scnnode/simdlocalright.md)
  The direction SceneKit treats as “right” in local space for all nodes.
- [class var localUp: SCNVector3](scnnode/localup.md)
  The direction SceneKit treats as “up” in local space for all nodes.
- [class var localFront: SCNVector3](scnnode/localfront.md)
  The unit vector SceneKit treats as “forward” in local space for all nodes.
- [var worldRight: SCNVector3](scnnode/worldright.md)
  The “right” (+X) direction vector relative to the node, expressed in world space.
- [var worldUp: SCNVector3](scnnode/worldup.md)
  The “up” (+Y) direction vector relative to the node, expressed in world space.
- [var worldFront: SCNVector3](scnnode/worldfront.md)
  The “forward” (-Z) direction vector relative to the node, expressed in world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/localright)*