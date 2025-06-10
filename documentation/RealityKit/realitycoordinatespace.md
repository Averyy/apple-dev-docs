# RealityCoordinateSpace

**Framework**: RealityKit  
**Kind**: protocol

A 3D coordinate space that exists within a RealityKit hierarchy.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol RealityCoordinateSpace
```

#### Overview

Any `RealityCoordinateSpaceConverting` can convert spatial data between a [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI) `CoordinateSpace` and a `RealityCoordinateSpace`.

## Topics

### Type Properties
- [static var camera: CameraRealityCoordinateSpace](realitycoordinatespace/camera.md)
  The coordinate space that represents the scene’s active camera.
- [static var scene: SceneRealityCoordinateSpace](realitycoordinatespace/scene.md)
  The coordinate space that represents ARKit world space.

## Relationships

### Conforming Types
- [AnchorEntity](anchorentity.md)
- [BodyTrackedEntity](bodytrackedentity.md)
- [CameraRealityCoordinateSpace](camerarealitycoordinatespace.md)
- [DirectionalLight](directionallight.md)
- [Entity](entity.md)
- [ModelEntity](modelentity.md)
- [PerspectiveCamera](perspectivecamera.md)
- [PointLight](pointlight.md)
- [RealityViewContent](realityviewcontent.md)
- [SceneRealityCoordinateSpace](scenerealitycoordinatespace.md)
- [SpotLight](spotlight.md)
- [TriggerVolume](triggervolume.md)
- [ViewAttachmentEntity](viewattachmententity.md)

## See Also

- [protocol RealityCoordinateSpaceConverting](realitycoordinatespaceconverting.md)
  A value that can be converted between SwiftUI `CoordinateSpace` and RealityKit `Entity`.
- [struct SceneRealityCoordinateSpace](scenerealitycoordinatespace.md)
  The coordinate space that represents the center of a RealityKit scene.
- [struct CameraRealityCoordinateSpace](camerarealitycoordinatespace.md)
  The coordinate space that represents the scene’s active camera.
- [protocol RealityCoordinateSpaceProjecting](realitycoordinatespaceprojecting.md)
  A protocol for coordinate spaces that can project 2D points to and from 3D.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realitycoordinatespace)*