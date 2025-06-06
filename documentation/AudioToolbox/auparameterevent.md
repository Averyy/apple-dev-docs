# AUParameterEvent

**Framework**: Audio Toolbox  
**Kind**: struct

A structure that describes a scheduled parameter event.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AUParameterEvent
```

## Topics

### Initializers
- [init()](auparameterevent/init.md)
- [init(next: UnsafeMutablePointer<AURenderEvent>?, eventSampleTime: AUEventSampleTime, eventType: AURenderEventType, reserved: (UInt8, UInt8, UInt8), rampDurationSampleFrames: AUAudioFrameCount, parameterAddress: AUParameterAddress, value: AUValue)](auparameterevent/init(next:eventsampletime:eventtype:reserved:rampdurationsampleframes:parameteraddress:value:).md)
### Instance Properties
- [var eventSampleTime: AUEventSampleTime](auparameterevent/eventsampletime.md)
  The sample time at which the event is scheduled to occur.
- [var eventType: AURenderEventType](auparameterevent/eventtype.md)
  The type of render event. Must be [`AURenderEventType.parameter`](aurendereventtype/parameter.md) or [`AURenderEventType.parameterRamp`](aurendereventtype/parameterramp.md).
- [var next: UnsafeMutablePointer<AURenderEvent>?](auparameterevent/next.md)
  The next event in a linked list of events.
- [var parameterAddress: AUParameterAddress](auparameterevent/parameteraddress.md)
  The parameter to change.
- [var rampDurationSampleFrames: AUAudioFrameCount](auparameterevent/rampdurationsampleframes.md)
  The ramp duration, in sample frames. Must be `0` for a non-ramped event; otherwise, must be greater than `0` for a ramped event.
- [var reserved: (UInt8, UInt8, UInt8)](auparameterevent/reserved.md)
  Reserved field. Must be `0`.
- [var value: AUValue](auparameterevent/value.md)
  For a non-ramped event, this is the new parameter value. For a ramped event, this is the parameter value at the end of the ramp.

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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameterevent)*