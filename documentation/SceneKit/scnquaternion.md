# SCNQuaternion

**Framework**: SceneKit  
**Kind**: typealias

A representation of a quaternion.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias SCNQuaternion = SCNVector4
```

#### Discussion

A quaternion is a mathematical construct useful for describing rotations in three-dimensional space. Although its implementation differs from that of a 4-component vector, you specify a quaternion value using the same fields as an `SCNVector4` structure.

SceneKit uses unit quaternions (those whose components satisfy the equation `x*x + y*y + z*z + w*w == 1`) for the [`orientation`](scnnode/orientation.md) property of nodes.

## See Also

- [struct SCNMatrix4](scnmatrix4-swift.struct.md)
  A representation of a 4 x 4 matrix.
- [typealias SCNMatrix4](scnmatrix4-swift.typealias.md)
  A representation of a 4 x 4 matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnquaternion)*