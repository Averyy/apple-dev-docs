# ARConfiguration.SceneReconstruction

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

Options that enable ARKit to detect the shape of the physical environment.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+

## Declaration

```swift
struct SceneReconstruction
```

```c
enum ARSceneReconstruction : NSUInteger;
```

#### Overview

When you set one of the these values onto a world-tracking configuration’s [`sceneReconstruction`](../arworldtrackingconfiguration/scenereconstruction.md) property, ARKit provides you with a mesh that models the real-world surrounding the user.

## Topics

### Modeling the Environment
- [init(rawValue: UInt)](./scenereconstruction/init%28rawvalue%29.md)
  Initializes a scene-reconstruction object.
- [static var mesh: ARConfiguration.SceneReconstruction](./scenereconstruction/mesh.md)
  A polygonal mesh approximation of the physical environment.
- [static var meshWithClassification: ARConfiguration.SceneReconstruction](./scenereconstruction/meshwithclassification.md)
  An approximate shape of the physical environment, including classification of the real-world objects within it.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/scenereconstruction)*