# PHASEBlendNodeDefinition

**Framework**: PHASE  
**Kind**: class

A node that smoothly fades between the audio of its child nodes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEBlendNodeDefinition
```

#### Overview

This class defines a threshold and a numeric parameter the app increases and decreases to fade between child nodes. Each child node defines a range within the threshold in which the child node plays audio. As the app moves the blend parameter value between `0` and the threshold, the blend node plays the audio of its child nodes whose range and fade curve overlap at the current value.

![Illustration of a flowchart that represents a sound event node tree. The chart contains three boxes, which represent nodes. At left, a box labeled Blend Node extends an arrow, which points to a box in the upper right that’s labeled, Sampler Node Cobblestone Footstep. The box labeled Random Node extends another arrow, which points to a box in the lower right that’s labeled, Sampler Node Grass Footstep. A verticle bar ranges from top sampler node to the bottom sampler node to indicate the range in which both just one node actively plays audio, or both nodes actively play audio, and to what volume they play. ](https://docs-assets.developer.apple.com/published/aca0330112ec32cda9c94d16e6119920/media-3918862%402x.png)

##### Play a Blend of Simultaneous Audio Data

To gradually change the audio that a sound event plays, define blend thresholds and a number metaparameter that incrementally increases or decreases between the thresholds. For example, the following code sets up a sound event hierarchy containing two sampler nodes that play audio, with each one modeling a different terrain. The app sets the metaparameter value based on the value of the terrain the player stands on. When the app starts a sound event from this hierarchy, PHASE plays:

- A grass footstep for terrain values between `0` and `0.33`
- A cobblestone footstep for terrain values between `0.67` and `1.0`
- A blend of both footstep sounds for values between `0.33` and `0.67`

```swift
// Create a meta parameter definition that chooses among different terrains.
let terrainBlendParameter = PHASENumberMetaParameterDefinition(
    value: 0.5, 
    minimum: 0.0,
    maximum: 1.0,
    identifier: "terrain")

// Create a blend node and pass in the meta parameter.
let terrainBlendNode = PHASEBlendNodeDefinition(blendMetaParameterDefinition: terrainBlendParameter)

// Add two samples nodes to blend between.
terrainBlendNode.addRangeForInputValuesAbove( 
    value: 0.33,
    fullGainAtValue: 1.0,
    fadeCurveType: .linear,
    subtree:cobblestoneSamplerNode)

terrainBlendNode.addRangeForInputValuesBelow( 
    value: 0.67,
    fullGainAtValue: 0.0,
    fadeCurveType: .linear,
    subtree:grassSamplerNode)

// Create a sound event.
var footstepEvent: PHASESoundEvent?
do { footstepEvent = try PHASESoundEvent(engine: myEngine, assetIdentifier: "terrain") } 
catch { fatalError("Failed to create the sound event due to: \(error)") }        

// Set the "terrain" metaparameter value to a midpoint that 
//  plays audio from both subtrees at an equal volume.
guard let terrainParameter = footstepEvent?.metaParameters["terrain"] else { fatalError() }
terrainParameter.value = 0.5

// Play the sound and hear a mix of both terrains.
footstepEvent?.start() { reason in 
/* Perform completion tasks. */ }
```

## Topics

### Creating a Blend Node
- [init(blendMetaParameterDefinition: PHASENumberMetaParameterDefinition)](phaseblendnodedefinition/init(blendmetaparameterdefinition:).md)
  Creates a blend node with a maxiumum blend range value.
- [convenience init(blendMetaParameterDefinition: PHASENumberMetaParameterDefinition, identifier: String)](phaseblendnodedefinition/init(blendmetaparameterdefinition:identifier:).md)
  Creates a named blend node with a maxiumum blend range value.
- [init(spatialMixerDefinition: PHASESpatialMixerDefinition)](phaseblendnodedefinition/init(spatialmixerdefinition:).md)
  Creates a blend node for spatial audio output.
- [convenience init(spatialMixerDefinition: PHASESpatialMixerDefinition, identifier: String)](phaseblendnodedefinition/init(spatialmixerdefinition:identifier:).md)
  Creates a named blend node for spatial audio output.
### Accessing Blend Properties
- [var blendParameterDefinition: PHASENumberMetaParameterDefinition?](phaseblendnodedefinition/blendparameterdefinition.md)
  The meta parameter definition that caps the blend range.
- [var spatialMixerDefinitionForDistance: PHASESpatialMixerDefinition?](phaseblendnodedefinition/spatialmixerdefinitionfordistance.md)
  An object that combines spatial audio layers.
### Adding Child Nodes
- [func addRange(envelope: PHASEEnvelope, subtree: PHASESoundEventNodeDefinition)](phaseblendnodedefinition/addrange(envelope:subtree:).md)
  Adds a child node with an envelope.
- [func addRangeForInputValuesAbove(value: Double, fullGainAtValue: Double, fadeCurveType: PHASECurveType, subtree: PHASESoundEventNodeDefinition)](phaseblendnodedefinition/addrangeforinputvaluesabove(value:fullgainatvalue:fadecurvetype:subtree:).md)
  Adds a child node that blends above a given value.
- [func addRangeForInputValuesBelow(value: Double, fullGainAtValue: Double, fadeCurveType: PHASECurveType, subtree: PHASESoundEventNodeDefinition)](phaseblendnodedefinition/addrangeforinputvaluesbelow(value:fullgainatvalue:fadecurvetype:subtree:).md)
  Adds a child node that blends below a given value.
- [func addRangeForInputValuesBetween(lowValue: Double, highValue: Double, fullGainAtLowValue: Double, fullGainAtHighValue: Double, lowFadeCurveType: PHASECurveType, highFadeCurveType: PHASECurveType, subtree: PHASESoundEventNodeDefinition)](phaseblendnodedefinition/addrangeforinputvaluesbetween(lowvalue:highvalue:fullgainatlowvalue:fullgainathighvalue:lowfadecurvetype:highfadecurvetype:subtree:).md)
  Adds a child node that blends between a given high and low value.

## Relationships

### Inherits From
- [PHASESoundEventNodeDefinition](phasesoundeventnodedefinition.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASESwitchNodeDefinition](phaseswitchnodedefinition.md)
  A node that passes invocation to only one of its child nodes.
- [class PHASERandomNodeDefinition](phaserandomnodedefinition.md)
  A sound event node that invokes one of its child nodes at random.
- [class PHASEContainerNodeDefinition](phasecontainernodedefinition.md)
  A node that plays all its children at the same time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseblendnodedefinition)*