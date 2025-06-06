# look(at:from:)

**Framework**: Model I/O  
**Kind**: method

Sets the camera’s position and orients the camera to face toward the specified point.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func look(at focusPosition: vector_float3, from cameraPosition: vector_float3)
```

#### Discussion

When calculating the new camera position and orientation, this method assumes the camera points in the negative z-axis direction and that the positive y-axis represents the up direction for the camera’s view.

## Parameters

- `focusPosition`: The point, in world space coordinates, to be made visible to the camera.
- `cameraPosition`: The new position, in world space coordinates, for the camera.

## See Also

- [func frameBoundingBox(MDLAxisAlignedBoundingBox, setNearAndFar: Bool)](mdlcamera/frameboundingbox(_:setnearandfar:).md)
  Moves the camera such that the specified bounding box lies entirely within the camera’s field of view.
- [func look(at: vector_float3)](mdlcamera/look(at:).md)
  Orients the camera to face toward the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcamera/look(at:from:))*