# ClothGrabComponent.GrabMode

**Framework**: RealityKit  
**Kind**: struct

Defines whether a grab component will select particles using a ray or a volume.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct GrabMode
```

## Topics

### Creating a grab mode
- [static var ray: ClothGrabComponent.GrabMode](clothgrabcomponent/grabmode/ray.md)
  Grabbing will be performed using a ray.
- [static func volume(shape: ClothVolumeShape) -> ClothGrabComponent.GrabMode](clothgrabcomponent/grabmode/volume(shape:).md)
  Grabbing will be performed using a volume of the given shape.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(mode: ClothGrabComponent.GrabMode)](clothgrabcomponent/init(mode:).md)
  Creates a cloth grab component with the given grab mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothgrabcomponent/grabmode)*