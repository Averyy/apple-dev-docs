# leftVergence

**Framework**: Model I/O  
**Kind**: property

The angle, in degrees, at which the camera’s left viewpoint faces toward a central focal point.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var leftVergence: Float { get set }
```

#### Discussion

A stereoscopic camera simulates binocular vision by looking toward a central point in a scene from two slightly different viewpoints. Vergence measures the difference between the camera’s forward axis and the angle from each viewpoint toward that central point, called the . There are two common ways to model a stereoscopic camera:

- In a toed-in camera, each simulated lens and imaging surface is rotated (by the [`leftVergence`](mdlstereoscopiccamera/leftvergence.md) and [`rightVergence`](mdlstereoscopiccamera/rightvergence.md) angles) to face toward the focal point. That is, a line from the focal point through the center of the lens reaches the center of the imaging surface and is perpendicular to the image plane.
- In a parallel stereoscopic camera, the imaging surfaces are perpendicular to the camera’s forward axis and are shifted horizontally relative to the center of each lens. The distance by which each imaging surface shifts is given by the following formula:

`shift = (focalLength * interPupillaryDistance) / distanceToVergencePoint`

## See Also

- [var interPupillaryDistance: Float](mdlstereoscopiccamera/interpupillarydistance.md)
  The distance, in millimeters, between the stereoscopic camera’s two viewpoints.
- [var overlap: Float](mdlstereoscopiccamera/overlap.md)
  The amount, as a fraction of image width, by which the images from the camera’s two viewpoints overlap.
- [var rightVergence: Float](mdlstereoscopiccamera/rightvergence.md)
  The angle, in degrees, at which the camera’s right viewpoint faces toward a central focal point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlstereoscopiccamera/leftvergence)*