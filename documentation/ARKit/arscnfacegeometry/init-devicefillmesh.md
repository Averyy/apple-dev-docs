# init(device:fillMesh:)

**Framework**: ARKit  
**Kind**: init

Creates a SceneKit face geometry, optionally filling in gaps in the mesh for the eyes and mouth.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
convenience init?(device: any MTLDevice, fillMesh: Bool)
```

#### Return Value

A new SceneKit face geometry, or `nil` if the Metal device is unavailable or ARKit face tracking is not supported on the current device.

#### Discussion

A newly created [`ARSCNFaceGeometry`](arscnfacegeometry.md) instance represents a neutral, generic face; use the [`update(from:)`](arscnfacegeometry/update(from:).md) method to deform the geometry to match a specific facial expression or face shape.

If the `fillMesh` parameter is [`false`](https://developer.apple.com/documentation/swift/false), the geometry contains a single geometry element. If the `fillMesh` parameter is [`true`](https://developer.apple.com/documentation/swift/true), the geometry contains four elements in the following order: the face itself, the left and right eyes, and the mouth. (When a SceneKit geometry contains multiple elements, the number and order of materials you assign to its [`materials`](https://developer.apple.com/documentation/scenekit/scngeometry/materials) array determines whether the entire surface has a uniform appearance or different appearances for each geometry element.)

## Parameters

- `device`: The Metal device to use for rendering the geometry.
- `fillMesh`: If [`false`](https://developer.apple.com/documentation/swift/false), the mesh doesn’t include the eye and mouth areas of the face topology—as a result, if you render the face geometry for a face anchor atop the camera feed in an AR session, the user’s eyes and the inside of the user’s mouth (when open) are visible through the gaps in the 3D model. If [`true`](https://developer.apple.com/documentation/swift/true), the mesh fills in the gaps for the eyes and mouth. This option can be useful when using the face geometry for occlusion only—that is, to prevent other 3D content from rendering behind it, while still showing the camera image beneath.

## See Also

- [convenience init?(device: any MTLDevice)](arscnfacegeometry/init(device:).md)
  Creates a SceneKit face geometry for rendering with the specified Metal device object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnfacegeometry/init(device:fillmesh:))*