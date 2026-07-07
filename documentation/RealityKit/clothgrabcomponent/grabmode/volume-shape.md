# volume(shape:)

**Framework**: RealityKit  
**Kind**: method

Grabbing will be performed using a volume of the given shape.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func volume(shape: ClothVolumeShape) -> ClothGrabComponent.GrabMode
```

#### Return Value

A volume-based grab mode.

## Parameters

- `shape`: The shape of the volume used to select and drag particles.

## See Also

- [static var ray: ClothGrabComponent.GrabMode](clothgrabcomponent/grabmode/ray.md)
  Grabbing will be performed using a ray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothgrabcomponent/grabmode/volume(shape:))*