# Manipulable.InputDevice

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Describes an input device like a hand or a trackpad.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct InputDevice
```

## Topics

### Instance Properties
- [let chirality: Manipulable.InputDevice.Chirality?](./inputdevice/chirality-swift.property.md)
  The hand chirality (left or right) of this input device, or `nil` if this input device has no hand chirality.
- [let kind: Manipulable.InputDevice.Kind](./inputdevice/kind-swift.property.md)
  The kind of this input device.
- [let pose: Pose3D?](./inputdevice/pose.md)
  The pose of this input device, or `nil` if this input device has no pose.
### Enumerations
- [Manipulable.InputDevice.Chirality](./inputdevice/chirality-swift.enum.md)
  Describes hand chirality (left or right) of an input device.
- [Manipulable.InputDevice.Kind](./inputdevice/kind-swift.enum.md)
  Describes the kind of an input device.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/manipulable/inputdevice)*