# PHASENumberMetaParameterDefinition

**Framework**: PHASE  
**Kind**: class

A specification for a metaparameter defined by a number.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASENumberMetaParameterDefinition
```

#### Overview

Use this class to spawn discrete instances of [`PHASENumberMetaParameter`](phasenumbermetaparameter.md), for example, a “player speed” metaparameter that the app changes gradually from `0.0` to `1.0`.

To use a number metaparameter, create an instance of this class and:

- Register it with the engine by calling [`registerGlobalMetaParameter(metaParameterDefinition:)`](phaseassetregistry/registerglobalmetaparameter(metaparameterdefinition:).md), then access the instance of this class in the engine’s [`globalMetaParameters`](phaseassetregistry/globalmetaparameters.md) dictionary.
- Pass it to the [`PHASEBlendNodeDefinition`](phaseblendnodedefinition.md) initializer, [`init(blendMetaParameterDefinition:identifier:)`](phaseblendnodedefinition/init(blendmetaparameterdefinition:identifier:).md), and then access the instance of this class in a sound event’s [`metaParameters`](phasesoundevent/metaparameters.md) dictionary.
- Pass it into the [`PHASEMappedMetaParameterDefinition`](phasemappedmetaparameterdefinition.md) initializer, [`init(inputMetaParameterDefinition:envelope:)`](phasemappedmetaparameterdefinition/init(inputmetaparameterdefinition:envelope:).md). Then, access the instance of this class using the mapped parameter’s [`inputMetaParameterDefinition`](phasemappedmetaparameterdefinition/inputmetaparameterdefinition.md) property.

## Topics

### Creating a Metaparameter Definition
- [convenience init(value: Double)](phasenumbermetaparameterdefinition/init(value:).md)
  Creates a specification for a metaparameter with the given numeric value.
- [convenience init(value: Double, identifier: String)](phasenumbermetaparameterdefinition/init(value:identifier:).md)
  Creates a specification for a named metaparameter with the given numeric value.
- [init(value: Double, minimum: Double, maximum: Double)](phasenumbermetaparameterdefinition/init(value:minimum:maximum:).md)
  Creates a specification for a metaparameter with the given numeric value and range.
- [convenience init(value: Double, minimum: Double, maximum: Double, identifier: String)](phasenumbermetaparameterdefinition/init(value:minimum:maximum:identifier:).md)
  Creates a specification for a named metaparameter with the given numeric value and range.
### Reistricting the Value
- [var minimum: Double](phasenumbermetaparameterdefinition/minimum.md)
  The lowest possible number for the value.
- [var maximum: Double](phasenumbermetaparameterdefinition/maximum.md)
  The highest possible number for the value.

## Relationships

### Inherits From
- [PHASEMetaParameterDefinition](phasemetaparameterdefinition.md)
### Inherited By
- [PHASEMappedMetaParameterDefinition](phasemappedmetaparameterdefinition.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASENumberMetaParameter](phasenumbermetaparameter.md)
  A metaparameter defined by a number that can change over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasenumbermetaparameterdefinition)*