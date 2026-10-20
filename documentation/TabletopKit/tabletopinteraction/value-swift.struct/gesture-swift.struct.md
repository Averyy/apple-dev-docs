# TabletopInteraction.Value.Gesture

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

A structure that provides details specific to a gesture driven interaction.

**Availability**:
- visionOS 2.2+

## Declaration

```swift
struct Gesture
```

## Topics

### Getting the gesture properties
- [var initialInputDevicePose: Pose3D](./gesture-swift.struct/initialinputdevicepose.md)
  The pose of the input device at the start of the interaction.
- [var inputDevicePose: Pose3D](./gesture-swift.struct/inputdevicepose.md)
  The current pose of the input device.
- [var kind: TabletopInteraction.Value.Gesture.Kind](./gesture-swift.struct/kind-swift.property.md)
  The input source or mode which started this gesture.
- [TabletopInteraction.Value.Gesture.Kind](./gesture-swift.struct/kind-swift.enum.md)
  The possible input sources or modes that can start a gesture interaction.
- [var chirality: TabletopInteraction.Value.Gesture.Chirality?](./gesture-swift.struct/chirality-swift.property.md)
  The chirality, or handedness, of this gesture, if known.
- [TabletopInteraction.Value.Gesture.Chirality](./gesture-swift.struct/chirality-swift.enum.md)
  The chirality, or handedness, of a gesture.
- [var phase: TabletopInteraction.Value.Phase](./gesture-swift.struct/phase.md)
  The current phase of the gesture.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the gestures
- [var gesture: TabletopInteraction.Value.Gesture?](./gesture-swift.property.md)
  If this is interaction is currently gesture driven, contains gesture specific additional information


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/value-swift.struct/gesture-swift.struct)*