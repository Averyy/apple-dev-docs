# AudioUnitParameterNameInfo

**Framework**: Audio Toolbox  
**Kind**: struct

A short version of the name for an audio unit parameter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioUnitParameterNameInfo
```

#### Discussion

This data structure is used as a value for the [`kAudioUnitProperty_ParameterClumpName`](kaudiounitproperty_parameterclumpname.md) and [`kAudioUnitProperty_ParameterIDName`](kaudiounitproperty_parameteridname.md) audio unit properties.

## Topics

### Initializers
- [init()](audiounitparameternameinfo/init.md)
- [init(inID: AudioUnitParameterID, inDesiredLength: Int32, outName: Unmanaged<CFString>?)](audiounitparameternameinfo/init(inid:indesiredlength:outname:).md)
### Instance Properties
- [var inDesiredLength: Int32](audiounitparameternameinfo/indesiredlength.md)
  When setting an audio unit property that uses this data structure for its value, the maximum length that you are specifying for the audio unit parameter name.
- [var inID: AudioUnitParameterID](audiounitparameternameinfo/inid.md)
  The identifier for the audio unit parameter.
- [var outName: Unmanaged<CFString>?](audiounitparameternameinfo/outname.md)
  When getting an audio unit property that uses this data structure for its value, the short version of the parameter name provided by the audio unit. The host application then owns the string and is responsible for releasing it.

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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitparameternameinfo)*