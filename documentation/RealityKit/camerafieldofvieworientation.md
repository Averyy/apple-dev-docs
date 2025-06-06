# CameraFieldOfViewOrientation

**Framework**: RealityKit  
**Kind**: enum

The orientations that a camera’s field-of-view degrees can apply.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum CameraFieldOfViewOrientation
```

## Topics

### Operators
- [static func == (CameraFieldOfViewOrientation, CameraFieldOfViewOrientation) -> Bool](camerafieldofvieworientation/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [CameraFieldOfViewOrientation.horizontal](camerafieldofvieworientation/horizontal.md)
  Applies the field-of-view degrees in the camera’s horizontal axis.
- [CameraFieldOfViewOrientation.vertical](camerafieldofvieworientation/vertical.md)
  Applies the field-of-view degrees in the camera’s vertical axis.
### Instance Properties
- [var hashValue: Int](camerafieldofvieworientation/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](camerafieldofvieworientation/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](camerafieldofvieworientation/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct PerspectiveCameraComponent](perspectivecameracomponent.md)
  A component that defines a virtual camera and its controls.
- [struct OrthographicCameraComponent](orthographiccameracomponent.md)
  A component that defines an orthographic virtual camera and its settings.
- [struct ProjectiveTransformCameraComponent](projectivetransformcameracomponent.md)
  A component that defines a virtual camera with a custom projection matrix.
- [class PerspectiveCamera](perspectivecamera.md)
  A virtual camera that establishes the rendering perspective.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/camerafieldofvieworientation)*