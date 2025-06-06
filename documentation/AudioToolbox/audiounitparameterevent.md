# AudioUnitParameterEvent

**Framework**: Audio Toolbox  
**Kind**: struct

A scheduled change to an audio unit parameter’s value.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioUnitParameterEvent
```

#### Overview

If the `eventType` field value is [`AUParameterEventType.parameterEvent_Immediate`](auparametereventtype/parameterevent_immediate.md), use the `immediate` structure in the `eventValues` union. If the event type is [`AUParameterEventType.parameterEvent_Ramped`](auparametereventtype/parameterevent_ramped.md), use the `ramp` structure in the `eventValues` union.

Apply one or more [`AudioUnitParameterEvent`](audiounitparameterevent.md) events to an audio unit using the [`AudioUnitScheduleParameters(_:_:_:)`](audiounitscheduleparameters(_:_:_:).md) function.

## Topics

### Fields
- [var scope: AudioUnitScope](audiounitparameterevent/scope.md)
  The scope for this parameter event.
- [var element: AudioUnitElement](audiounitparameterevent/element.md)
  The element for this parameter event.
- [var parameter: AudioUnitParameterID](audiounitparameterevent/parameter.md)
  An identifier for this parameter event.
- [var eventType: AUParameterEventType](audiounitparameterevent/eventtype.md)
  The type for this parameter event.
- [var eventValues: AudioUnitParameterEvent.__Unnamed_union_eventValues](audiounitparameterevent/eventvalues.md)
  The values for this parameter event.
### Initializers
- [init()](audiounitparameterevent/init.md)
- [init(scope: AudioUnitScope, element: AudioUnitElement, parameter: AudioUnitParameterID, eventType: AUParameterEventType, eventValues: AudioUnitParameterEvent.__Unnamed_union_eventValues)](audiounitparameterevent/init(scope:element:parameter:eventtype:eventvalues:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

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
- [struct AudioUnitParameterValueFromString](audiounitparametervaluefromstring.md)
  A parameter’s value based on a string representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterevent)*