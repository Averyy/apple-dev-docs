# ClothGrabComponent.GrabMode

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Defines whether a grab component will select particles using a ray or a volume.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct GrabMode
```

## Topics

### Creating a grab mode
- [static var ray: ClothGrabComponent.GrabMode](./grabmode/ray.md)
  Grabbing will be performed using a ray.
- [static func volume(shape: ClothVolumeShape) -> ClothGrabComponent.GrabMode](./grabmode/volume%28shape%29.md)
  Grabbing will be performed using a volume of the given shape.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a grab component
- [init(mode: ClothGrabComponent.GrabMode)](./init%28mode%29.md)
  Creates a cloth grab component with the given grab mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothgrabcomponent/grabmode)*