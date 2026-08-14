# ClothGrabComponent.Falloff

**Framework**: RealityKit  
**Kind**: struct

Controls whether grab strength falls off based on particle distance from the volume surface.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Falloff
```

#### Overview

When grabbing particles using a volume, falloff determines how strongly particles are dragged based on their position within the volume. With falloff disabled, all particles inside the volume are dragged with equal strength. With falloff enabled, particles closer to the volume surface are dragged less strongly, producing smoother motion.

## Topics

### Type Properties
- [static var disabled: ClothGrabComponent.Falloff](clothgrabcomponent/falloff-swift.struct/disabled.md)
  No falloff is applied.
- [static var enabled: ClothGrabComponent.Falloff](clothgrabcomponent/falloff-swift.struct/enabled.md)
  Grab strength decreases as particles approach the volume surface.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var falloff: ClothGrabComponent.Falloff](clothgrabcomponent/falloff-swift.property.md)
  Controls whether the grabbing strength falls off based on distance from the volume surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothgrabcomponent/falloff-swift.struct)*