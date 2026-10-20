# AUNumVersion

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS

## Declaration

```swift
struct AUNumVersion
```

```c
typedef struct AUNumVersion { ... } AUNumVersion;
```

## Topics

### Initializers
- [init()](./aunumversion/init%28%29.md)
- [init(nonRelRev: UInt8, stage: UInt8, minorAndBugRev: UInt8, majorRev: UInt8)](./aunumversion/init%28nonrelrev,stage,minorandbugrev,majorrev%29.md)
### Instance Properties
- [var majorRev: UInt8](./aunumversion/majorrev.md)
- [var minorAndBugRev: UInt8](./aunumversion/minorandbugrev.md)
- [var nonRelRev: UInt8](./aunumversion/nonrelrev.md)
- [var stage: UInt8](./aunumversion/stage.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Structures
- [struct AudioUnitConnection](./audiounitconnection.md)
  An audio unit source-to-destination connection specification.
- [struct AudioUnitEvent](./audiounitevent.md)
- [struct AudioUnitExternalBuffer](./audiounitexternalbuffer.md)
  Allows an audio unit host application to tell an audio unit to use a specified buffer for its input callback.
- [struct AudioUnitFrequencyResponseBin](./audiounitfrequencyresponsebin.md)
  An audio unit’s audio level at a particular frequency.
- [struct AudioUnitMeterClipping](./audiounitmeterclipping.md)
  Audio clipping that has occurred in a mixer unit.
- [struct AudioUnitMIDIControlMapping](./audiounitmidicontrolmapping.md)
- [struct AudioUnitOtherPluginDesc](./audiounitotherplugindesc.md)
- [struct AudioUnitParameter](./audiounitparameter.md)
  An adjustable audio unit attribute such as volume, pitch, or filter cutoff frequency.
- [struct AudioUnitParameterEvent](./audiounitparameterevent.md)
  A scheduled change to an audio unit parameter’s value.
- [struct AudioUnitParameterHistoryInfo](./audiounitparameterhistoryinfo.md)
  The suggested update rate and history duration for parameters which have the [`flag_PlotHistory`](./audiounitparameteroptions/flag_plothistory.md) flag set.
- [struct AudioUnitParameterNameInfo](./audiounitparameternameinfo.md)
  A short version of the name for an audio unit parameter.
- [typealias AudioUnitParameterIDName](./audiounitparameteridname.md)
  A type definition for a data type that defines the short version of the name for an audio unit parameter.
- [struct AudioUnitParameterInfo](./audiounitparameterinfo.md)
- [struct AudioUnitParameterOptions](./audiounitparameteroptions.md)
  Value options for audio unit parameters.
- [struct AudioUnitParameterStringFromValue](./audiounitparameterstringfromvalue.md)
  A string representation of a parameter’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aunumversion)*