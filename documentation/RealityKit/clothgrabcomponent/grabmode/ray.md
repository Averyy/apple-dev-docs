# ray

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property

Grabbing will be performed using a ray.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static var ray: ClothGrabComponent.GrabMode { get }
```

#### Discussion

The translation of the entity determines the origin of the ray, and the forward vector determines the ray direction.

## See Also

### Creating a grab mode
- [static func volume(shape: ClothVolumeShape) -> ClothGrabComponent.GrabMode](./volume%28shape%29.md)
  Grabbing will be performed using a volume of the given shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothgrabcomponent/grabmode/ray)*