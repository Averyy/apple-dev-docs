# init(device:)

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Creates a SceneKit face geometry for rendering with the specified Metal device object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
convenience init?(device: any MTLDevice)
```

```objc
+ (instancetype) faceGeometryWithDevice:(id<MTLDevice>) device;
```

#### Return Value

A new SceneKit face geometry, or `nil` if the Metal device is unavailable or ARKit face tracking is not supported on the current device.

#### Discussion

A newly created [`ARSCNFaceGeometry`](../arscnfacegeometry.md) instance represents a neutral, generic face; use the [`update(from:)`](./update%28from%29.md) method to deform the geometry to match a specific facial expression or face shape.

The geometry contains a single geometry element; as such, assigning more than one material has no visible effect (see the inherited [`materials`](../../SceneKit/scngeometry/materials.md) property).

Calling this initializer is equivalent to calling the [`init(device:fillMesh:)`](./init%28device,fillmesh%29.md) initializer and passing [`false`](../../Swift/false.md) for the `fillMesh` parameter.

## Parameters

- `device`: The Metal device to use for rendering the geometry.

## See Also

### Creating a Geometry
- [convenience init?(device: any MTLDevice, fillMesh: Bool)](./init%28device,fillmesh%29.md)
  Creates a SceneKit face geometry, optionally filling in gaps in the mesh for the eyes and mouth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnfacegeometry/init(device:))*