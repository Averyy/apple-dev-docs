# AudioUnitFrequencyResponseBin

**Framework**: Audio Toolbox  
**Kind**: struct

An audio unit’s audio level at a particular frequency.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioUnitFrequencyResponseBin
```

#### Overview

An array of AudioUnitFrequencyResponseBin are passed in to kAudioUnitProperty_FrequencyResponse with the mFrequency field filled in. The array is returned with the mMagnitude fields filled in. If fewer than kNumberOfResponseFrequencies are needed, then the first unused bin should be marked with a negative frequency.

## Topics

### Initializers
- [init()](audiounitfrequencyresponsebin/init.md)
- [init(mFrequency: Float64, mMagnitude: Float64)](audiounitfrequencyresponsebin/init(mfrequency:mmagnitude:).md)
### Instance Properties
- [var mFrequency: Float64](audiounitfrequencyresponsebin/mfrequency.md)
- [var mMagnitude: Float64](audiounitfrequencyresponsebin/mmagnitude.md)

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
- [struct AudioUnitParameterValueFromString](audiounitparametervaluefromstring.md)
  A parameter’s value based on a string representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitfrequencyresponsebin)*