# fieldOfViewInDegrees

**Framework**: RealityKit  
**Kind**: property

The camera’s total field of view in degrees.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var fieldOfViewInDegrees: Float
```

#### Discussion

This property contains the entire field of view for the camera in degrees.

When you set [`fieldOfViewOrientation`](perspectivecameracomponent/fieldofvieworientation.md) to [`CameraFieldOfViewOrientation.vertical`](camerafieldofvieworientation/vertical.md), this value sets the vertical field of view for the camera in degrees, and the system automatically calculates the horizontal field of view to fit the aspect ratio of the device’s screen.

This property defaults to `60` degrees.

## See Also

- [var fieldOfViewOrientation: CameraFieldOfViewOrientation](perspectivecameracomponent/fieldofvieworientation.md)
  The orientation with which the system uses to apply the field-of-view degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/perspectivecameracomponent/fieldofviewindegrees)*