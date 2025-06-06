# overlap

**Framework**: Model I/O  
**Kind**: property

The amount, as a fraction of image width, by which the images from the camera’s two viewpoints overlap.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var overlap: Float { get set }
```

#### Discussion

Some stereoscopic rendering processes require shifting the location of each viewpoint’s rendered image in a framebuffer before display. Use this property to determine the distance to shift images by during rendering.

## See Also

- [var interPupillaryDistance: Float](mdlstereoscopiccamera/interpupillarydistance.md)
  The distance, in millimeters, between the stereoscopic camera’s two viewpoints.
- [var leftVergence: Float](mdlstereoscopiccamera/leftvergence.md)
  The angle, in degrees, at which the camera’s left viewpoint faces toward a central focal point.
- [var rightVergence: Float](mdlstereoscopiccamera/rightvergence.md)
  The angle, in degrees, at which the camera’s right viewpoint faces toward a central focal point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlstereoscopiccamera/overlap)*