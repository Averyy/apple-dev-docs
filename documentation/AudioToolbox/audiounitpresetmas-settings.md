# AudioUnitPresetMAS_Settings

**Framework**: Audio Toolbox  
**Kind**: struct

**Availability**:
- macOS ?+

## Declaration

```swift
struct AudioUnitPresetMAS_Settings
```

## Topics

### Initializers
- [init()](audiounitpresetmas_settings/init.md)
- [init(manufacturerID: UInt32, effectID: UInt32, variantID: UInt32, settingsVersion: UInt32, numberOfSettings: UInt32, settings: AudioUnitPresetMAS_SettingData)](audiounitpresetmas_settings/init(manufacturerid:effectid:variantid:settingsversion:numberofsettings:settings:).md)
### Instance Properties
- [var effectID: UInt32](audiounitpresetmas_settings/effectid.md)
- [var manufacturerID: UInt32](audiounitpresetmas_settings/manufacturerid.md)
- [var numberOfSettings: UInt32](audiounitpresetmas_settings/numberofsettings.md)
- [var settings: AudioUnitPresetMAS_SettingData](audiounitpresetmas_settings/settings.md)
- [var settingsVersion: UInt32](audiounitpresetmas_settings/settingsversion.md)
- [var variantID: UInt32](audiounitpresetmas_settings/variantid.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitpresetmas_settings)*