# Playback Parameterization

**Framework**: PHASE

Change the characteristics of in-flight audio by adjusting its properties at runtime.

#### Overview

Metaparameters control several features of a sound source or sound event, as they play back. For instance, metaparameters can adjust a switch node’s toggle, or the amount of reverb that a sound source emanates.

##### Attach Metaparameters to a Particular Sound

To use a metaparameter, you attach it to a sound event or sound source. PHASE provides the following ways to attach metaparameters:

- **[`PHASEGeneratorNodeDefinition`](phasegeneratornodedefinition.md)**: [`gainMetaParameterDefinition`](phasegeneratornodedefinition/gainmetaparameterdefinition.md), [`rateMetaParameterDefinition`](phasegeneratornodedefinition/ratemetaparameterdefinition.md)
- **[`PHASEMixerDefinition`](phasemixerdefinition.md)**: [`gainMetaParameterDefinition`](phasemixerdefinition/gainmetaparameterdefinition.md)
- **[`PHASESwitchNodeDefinition`](phaseswitchnodedefinition.md)**: [`init(switchMetaParameterDefinition:)`](phaseswitchnodedefinition/init(switchmetaparameterdefinition:).md)
- **[`PHASEBlendNodeDefinition`](phaseblendnodedefinition.md)**: [`init(blendMetaParameterDefinition:)`](phaseblendnodedefinition/init(blendmetaparameterdefinition:).md)
- **[`PHASEMappedMetaParameterDefinition`](phasemappedmetaparameterdefinition.md)**: [`init(inputMetaParameterDefinition:envelope:identifier:)`](phasemappedmetaparameterdefinition/init(inputmetaparameterdefinition:envelope:identifier:).md)
- **[`PHASESpatialPipelineEntry`](phasespatialpipelineentry.md)**: [`sendLevelMetaParameterDefinition`](phasespatialpipelineentry/sendlevelmetaparameterdefinition.md)

##### Adjust a Property of a Single Audio Signal

The framework refers to metaparameters that you access through a sound event’s [`metaParameters`](phasesoundevent/metaparameters.md) dictionary as *local* metaparameters. When you adjust the value of a local metaparameter, it affects just the sound event.

The following code changes the volume on a specific sound event:

**Swift**:

```swift
// Create a `PHASEMetaParameterDefinition` instance.
let myGainParam = PHASENumberMetaParameterDefinition(value: 1, identifier: "gain")

// Create a sampler node that plays an audio file named "mySound".
let mySampler = PHASESamplerNodeDefinition(
    soundAssetIdentifier: "mySound",
    mixerDefinition: myMixer)

// Attach the metaparameter to the sampler node.
mySampler.gainMetaParameterDefinition = myGainParam;

// Invoke the sound event.
mySoundEvent.start()

// Access the local metaparameter and change the gain.
if let metaparameter = mySoundEvent.metaParameters["gain"] {
    metaparameter.value = 0.5
}
```

**Objective-C**:

```objc
// Create a `PHASEMetaParameterDefinition` instance. 
PHASENumberMetaParameterDefinition* myGainParam = 
    [[PHASENumberMetaParameterDefinition alloc] 
    initWithValue:1 uid:@"gain"];

// Create a sampler node that plays an audio file named "mySound".
PHASESamplerNodeDefinition* mySampler = [[PHASESamplerNodeDefinition alloc]
    initWithSoundAssetUID:@"mySound"] mixerDefinition:myMixer];

// Attach the metaparameter to the sampler node.
mySampler.gainMetaParameterDefinition = myGainParam;

// Invoke the sound event.
[myPHASESoundEvent startAndReturnError:&myError];

// Access the local metaparameter and change the gain.
myPHASESoundEvent.metaParameters[@"gain"].value = 0.5
```

##### Share a Parameter with Multiple Audio Signals

The framework refers to parameters that affect many sound events or sound sources as *global* metaparameters. Real-time adjustments to global metaparameters affect the playback of all sound events that initialize with the metaparameter.

The following code changes a `weather` metaparameter for all of its associated sound events:

**Swift**:

```swift
// Create a `PHASEMetaParameterDefinition` instance.
let myGlobalWeatherParam = PHASEStringMetaParameterDefinition(
    value: "sunny", identifier: "weather")

// Register it as a global metaparameter.
do {
    try myEngine.assetRegistry.registerGlobalMetaParameter(metaParameterDefinition: myGlobalWeatherParam)
} catch {
    fatalError("Unable to register the weather metaparameter.")
}

// Attach it to a sound event node definition.
let mySwitchNode = PHASESwitchNodeDefinition(switchMetaParameterDefinition: myGlobalWeatherParam)

// Change the its value at runtime.
if let metaparameter = myEngine.assetRegistry.globalMetaParameters["weather"] {
    metaparameter.value = "rainy"
}
```

**Objective-C**:

```objc
// Create a `PHASEMetaParameterDefinition` instance. 
PHASEStringMetaParameterDefinition* myGlobalWeatherParam = 
    [[PHASEStringMetaParameterDefinition alloc] 
    initWithValue:@"sunny" uid:@"weather"];

// Register it as a global metaparameter.
[myPHASEEngine.assetRegistry registerGlobalMetaParameter:myGlobalWeatherParam
    uid:@"weather"];

// Attach it to a sound event node definition.
PHASESwitchNodeDefinition* mySwitchNode = [[PHASESwitchNodeDefinition alloc] 
    initWithSwitchMetaParameterDefinition:myGlobalWeatherParam];

// Change the its value at runtime.
myPHASEEngine.assetRegistry.globalMetaParameters[@"weather"].value = @"rainy";
```

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