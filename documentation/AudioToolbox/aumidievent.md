# AUMIDIEvent

**Framework**: Audio Toolbox  
**Kind**: struct

A structure that describes a scheduled MIDI event.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AUMIDIEvent
```

## Topics

### Initializers
- [init()](aumidievent/init.md)
- [init(next: UnsafeMutablePointer<AURenderEvent>?, eventSampleTime: AUEventSampleTime, eventType: AURenderEventType, reserved: UInt8, length: UInt16, cable: UInt8, data: (UInt8, UInt8, UInt8))](aumidievent/init(next:eventsampletime:eventtype:reserved:length:cable:data:).md)
### Instance Properties
- [var cable: UInt8](aumidievent/cable.md)
  The virtual cable number.
- [var data: (UInt8, UInt8, UInt8)](aumidievent/data.md)
  The bytes of the MIDI event. Running status is not used.
- [var eventSampleTime: AUEventSampleTime](aumidievent/eventsampletime.md)
  The sample time at which the event is scheduled to occur.
- [var eventType: AURenderEventType](aumidievent/eventtype.md)
  The type of render event. Must be [`AURenderEventType.MIDI`](aurendereventtype/midi.md) or [`AURenderEventType.midiSysEx`](aurendereventtype/midisysex.md).
- [var length: UInt16](aumidievent/length.md)
  The number of valid MIDI bytes in the data field. For most MIDI events this value is usually `1`, `2`, or `3`, but it can be longer for system-exclusive events.
- [var next: UnsafeMutablePointer<AURenderEvent>?](aumidievent/next.md)
  The next event in a linked list of events.
- [var reserved: UInt8](aumidievent/reserved.md)
  Reserved field. Must be `0`.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct AudioUnitConnection](audiounitconnection.md)
  An audio unit source-to-destination connection specification.
- [struct AudioUnitEvent](audiounitevent.md)
- [struct AudioUnitExternalBuffer](audiounitexternalbuffer.md)
  Allows an audio unit host application to tell an audio unit to use a specified buffer for its input callback.
- [struct AudioUnitFrequencyResponseBin](audiounitfrequencyresponsebin.md)
  An audio unit’s audio level at a particular frequency.
- [struct AudioUnitMeterClipping](audiounitmeterclipping.md)
  Audio clipping that has occurred in a mixer unit.
- [struct AudioUnitMIDIControlMapping](audiounitmidicontrolmapping.md)
- [struct AudioUnitOtherPluginDesc](audiounitotherplugindesc.md)
- [struct AudioUnitParameter](audiounitparameter.md)
  An adjustable audio unit attribute such as volume, pitch, or filter cutoff frequency.
- [struct AudioUnitParameterEvent](audiounitparameterevent.md)
  A scheduled change to an audio unit parameter’s value.
- [struct AudioUnitParameterHistoryInfo](audiounitparameterhistoryinfo.md)
  The suggested update rate and history duration for parameters which have the [`flag_PlotHistory`](audiounitparameteroptions/flag_plothistory.md) flag set.
- [struct AudioUnitParameterNameInfo](audiounitparameternameinfo.md)
  A short version of the name for an audio unit parameter.
- [typealias AudioUnitParameterIDName](audiounitparameteridname.md)
  A type definition for a data type that defines the short version of the name for an audio unit parameter.
- [struct AudioUnitParameterInfo](audiounitparameterinfo.md)
- [struct AudioUnitParameterOptions](audiounitparameteroptions.md)
  Value options for audio unit parameters.
- [struct AudioUnitParameterStringFromValue](audiounitparameterstringfromvalue.md)
  A string representation of a parameter’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aumidievent)*