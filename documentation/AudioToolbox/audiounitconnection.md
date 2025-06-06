# AudioUnitConnection

**Framework**: Audio Toolbox  
**Kind**: struct

An audio unit source-to-destination connection specification.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioUnitConnection
```

## Topics

### Initializers
- [init()](audiounitconnection/init.md)
- [init(sourceAudioUnit: AudioUnit?, sourceOutputNumber: UInt32, destInputNumber: UInt32)](audiounitconnection/init(sourceaudiounit:sourceoutputnumber:destinputnumber:)-63vjd.md)
- [init(sourceAudioUnit: AudioUnit?, sourceOutputNumber: UInt32, destInputNumber: UInt32)](audiounitconnection/init(sourceaudiounit:sourceoutputnumber:destinputnumber:)-6kg20.md)
### Instance Properties
- [var destInputNumber: UInt32](audiounitconnection/destinputnumber.md)
  The destination audio unit’s input element to be used in the connection.
- [var sourceAudioUnit: AudioUnit?](audiounitconnection/sourceaudiounit.md)
  The audio unit that is serves as the source in the connection.
- [var sourceOutputNumber: UInt32](audiounitconnection/sourceoutputnumber.md)
  The source audio unit’s output element to be used in the connection.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

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
- [struct AudioUnitParameterValueFromString](audiounitparametervaluefromstring.md)
  A parameter’s value based on a string representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitconnection)*