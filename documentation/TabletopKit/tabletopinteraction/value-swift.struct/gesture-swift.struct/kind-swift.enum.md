# TabletopInteraction.Value.Gesture.Kind

**Framework**: TabletopKit  
**Kind**: enum  
**Role**: Enumeration

The possible input sources or modes that can start a gesture interaction.

**Availability**:
- visionOS 2.2+

## Declaration

```swift
enum Kind
```

## Topics

### Gestures
- [TabletopInteraction.Value.Gesture.Kind.directPinch](./kind-swift.enum/directpinch.md)
- [TabletopInteraction.Value.Gesture.Kind.indirectPinch](./kind-swift.enum/indirectpinch.md)

## Relationships

### Conforms To
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Getting the gesture properties
- [var initialInputDevicePose: Pose3D](./initialinputdevicepose.md)
  The pose of the input device at the start of the interaction.
- [var inputDevicePose: Pose3D](./inputdevicepose.md)
  The current pose of the input device.
- [var kind: TabletopInteraction.Value.Gesture.Kind](./kind-swift.property.md)
  The input source or mode which started this gesture.
- [var chirality: TabletopInteraction.Value.Gesture.Chirality?](./chirality-swift.property.md)
  The chirality, or handedness, of this gesture, if known.
- [TabletopInteraction.Value.Gesture.Chirality](./chirality-swift.enum.md)
  The chirality, or handedness, of a gesture.
- [var phase: TabletopInteraction.Value.Phase](./phase.md)
  The current phase of the gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/value-swift.struct/gesture-swift.struct/kind-swift.enum)*