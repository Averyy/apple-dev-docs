# AudioUnitProperty

**Framework**: Audio Toolbox  
**Kind**: struct

A key-value pair that declares an attribute or behavior for an audio unit.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioUnitProperty
```

## Topics

### Initializers
- [init(mAudioUnit: AudioUnit, mPropertyID: AudioUnitPropertyID, mScope: AudioUnitScope, mElement: AudioUnitElement)](audiounitproperty/init(maudiounit:mpropertyid:mscope:melement:)-1z6rt.md)
- [init(mAudioUnit: AudioUnit, mPropertyID: AudioUnitPropertyID, mScope: AudioUnitScope, mElement: AudioUnitElement)](audiounitproperty/init(maudiounit:mpropertyid:mscope:melement:)-2ay1o.md)
### Instance Properties
- [var mAudioUnit: AudioUnit](audiounitproperty/maudiounit.md)
  The audio unit instance that the parameter applies to.
- [var mElement: AudioUnitElement](audiounitproperty/melement.md)
  The audio unit element for the property.
- [var mPropertyID: AudioUnitPropertyID](audiounitproperty/mpropertyid.md)
  The audio unit property identifier.
- [var mScope: AudioUnitScope](audiounitproperty/mscope.md)
  The audio unit scope for the property.

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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitproperty)*