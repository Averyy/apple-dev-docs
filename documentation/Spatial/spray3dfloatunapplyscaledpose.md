# SPRay3DFloatUnapplyScaledPose

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```c
static SPRay3DFloat SPRay3DFloatUnapplyScaledPose(SPRay3DFloat ray, SPScaledPose3DFloat pose);
```

#### Return Value

The transformed ray.

#### Discussion

Returns a ray that’s transformed by the inverse of the specified scaled pose.

> **Note**: This function rotates the ray’s direction by the pose’s rotation and offsets the ray’s origin by the pose’s position.

## Parameters

- `ray`: The source ray.
- `pose`: The scaled pose that the function unapplies to the ray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spray3dfloatunapplyscaledpose)*