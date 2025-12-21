# fieldOfViewOrientation

**Framework**: RealityKit  
**Kind**: property

The orientation with which the system uses to apply the field-of-view degrees.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var fieldOfViewOrientation: CameraFieldOfViewOrientation
```

#### Discussion

The value of this property determines the orientation that the system uses to apply the [`fieldOfViewInDegrees`](perspectivecameracomponent/fieldofviewindegrees.md) value.

This property defaults to [`CameraFieldOfViewOrientation.vertical`](camerafieldofvieworientation/vertical.md).

## See Also

- [var fieldOfViewInDegrees: Float](perspectivecameracomponent/fieldofviewindegrees.md)
  The camera’s total field of view in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/perspectivecameracomponent/fieldofvieworientation)*