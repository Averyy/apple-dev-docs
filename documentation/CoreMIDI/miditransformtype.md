# MIDITransformType

**Framework**: Core MIDI  
**Kind**: enum

Values that specify the type of MIDI transformation.

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
enum MIDITransformType
```

## Topics

### Transform Types
- [MIDITransformType.none](miditransformtype/none.md)
  No transformation.
- [MIDITransformType.filterOut](miditransformtype/filterout.md)
  A transformation that filters out an event type.
- [MIDITransformType.mapControl](miditransformtype/mapcontrol.md)
  A transformation that changes a specified control number to a supplied parameter value.
- [MIDITransformType.add](miditransformtype/add.md)
  A transform that adds a parameter value.
- [MIDITransformType.scale](miditransformtype/scale.md)
  A transform that multiplies by the specified parameter value.
- [MIDITransformType.minValue](miditransformtype/minvalue.md)
  A transform that sets the minimum value to the specified parameter value.
- [MIDITransformType.maxValue](miditransformtype/maxvalue.md)
  A transform that sets the maximum value to the specified parameter value.
- [MIDITransformType.mapValue](miditransformtype/mapvalue.md)
  A transform that maps one value to another.
### Initializers
- [init?(rawValue: UInt16)](miditransformtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MIDIValueMap](midivaluemap.md)
  A custom lookup table to transform MIDI 7-bit values, as contained in note numbers, velocities, control values, and so on.
- [struct MIDIControlTransform](midicontroltransform.md)
  A structure that describes the transformation of MIDI control change events.
- [struct MIDITransform](miditransform.md)
  The transformation of a single type of MIDI event.
- [enum MIDITransformControlType](miditransformcontroltype.md)
  A set of values that indicate how to interpret control numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/miditransformtype)*