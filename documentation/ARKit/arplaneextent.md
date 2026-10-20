# ARPlaneExtent

**Framework**: ARKit  
**Kind**: class  
**Role**: Class

The size and y-axis rotation of a detected plane.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
class ARPlaneExtent
```

```objc
@interface ARPlaneExtent : NSObject
```

#### Overview

A plane anchor ([`ARPlaneAnchor`](./arplaneanchor.md)) describes its size and orientation on the y-axis using the [`planeExtent`](./arplaneanchor/planeextent.md) property of this type.

At runtime, ARKit continually updates the anchor’s width and height as the framework refines its knowledge of the plane’s shape in the environment.

Similarly, as the session runs, the framework may update the plane’s y-rotation to better fit its rectangular area in the environment. In iOS 15 and earlier, the framework rotates the plane anchor according to that angle. In iOS 16, the framework doesn’t rotate the anchor automatically and its transform matrix remains unchanged. Instead, the framework exposes the angle [`rotationOnYAxis`](./arplaneextent/rotationonyaxis.md) that you apply to any plane extent geometry in your app.

> ❗ **Important**:  Apps that run on iOS 16 with a deployment target less than iOS 16 preserve the prior y-axis rotation behavior.

##### Size and Rotate an Entity to a Plane’s Extent

The following code defines a RealityKit entity sized to the plane extent’s width and height. The helper function also applies the extent’s suggested y-axis rotation by setting its transform `yaw` value to [`rotationOnYAxis`](./arplaneextent/rotationonyaxis.md).

```swift
func createPlane(for planeAnchor: ARPlaneAnchor, material: Material) -> ModelEntity {

    // Get the plane's extent.
    let extent = planeAnchor.planeExtent

    // Create a model entity sized to the plane's extent.
    let planeEntity = ModelEntity(mesh: .generatePlane (width: extent.width, depth: extent.height),
        materials: [material])

    // Orient the entity according to the extent's y-axis rotation.
    planeEntity.transform = Transform(pitch: 0, yaw: extent.rotationOnYAxis, roll: 0)

    // Center the entity on the plane.
    planeEntity.transform.translation = planeAnchor.center

    return planeEntity
}
```

## Topics

### Inspecting Plane Size
- [var width: Float](./arplaneextent/width.md)
  The estimated width of the plane.
- [var height: Float](./arplaneextent/height.md)
  The estimated height of the plane.
### Inspecting Plane Y-Rotation
- [var rotationOnYAxis: Float](./arplaneextent/rotationonyaxis.md)
  A radian value that indicates a plane’s y-axis orientation.
### Initializers
- [init?(coder: NSCoder)](./arplaneextent/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Dimensions
- [var center: simd_float3](./arplaneanchor/center.md)
  The center point of the plane relative to its anchor position.
- [var planeExtent: ARPlaneExtent](./arplaneanchor/planeextent.md)
  The estimated width, length, and y-axis rotation of the detected plane.
- [var extent: simd_float3](./arplaneanchor/extent.md)
  The estimated width and length of the detected plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneextent)*