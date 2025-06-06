# frameBoundingBox(_:setNearAndFar:)

**Framework**: Model I/O  
**Kind**: method

Moves the camera such that the specified bounding box lies entirely within the camera’s field of view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func frameBoundingBox(_ boundingBox: MDLAxisAlignedBoundingBox, setNearAndFar: Bool)
```

#### Discussion

When calculating the new camera position and orientation, this method assumes the camera points in the negative z-axis direction and that the positive y-axis represents the up direction for the camera’s view.

## Parameters

- `boundingBox`: The region, in world space coordinates, to be made visible to the camera.
- `setNearAndFar`: If  , the camera also adjusts its   and   properties to place the specified region entirely within the camera’s viewing frustum. If  , those properties remain unchanged, and the specified region may therefore lie outside the camera’s near and far limits.

## See Also

- [func look(at: vector_float3)](mdlcamera/look(at:).md)
  Orients the camera to face toward the specified point.
- [func look(at: vector_float3, from: vector_float3)](mdlcamera/look(at:from:).md)
  Sets the camera’s position and orients the camera to face toward the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcamera/frameboundingbox(_:setnearandfar:))*