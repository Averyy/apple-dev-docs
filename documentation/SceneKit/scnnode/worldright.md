# worldRight

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
var worldRight: SCNVector3 { get }
```

#### Discussion

Reading this property is equivalent to reading the [`localRight`](scnnode/localright.md) class property and using the [`convertVector(_:to:)`](scnnode/convertvector(_:to:).md) or [`convertVector(_:from:)`](scnnode/convertvector(_:from:).md) method to convert that vector from the node’s local coordinate space to the scene’s world coordinate space.

## See Also

- [var simdWorldRight: simd_float3](scnnode/simdworldright.md)
  The “right” (+X) direction vector relative to the node, expressed in world space.
- [class var localRight: SCNVector3](scnnode/localright.md)
  The direction SceneKit treats as “right” in local space for all nodes.
- [class var localUp: SCNVector3](scnnode/localup.md)
  The direction SceneKit treats as “up” in local space for all nodes.
- [class var localFront: SCNVector3](scnnode/localfront.md)
  The unit vector SceneKit treats as “forward” in local space for all nodes.
- [var worldUp: SCNVector3](scnnode/worldup.md)
  The “up” (+Y) direction vector relative to the node, expressed in world space.
- [var worldFront: SCNVector3](scnnode/worldfront.md)
  The “forward” (-Z) direction vector relative to the node, expressed in world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/worldright)*