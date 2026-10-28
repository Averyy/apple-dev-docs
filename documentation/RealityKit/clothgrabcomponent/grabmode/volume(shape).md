# volume(shape:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Grabbing will be performed using a volume of the given shape.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func volume(shape: ClothVolumeShape) -> ClothGrabComponent.GrabMode
```

## Return Value

A volume-based grab mode.

## Parameters

- `shape`: The shape of the volume used to select and drag particles.

## See Also

### Creating a grab mode
- [static var ray: ClothGrabComponent.GrabMode](./ray.md)
  Grabbing will be performed using a ray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothgrabcomponent/grabmode/volume(shape:))*