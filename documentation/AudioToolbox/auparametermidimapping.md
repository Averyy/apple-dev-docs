# AUParameterMIDIMapping

**Framework**: Audio Toolbox  
**Kind**: struct

**Availability**:
- macOS ?+

## Declaration

```swift
struct AUParameterMIDIMapping
```

## Topics

### Initializers
- [init()](auparametermidimapping/init.md)
- [init(mScope: AudioUnitScope, mElement: AudioUnitElement, mParameterID: AudioUnitParameterID, mFlags: AUParameterMIDIMappingFlags, mSubRangeMin: AudioUnitParameterValue, mSubRangeMax: AudioUnitParameterValue, mStatus: UInt8, mData1: UInt8, reserved1: UInt8, reserved2: UInt8, reserved3: UInt32)](auparametermidimapping/init(mscope:melement:mparameterid:mflags:msubrangemin:msubrangemax:mstatus:mdata1:reserved1:reserved2:reserved3:).md)
### Instance Properties
- [var mData1: UInt8](auparametermidimapping/mdata1.md)
- [var mElement: AudioUnitElement](auparametermidimapping/melement.md)
- [var mFlags: AUParameterMIDIMappingFlags](auparametermidimapping/mflags.md)
- [var mParameterID: AudioUnitParameterID](auparametermidimapping/mparameterid.md)
- [var mScope: AudioUnitScope](auparametermidimapping/mscope.md)
- [var mStatus: UInt8](auparametermidimapping/mstatus.md)
- [var mSubRangeMax: AudioUnitParameterValue](auparametermidimapping/msubrangemax.md)
- [var mSubRangeMin: AudioUnitParameterValue](auparametermidimapping/msubrangemin.md)
- [var reserved1: UInt8](auparametermidimapping/reserved1.md)
- [var reserved2: UInt8](auparametermidimapping/reserved2.md)
- [var reserved3: UInt32](auparametermidimapping/reserved3.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparametermidimapping)*