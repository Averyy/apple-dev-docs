# PHASEDefinition

**Framework**: PHASE  
**Kind**: class

A base class that adds a name to framework definitions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEDefinition
```

#### Overview

Various PHASE classes derive from this class, for example, [`PHASEMixerDefinition`](phasemixerdefinition.md), [`PHASEMetaParameterDefinition`](phasemetaparameterdefinition.md), and [`PHASESoundEventNodeDefinition`](phasesoundeventnodedefinition.md).

This class represents a template from which PHASE creates concrete [`PHASEAsset`](phaseasset.md) subclasses at runtime. For example, when you register a global metaparameter definition using [`registerGlobalMetaParameter(metaParameterDefinition:)`](phaseassetregistry/registerglobalmetaparameter(metaparameterdefinition:).md), PHASE returns a [`PHASEAsset`](phaseasset.md) subclass, [`PHASEGlobalMetaParameterAsset`](phaseglobalmetaparameterasset.md), that identifies a usable metaparameter by name. To access the usable metaparameter, pass the [`PHASEGlobalMetaParameterAsset`](phaseglobalmetaparameterasset.md) [`identifier`](phaseasset/identifier.md) into the [`globalMetaParameters`](phaseassetregistry/globalmetaparameters.md) dictionary.

## Topics

### Identifying a Definition
- [var identifier: String](phasedefinition/identifier.md)
  A unique name for the definition.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [PHASEMetaParameterDefinition](phasemetaparameterdefinition.md)
- [PHASEMixerDefinition](phasemixerdefinition.md)
- [PHASESoundEventNodeDefinition](phasesoundeventnodedefinition.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASEChannelMixerDefinition](phasechannelmixerdefinition.md)
  An audio-layering object that routes sound directly to the device’s output.
- [class PHASEAmbientMixerDefinition](phaseambientmixerdefinition.md)
  An audio-layering object that outputs sound in a particular direction in 3D space.
- [class PHASEMixerDefinition](phasemixerdefinition.md)
  An object to initialize a mixer with a given configuration.
- [class PHASEMixer](phasemixer.md)
  An object that combines multiple audio signals into a single signal.
- [Spatial Mixing](spatial-mixing.md)
  Define environmental characteristics that determine how sound plays in your app’s 3D soundscape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasedefinition)*