# MIDITransformType.scale

**Framework**: Core MIDI  
**Kind**: case  
**Role**: Case

A transform that multiplies by the specified parameter value.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case scale
```

```c
kMIDITransform_Scale
```

#### Discussion

Specify the parameter value in fixed point format: `bbbb.bbbb bbbb bbbb`

## See Also

### Transform Types
- [MIDITransformType.none](./none.md)
  No transformation.
- [MIDITransformType.filterOut](./filterout.md)
  A transformation that filters out an event type.
- [MIDITransformType.mapControl](./mapcontrol.md)
  A transformation that changes a specified control number to a supplied parameter value.
- [MIDITransformType.add](./add.md)
  A transform that adds a parameter value.
- [MIDITransformType.minValue](./minvalue.md)
  A transform that sets the minimum value to the specified parameter value.
- [MIDITransformType.maxValue](./maxvalue.md)
  A transform that sets the maximum value to the specified parameter value.
- [MIDITransformType.mapValue](./mapvalue.md)
  A transform that maps one value to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/miditransformtype/scale)*