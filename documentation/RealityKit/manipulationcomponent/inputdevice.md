# ManipulationComponent.InputDevice

**Framework**: RealityKit  
**Kind**: struct

Describes an input device like a hand or a trackpad.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct InputDevice
```

## Topics

### Instance Properties
- [var chirality: ManipulationComponent.InputDevice.Chirality?](manipulationcomponent/inputdevice/chirality-swift.property.md)
  The hand chirality (left or right) of this input device, or `nil` if this input device has no hand chirality.
- [var kind: ManipulationComponent.InputDevice.Kind](manipulationcomponent/inputdevice/kind-swift.property.md)
  The kind of this input device.
- [var pose: Pose3DFloat?](manipulationcomponent/inputdevice/pose.md)
  The pose of this input device, or `nil` if this input device has no pose.
### Enumerations
- [ManipulationComponent.InputDevice.Chirality](manipulationcomponent/inputdevice/chirality-swift.enum.md)
  Describes hand chirality (left or right) of an input device.
- [ManipulationComponent.InputDevice.Kind](manipulationcomponent/inputdevice/kind-swift.enum.md)
  Describes the kind of an input device.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationcomponent/inputdevice)*