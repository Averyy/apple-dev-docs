# MIDITransform

**Framework**: Core MIDI  
**Kind**: struct

The transformation of a single type of MIDI event.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct MIDITransform
```

## Topics

### Configuring a Transform
- [var param: Int16](miditransform/param.md)
  An argument to the transformation method (see description of MIDITransformType).
- [var transform: MIDITransformType](miditransform/transform.md)
  The type of transformation to apply to the event values.
### Initializers
- [init()](miditransform/init.md)
- [init(transform: MIDITransformType, param: Int16)](miditransform/init(transform:param:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MIDIValueMap](midivaluemap.md)
  A custom lookup table to transform MIDI 7-bit values, as contained in note numbers, velocities, control values, and so on.
- [struct MIDIControlTransform](midicontroltransform.md)
  A structure that describes the transformation of MIDI control change events.
- [enum MIDITransformType](miditransformtype.md)
  Values that specify the type of MIDI transformation.
- [enum MIDITransformControlType](miditransformcontroltype.md)
  A set of values that indicate how to interpret control numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/miditransform)*