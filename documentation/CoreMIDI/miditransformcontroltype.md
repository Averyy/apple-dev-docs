# MIDITransformControlType

**Framework**: Core MIDI  
**Kind**: enum

A set of values that indicate how to interpret control numbers.

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
enum MIDITransformControlType
```

## Topics

### Transform Control Types
- [MIDITransformControlType.controlType_7Bit](miditransformcontroltype/controltype_7bit.md)
  A 7-bit control type.
- [MIDITransformControlType.controlType_14Bit](miditransformcontroltype/controltype_14bit.md)
  A 14-bit control type.
- [MIDITransformControlType.controlType_7BitRPN](miditransformcontroltype/controltype_7bitrpn.md)
  A 7-bit Registered Parameter Number (RPN).
- [MIDITransformControlType.controlType_14BitRPN](miditransformcontroltype/controltype_14bitrpn.md)
  A 14-bit Registered Parameter Number (RPN).
- [MIDITransformControlType.controlType_7BitNRPN](miditransformcontroltype/controltype_7bitnrpn.md)
  A 7-bit Nonregistered Parameter Number (RPN).
- [MIDITransformControlType.controlType_14BitNRPN](miditransformcontroltype/controltype_14bitnrpn.md)
  A 14-bit Nonregistered Parameter Number (RPN).
### Initializers
- [init?(rawValue: UInt8)](miditransformcontroltype/init(rawvalue:).md)

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
- [enum MIDITransformType](miditransformtype.md)
  Values that specify the type of MIDI transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/miditransformcontroltype)*