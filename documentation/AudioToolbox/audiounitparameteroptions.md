# AudioUnitParameterOptions

**Framework**: Audio Toolbox  
**Kind**: struct

Value options for audio unit parameters.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioUnitParameterOptions
```

#### Overview

These constants are relevant only in macOS, and not in iOS.

Audio unit parameter flags, for use in the [`AudioUnitParameterInfo`](audiounitparameterinfo.md) data structure , serve as a dictionary-like set of information about an audio unit parameter. Parameter flag bit position 19 is reserved.

## Topics

### Constants
- [static var flag_CFNameRelease: AudioUnitParameterOptions](audiounitparameteroptions/flag_cfnamerelease.md)
  If an audio unit can generate parameter names dynamically, it should set this flag.
- [static var flag_CanRamp: AudioUnitParameterOptions](audiounitparameteroptions/flag_canramp.md)
- [static var flag_DisplayCubeRoot: AudioUnitParameterOptions](audiounitparameteroptions/flag_displaycuberoot.md)
- [static var flag_DisplayCubed: AudioUnitParameterOptions](audiounitparameteroptions/flag_displaycubed.md)
- [static var flag_DisplayExponential: AudioUnitParameterOptions](audiounitparameteroptions/flag_displayexponential.md)
- [static var flag_DisplayLogarithmic: AudioUnitParameterOptions](audiounitparameteroptions/flag_displaylogarithmic.md)
- [static var flag_DisplayMask: AudioUnitParameterOptions](audiounitparameteroptions/flag_displaymask.md)
- [static var flag_DisplaySquareRoot: AudioUnitParameterOptions](audiounitparameteroptions/flag_displaysquareroot.md)
- [static var flag_DisplaySquared: AudioUnitParameterOptions](audiounitparameteroptions/flag_displaysquared.md)
- [static var flag_ExpertMode: AudioUnitParameterOptions](audiounitparameteroptions/flag_expertmode.md)
- [static var flag_HasCFNameString: AudioUnitParameterOptions](audiounitparameteroptions/flag_hascfnamestring.md)
- [static var flag_HasClump: AudioUnitParameterOptions](audiounitparameteroptions/flag_hasclump.md)
- [static var flag_IsElementMeta: AudioUnitParameterOptions](audiounitparameteroptions/flag_iselementmeta.md)
- [static var flag_IsGlobalMeta: AudioUnitParameterOptions](audiounitparameteroptions/flag_isglobalmeta.md)
- [static var flag_IsHighResolution: AudioUnitParameterOptions](audiounitparameteroptions/flag_ishighresolution.md)
- [static var flag_IsReadable: AudioUnitParameterOptions](audiounitparameteroptions/flag_isreadable.md)
- [static var flag_IsWritable: AudioUnitParameterOptions](audiounitparameteroptions/flag_iswritable.md)
- [static var flag_MeterReadOnly: AudioUnitParameterOptions](audiounitparameteroptions/flag_meterreadonly.md)
- [static var flag_NonRealTime: AudioUnitParameterOptions](audiounitparameteroptions/flag_nonrealtime.md)
- [static var flag_OmitFromPresets: AudioUnitParameterOptions](audiounitparameteroptions/flag_omitfrompresets.md)
- [static var flag_PlotHistory: AudioUnitParameterOptions](audiounitparameteroptions/flag_plothistory.md)
  If set, getting the `kAudioUnitProperty_ParameterHistoryInfo` property fills out the [`AudioUnitParameterHistoryInfo`](audiounitparameterhistoryinfo.md) struct containing the recommended update rate and history duration.
- [static var flag_ValuesHaveStrings: AudioUnitParameterOptions](audiounitparameteroptions/flag_valueshavestrings.md)
### Initializers
- [init(rawValue: UInt32)](audiounitparameteroptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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
- [struct AudioUnitParameterStringFromValue](audiounitparameterstringfromvalue.md)
  A string representation of a parameter’s value.
- [struct AudioUnitParameterValueFromString](audiounitparametervaluefromstring.md)
  A parameter’s value based on a string representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions)*