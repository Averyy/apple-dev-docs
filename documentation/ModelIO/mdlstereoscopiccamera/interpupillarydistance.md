# interPupillaryDistance

**Framework**: Model I/O  
**Kind**: property

The distance, in millimeters, between the stereoscopic camera’s two viewpoints.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var interPupillaryDistance: Float { get set }
```

#### Discussion

Each viewpoint is assumed to be horizontally offset from the camera’s position by half the interocular distance.

## See Also

- [var overlap: Float](mdlstereoscopiccamera/overlap.md)
  The amount, as a fraction of image width, by which the images from the camera’s two viewpoints overlap.
- [var leftVergence: Float](mdlstereoscopiccamera/leftvergence.md)
  The angle, in degrees, at which the camera’s left viewpoint faces toward a central focal point.
- [var rightVergence: Float](mdlstereoscopiccamera/rightvergence.md)
  The angle, in degrees, at which the camera’s right viewpoint faces toward a central focal point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlstereoscopiccamera/interpupillarydistance)*