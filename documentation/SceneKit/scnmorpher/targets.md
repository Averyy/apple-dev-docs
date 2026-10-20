# targets

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The array of target geometries to morph between.

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
var targets: [SCNGeometry] { get set }
```

```objc
@property (nonatomic, copy) NSArray<SCNGeometry *> * targets;
```

#### Discussion

An array of [`SCNGeometry`](../scngeometry.md) objects.

A morpher blends between a base geometry, specified in the [`geometry`](../scnnode/geometry.md) property of the node the morpher is attached to, and one or more target geometries. The base geometry and all target geometries must be topologically identical—that is, they must contain the same number and structural arrangement of vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmorpher/targets)*