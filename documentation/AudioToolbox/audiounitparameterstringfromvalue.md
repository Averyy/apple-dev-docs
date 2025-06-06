# AudioUnitParameterStringFromValue

**Framework**: Audio Toolbox  
**Kind**: struct

A string representation of a parameter’s value.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioUnitParameterStringFromValue
```

## Topics

### Initializers
- [init(inParamID: AudioUnitParameterID, inValue: UnsafePointer<AudioUnitParameterValue>, outString: Unmanaged<CFString>?)](audiounitparameterstringfromvalue/init(inparamid:invalue:outstring:).md)
### Instance Properties
- [var inParamID: AudioUnitParameterID](audiounitparameterstringfromvalue/inparamid.md)
- [var inValue: UnsafePointer<AudioUnitParameterValue>](audiounitparameterstringfromvalue/invalue.md)
- [var outString: Unmanaged<CFString>?](audiounitparameterstringfromvalue/outstring.md)

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
- [struct AudioUnitParameterValueFromString](audiounitparametervaluefromstring.md)
  A parameter’s value based on a string representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterstringfromvalue)*