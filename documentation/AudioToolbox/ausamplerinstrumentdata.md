# AUSamplerInstrumentData

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
struct AUSamplerInstrumentData
```

## Topics

### Initializers
- [init(fileURL: Unmanaged<CFURL>, instrumentType: UInt8, bankMSB: UInt8, bankLSB: UInt8, presetID: UInt8)](ausamplerinstrumentdata/init(fileurl:instrumenttype:bankmsb:banklsb:presetid:).md)
### Instance Properties
- [var bankLSB: UInt8](ausamplerinstrumentdata/banklsb.md)
- [var bankMSB: UInt8](ausamplerinstrumentdata/bankmsb.md)
- [var fileURL: Unmanaged<CFURL>](ausamplerinstrumentdata/fileurl.md)
- [var instrumentType: UInt8](ausamplerinstrumentdata/instrumenttype.md)
- [var presetID: UInt8](ausamplerinstrumentdata/presetid.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/ausamplerinstrumentdata)*