# AudioUnitParameter

**Framework**: Audio Toolbox  
**Kind**: struct

An adjustable audio unit attribute such as volume, pitch, or filter cutoff frequency.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioUnitParameter
```

#### Overview

This data structure is used by functions declared in the `AudioToolbox/AudioUnitUtilities.h` header file in macOS.

An audio unit parameter is uniquely identified by the combination of its scope, element, and ID.

## Topics

### Initializers
- [init(mAudioUnit: AudioUnit, mParameterID: AudioUnitParameterID, mScope: AudioUnitScope, mElement: AudioUnitElement)](audiounitparameter/init(maudiounit:mparameterid:mscope:melement:)-2hcn6.md)
- [init(mAudioUnit: AudioUnit, mParameterID: AudioUnitParameterID, mScope: AudioUnitScope, mElement: AudioUnitElement)](audiounitparameter/init(maudiounit:mparameterid:mscope:melement:)-55k5j.md)
### Instance Properties
- [var mAudioUnit: AudioUnit](audiounitparameter/maudiounit.md)
  The audio unit instance that the parameter applies to.
- [var mElement: AudioUnitElement](audiounitparameter/melement.md)
  The audio unit element for the parameter.
- [var mParameterID: AudioUnitParameterID](audiounitparameter/mparameterid.md)
  The audio unit parameter identifier.
- [var mScope: AudioUnitScope](audiounitparameter/mscope.md)
  The audio unit scope for the parameter.

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
- [struct AudioUnitParameterValueFromString](audiounitparametervaluefromstring.md)
  A parameter’s value based on a string representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitparameter)*