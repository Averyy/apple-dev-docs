# SceneRealityCoordinateSpace

**Framework**: RealityKit  
**Kind**: struct

The coordinate space that represents the center of a RealityKit scene.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct SceneRealityCoordinateSpace
```

#### Overview

The center, or origin, of a RealityKit scene varies depending on the platform and context:

> **Note**: This object is equivalent to [`scene`](realitycoordinatespace/scene.md).

## Topics

### Initializers
- [init()](scenerealitycoordinatespace/init.md)
  Creates a scene coordinate space.

## Relationships

### Conforms To
- [RealityCoordinateSpace](realitycoordinatespace.md)

## See Also

- [protocol RealityCoordinateSpaceConverting](realitycoordinatespaceconverting.md)
  A value that can be converted between SwiftUI `CoordinateSpace` and RealityKit `Entity`.
- [struct CameraRealityCoordinateSpace](camerarealitycoordinatespace.md)
  The coordinate space that represents the scene’s active camera.
- [protocol RealityCoordinateSpace](realitycoordinatespace.md)
  A 3D coordinate space that exists within a RealityKit hierarchy.
- [protocol RealityCoordinateSpaceProjecting](realitycoordinatespaceprojecting.md)
  A protocol for coordinate spaces that can project 2D points to and from 3D.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scenerealitycoordinatespace)*