# init(near:far:fieldOfViewInDegrees:fieldOfViewOrientation:)

**Framework**: RealityKit  
**Kind**: init

Creates a perspective camera component from near and far clipping planes, a field of view, and an orientation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(near: Float = 0.01, far: Float = .infinity, fieldOfViewInDegrees: Float = 60.0, fieldOfViewOrientation: CameraFieldOfViewOrientation = .vertical)
```

## Parameters

- `near`: The minimum distance in meters from the camera that the camera can see.
- `far`: The maximum distance in meters from the camera that the camera can see.
- `fieldOfViewInDegrees`: The camera’s field of view in degrees.
- `fieldOfViewOrientation`: The orientation of the field of view.

## See Also

- [init(near: Float, far: Float, fieldOfViewInDegrees: Float)](perspectivecameracomponent/init(near:far:fieldofviewindegrees:).md)
  Creates a perspective camera component from near and far clipping planes and a field of view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/perspectivecameracomponent/init(near:far:fieldofviewindegrees:fieldofvieworientation:))*