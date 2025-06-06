# targets

**Framework**: SceneKit  
**Kind**: property

The array of target geometries to morph between.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var targets: [SCNGeometry] { get set }
```

#### Discussion

An array of [`SCNGeometry`](scngeometry.md) objects.

A morpher blends between a base geometry, specified in the [`geometry`](scnnode/geometry.md) property of the node the morpher is attached to, and one or more target geometries. The base geometry and all target geometries must be topologically identical—that is, they must contain the same number and structural arrangement of vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmorpher/targets)*