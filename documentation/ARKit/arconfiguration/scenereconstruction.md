# ARConfiguration.SceneReconstruction

**Framework**: ARKit  
**Kind**: struct

Options that enable ARKit to detect the shape of the physical environment.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
struct SceneReconstruction
```

#### Overview

When you set one of the these values onto a world-tracking configuration’s [`sceneReconstruction`](arworldtrackingconfiguration/scenereconstruction.md) property, ARKit provides you with a mesh that models the real-world surrounding the user.

## Topics

### Modeling the Environment
- [init(rawValue: UInt)](arconfiguration/scenereconstruction/init(rawvalue:).md)
  Initializes a scene-reconstruction object.
- [static var mesh: ARConfiguration.SceneReconstruction](arconfiguration/scenereconstruction/mesh.md)
  A polygonal mesh approximation of the physical environment.
- [static var meshWithClassification: ARConfiguration.SceneReconstruction](arconfiguration/scenereconstruction/meshwithclassification.md)
  An approximate shape of the physical environment, including classification of the real-world objects within it.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/scenereconstruction)*