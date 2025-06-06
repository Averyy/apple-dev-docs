# init(device:)

**Framework**: ARKit  
**Kind**: init

Creates a SceneKit face geometry for rendering with the specified Metal device object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
convenience init?(device: any MTLDevice)
```

#### Return Value

A new SceneKit face geometry, or `nil` if the Metal device is unavailable or ARKit face tracking is not supported on the current device.

#### Discussion

A newly created [`ARSCNFaceGeometry`](arscnfacegeometry.md) instance represents a neutral, generic face; use the [`update(from:)`](arscnfacegeometry/update(from:).md) method to deform the geometry to match a specific facial expression or face shape.

The geometry contains a single geometry element; as such, assigning more than one material has no visible effect (see the inherited [`materials`](https://developer.apple.com/documentation/scenekit/scngeometry/1523472-materials) property).

Calling this initializer is equivalent to calling the [`init(device:fillMesh:)`](arscnfacegeometry/init(device:fillmesh:).md) initializer and passing [`false`](https://developer.apple.com/documentation/swift/false) for the `fillMesh` parameter.

## Parameters

- `device`: The Metal device to use for rendering the geometry.

## See Also

- [convenience init?(device: any MTLDevice, fillMesh: Bool)](arscnfacegeometry/init(device:fillmesh:).md)
  Creates a SceneKit face geometry, optionally filling in gaps in the mesh for the eyes and mouth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnfacegeometry/init(device:))*