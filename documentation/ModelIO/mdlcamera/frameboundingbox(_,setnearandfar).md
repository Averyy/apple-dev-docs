# frameBoundingBox(_:setNearAndFar:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) frameBoundingBox:(MDLAxisAlignedBoundingBox) boundingBox setNearAndFar:(BOOL) setNearAndFar;
```

#### Discussion

When calculating the new camera position and orientation, this method assumes the camera points in the negative z-axis direction and that the positive y-axis represents the up direction for the camera’s view.

## Parameters

- `boundingBox`: The region, in world space coordinates, to be made visible to the camera.
- `setNearAndFar`: If [`true`](../../Swift/true.md), the camera also adjusts its [`nearVisibilityDistance`](./nearvisibilitydistance.md) and [`farVisibilityDistance`](./farvisibilitydistance.md) properties to place the specified region entirely within the camera’s viewing frustum. If [`false`](../../Swift/false.md), those properties remain unchanged, and the specified region may therefore lie outside the camera’s near and far limits.

## See Also

### Managing Camera Position and Orientation
- [func look(at: vector_float3)](./look%28at%29.md)
  Orients the camera to face toward the specified point.
- [func look(at: vector_float3, from: vector_float3)](./look%28at,from%29.md)
  Sets the camera’s position and orients the camera to face toward the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcamera/frameboundingbox(_:setnearandfar:))*