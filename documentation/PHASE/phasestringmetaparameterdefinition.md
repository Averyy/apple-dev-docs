# PHASEStringMetaParameterDefinition

**Framework**: PHASE  
**Kind**: class

A specification for a metaparameter defined by text.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEStringMetaParameterDefinition
```

#### Overview

Use this class to spawn discrete instances of [`PHASENumberMetaParameter`](phasenumbermetaparameter.md), for example, a “player speed” metaparameter that the app changes gradually from `0.0` to `1.0`.

To use a number metaparameter, create an instance of this class and:

- Register it with the engine by calling [`registerGlobalMetaParameter(metaParameterDefinition:)`](phaseassetregistry/registerglobalmetaparameter(metaparameterdefinition:).md), then access the instance of this class in the engine’s [`globalMetaParameters`](phaseassetregistry/globalmetaparameters.md) dictionary.
- Pass it to the [`PHASEBlendNodeDefinition`](phaseblendnodedefinition.md) initializer, [`init(blendMetaParameterDefinition:identifier:)`](phaseblendnodedefinition/init(blendmetaparameterdefinition:identifier:).md), and then access the instance of this class in a sound event’s [`metaParameters`](phasesoundevent/metaparameters.md) dictionary.

## Topics

### Creating a Parameter Definition
- [init(value: String)](phasestringmetaparameterdefinition/init(value:).md)
  Creates a specification for a textual metaparameter with the given value.
- [convenience init(value: String, identifier: String)](phasestringmetaparameterdefinition/init(value:identifier:).md)
  Creates a specification for a named textual metaparameter with the given value.

## Relationships

### Inherits From
- [PHASEMetaParameterDefinition](phasemetaparameterdefinition.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASEStringMetaParameter](phasestringmetaparameter.md)
  A metaparameter with a text definition that can change over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasestringmetaparameterdefinition)*