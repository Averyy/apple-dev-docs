# Playback Parameterization

**Framework**: PHASE

Change the characteristics of in-flight audio by adjusting its properties at runtime.

#### Overview

Metaparameters control several features of a sound source or sound event, as they play back. For instance, metaparameters can adjust a switch node’s toggle, or the amount of reverb that a sound source emanates.

##### Attach Metaparameters to a Particular Sound

To use a metaparameter, you attach it to a sound event or sound source. PHASE provides the following ways to attach metaparameters:

##### Adjust a Property of a Single Audio Signal

The framework refers to metaparameters that you access through a sound event’s [`metaParameters`](phasesoundevent/metaparameters.md) dictionary as  metaparameters. When you adjust the value of a local metaparameter, it affects just the sound event.

The following code changes the volume on a specific sound event:

##### Share a Parameter with Multiple Audio Signals

The framework refers to parameters that affect many sound events or sound sources as  metaparameters. Real-time adjustments to global metaparameters affect the playback of all sound events that initialize with the metaparameter.

The following code changes a `weather` metaparameter for all of its associated sound events:

As part of the engine’s asset registry, the [`globalMetaParameters`](phaseassetregistry/globalmetaparameters.md) dictionary affects every playing sound event that shares a metaparameter that the dictionary contains.

## Topics

### Base Metaparameters
- [class PHASEMetaParameter](phasemetaparameter.md)
  A named parameter with a value that the app can change over time.
- [class PHASEMetaParameterDefinition](phasemetaparameterdefinition.md)
  A specification for a named parameter with a constant value.
- [class PHASEGlobalMetaParameterAsset](phaseglobalmetaparameterasset.md)
  A reference to a registered metaparameter that the app can share with multiple sound events or sources.
### Linear Metaparameters
- [class PHASENumberMetaParameter](phasenumbermetaparameter.md)
  A metaparameter defined by a number that can change over time.
- [class PHASENumberMetaParameterDefinition](phasenumbermetaparameterdefinition.md)
  A specification for a metaparameter defined by a number.
### Textual Metaparameters
- [class PHASEStringMetaParameter](phasestringmetaparameter.md)
  A metaparameter with a text definition that can change over time.
- [class PHASEStringMetaParameterDefinition](phasestringmetaparameterdefinition.md)
  A specification for a metaparameter defined by text.
### Graphed Metaparameters
- [class PHASEMappedMetaParameterDefinition](phasemappedmetaparameterdefinition.md)
  A metaparameter that graphs an input value on a set of mathematical curves.

## See Also

- [class PHASEEnvelope](phaseenvelope.md)
  A collection of segments that connect to graph a complex curve over a linear input.
- [class PHASEEnvelopeSegment](phaseenvelopesegment.md)
  A curved portion of an envelope.
- [enum PHASECurveType](phasecurvetype.md)
  Options that apply a mathematical function to an input value.
- [class PHASENumericPair](phasenumericpair.md)
  An ordered pair that defines a bounding box for an envelope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/playback-parameterization)*