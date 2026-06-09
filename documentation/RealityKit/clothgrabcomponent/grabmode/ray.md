# ray

**Framework**: RealityKit  
**Kind**: property

Grabbing will be performed using a ray.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var ray: ClothGrabComponent.GrabMode { get }
```

#### Discussion

The translation of the entity determines the origin of the ray, and the forward vector determines the ray direction.

## See Also

- [static func volume(shape: ClothVolumeShape) -> ClothGrabComponent.GrabMode](clothgrabcomponent/grabmode/volume(shape:).md)
  Grabbing will be performed using a volume of the given shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothgrabcomponent/grabmode/ray)*