# PHASEMetaParameterDefinition

**Framework**: PHASE  
**Kind**: class  
**Role**: Class

A specification for a named parameter with a constant value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEMetaParameterDefinition
```

```objc
@interface PHASEMetaParameterDefinition : PHASEDefinition
```

## Overview

Instances of this class provide an app with dynamic control of various properies of live audio playback. This is a base class for the [`PHASENumberMetaParameterDefinition`](./phasenumbermetaparameterdefinition.md) and [`PHASEStringMetaParameterDefinition`](./phasestringmetaparameterdefinition.md) subclasses.

You create a single instance of one of the subclasses for a specific property you want to adjust. By passing the definition subclass to the framework, you spawn one or more [`PHASEMetaParameterDefinition`](./phasemetaparameterdefinition.md) objects for discrete use across your app. For example, when you initialize a [`PHASEBlendNodeDefinition`](./phaseblendnodedefinition.md) with a number metaparameter definition, PHASE registers a [`PHASENumberMetaParameter`](./phasenumbermetaparameter.md) in the corresponding sound event’s [`metaParameters`](./phasesoundevent/metaparameters.md) dictionary.

Put metaparameter definitions that you wish to share across different sounds in the asset registery’s [`globalMetaParameters`](./phaseassetregistry/globalmetaparameters.md) dictionary. To add global metaparameter definitions to the dictionary, call  [`registerGlobalMetaParameter(metaParameterDefinition:)`](./phaseassetregistry/registerglobalmetaparameter%28metaparameterdefinition%29.md). Then pass the definition into several sound event node defintions, such as [`PHASESamplerNodeDefinition`](./phasesamplernodedefinition.md).

## Topics

### Setting a Metaparameter
- [var value: Any](./phasemetaparameterdefinition/value.md)
  A constant value for the parameter definition.

## Relationships

### Inherits From
- [PHASEDefinition](./phasedefinition.md)
### Inherited By
- [PHASENumberMetaParameterDefinition](./phasenumbermetaparameterdefinition.md)
- [PHASEStringMetaParameterDefinition](./phasestringmetaparameterdefinition.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Base Metaparameters
- [class PHASEMetaParameter](./phasemetaparameter.md)
  A named parameter with a value that the app can change over time.
- [class PHASEGlobalMetaParameterAsset](./phaseglobalmetaparameterasset.md)
  A reference to a registered metaparameter that the app can share with multiple sound events or sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemetaparameterdefinition)*