# initialInputDevicePose

**Framework**: TabletopKit  
**Kind**: property  
**Role**: Instance Property

The pose of the input device at the start of the interaction.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
var initialInputDevicePose: Pose3D { get }
```

## See Also

### Getting the gesture properties
- [var inputDevicePose: Pose3D](./inputdevicepose.md)
  The current pose of the input device.
- [var kind: TabletopInteraction.Value.Gesture.Kind](./kind-swift.property.md)
  The input source or mode which started this gesture.
- [TabletopInteraction.Value.Gesture.Kind](./kind-swift.enum.md)
  The possible input sources or modes that can start a gesture interaction.
- [var chirality: TabletopInteraction.Value.Gesture.Chirality?](./chirality-swift.property.md)
  The chirality, or handedness, of this gesture, if known.
- [TabletopInteraction.Value.Gesture.Chirality](./chirality-swift.enum.md)
  The chirality, or handedness, of a gesture.
- [var phase: TabletopInteraction.Value.Phase](./phase.md)
  The current phase of the gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/value-swift.struct/gesture-swift.struct/initialinputdevicepose)*