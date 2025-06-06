# AudioUnitParameterInfo

**Framework**: Audio Toolbox  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioUnitParameterInfo
```

## Topics

### Initializers
- [init()](audiounitparameterinfo/init.md)
- [init(name: (CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar), unitName: Unmanaged<CFString>?, clumpID: UInt32, cfNameString: Unmanaged<CFString>?, unit: AudioUnitParameterUnit, minValue: AudioUnitParameterValue, maxValue: AudioUnitParameterValue, defaultValue: AudioUnitParameterValue, flags: AudioUnitParameterOptions)](audiounitparameterinfo/init(name:unitname:clumpid:cfnamestring:unit:minvalue:maxvalue:defaultvalue:flags:).md)
### Instance Properties
- [var cfNameString: Unmanaged<CFString>?](audiounitparameterinfo/cfnamestring.md)
  Only valid if `kAudioUnitParameterFlag_HasCFNameString` is set.
- [var clumpID: UInt32](audiounitparameterinfo/clumpid.md)
  Only valid if `kAudioUnitParameterFlag_HasClump` is set.
- [var defaultValue: AudioUnitParameterValue](audiounitparameterinfo/defaultvalue.md)
- [var flags: AudioUnitParameterOptions](audiounitparameterinfo/flags.md)
  The host should check for this flag and, if present, release the parameter name when it is finished with it.
- [var maxValue: AudioUnitParameterValue](audiounitparameterinfo/maxvalue.md)
- [var minValue: AudioUnitParameterValue](audiounitparameterinfo/minvalue.md)
- [var name: (CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar)](audiounitparameterinfo/name.md)
  Must be set to `0`.
- [var unit: AudioUnitParameterUnit](audiounitparameterinfo/unit.md)
  If the `unit` field contains a value not in the `AudioUnitParameterUnit` enumeration, then assume the unit type is `kAudioUnitParameterUnit_Generic`.
- [var unitName: Unmanaged<CFString>?](audiounitparameterinfo/unitname.md)
  If `kAudioUnitParameterUnit_CustomUnit` is set, this field must contain a valid `CFString` object. Only valid if `kAudioUnitParameterUnit_CustomUnit` is set.

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
- [struct AudioUnitParameterOptions](audiounitparameteroptions.md)
  Value options for audio unit parameters.
- [struct AudioUnitParameterStringFromValue](audiounitparameterstringfromvalue.md)
  A string representation of a parameter’s value.
- [struct AudioUnitParameterValueFromString](audiounitparametervaluefromstring.md)
  A parameter’s value based on a string representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterinfo)*