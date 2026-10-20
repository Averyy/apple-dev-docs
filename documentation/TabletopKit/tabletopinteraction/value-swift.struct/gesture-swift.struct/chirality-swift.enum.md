# TabletopInteraction.Value.Gesture.Chirality

**Framework**: TabletopKit  
**Kind**: enum  
**Role**: Enumeration

The chirality, or handedness, of a gesture.

**Availability**:
- visionOS 2.2+

## Declaration

```swift
enum Chirality
```

## Topics

### Handedness
- [TabletopInteraction.Value.Gesture.Chirality.left](./chirality-swift.enum/left.md)
  Indicates a left-handed gesture.
- [TabletopInteraction.Value.Gesture.Chirality.right](./chirality-swift.enum/right.md)
  Indicates a right-handed gesture.

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
- [TabletopInteraction.Value.Gesture.Kind](./kind-swift.enum.md)
  The possible input sources or modes that can start a gesture interaction.
- [var chirality: TabletopInteraction.Value.Gesture.Chirality?](./chirality-swift.property.md)
  The chirality, or handedness, of this gesture, if known.
- [var phase: TabletopInteraction.Value.Phase](./phase.md)
  The current phase of the gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/value-swift.struct/gesture-swift.struct/chirality-swift.enum)*