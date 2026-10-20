# PHASENumberMetaParameterDefinition

**Framework**: PHASE  
**Kind**: class  
**Role**: Class

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

```objc
@interface PHASENumberMetaParameterDefinition : PHASEMetaParameterDefinition
```

#### Overview

Use this class to spawn discrete instances of [`PHASENumberMetaParameter`](./phasenumbermetaparameter.md), for example, a “player speed” metaparameter that the app changes gradually from `0.0` to `1.0`.

To use a number metaparameter, create an instance of this class and:

- Register it with the engine by calling [`registerGlobalMetaParameter(metaParameterDefinition:)`](./phaseassetregistry/registerglobalmetaparameter%28metaparameterdefinition%29.md), then access the instance of this class in the engine’s [`globalMetaParameters`](./phaseassetregistry/globalmetaparameters.md) dictionary.
- Pass it to the [`PHASEBlendNodeDefinition`](./phaseblendnodedefinition.md) initializer, [`init(blendMetaParameterDefinition:identifier:)`](./phaseblendnodedefinition/init%28blendmetaparameterdefinition,identifier%29.md), and then access the instance of this class in a sound event’s [`metaParameters`](./phasesoundevent/metaparameters.md) dictionary.
- Pass it into the [`PHASEMappedMetaParameterDefinition`](./phasemappedmetaparameterdefinition.md) initializer, [`init(inputMetaParameterDefinition:envelope:)`](./phasemappedmetaparameterdefinition/init%28inputmetaparameterdefinition,envelope%29.md). Then, access the instance of this class using the mapped parameter’s [`inputMetaParameterDefinition`](./phasemappedmetaparameterdefinition/inputmetaparameterdefinition.md) property.

## Topics

### Creating a Metaparameter Definition
- [convenience init(value: Double)](./phasenumbermetaparameterdefinition/init%28value%29.md)
  Creates a specification for a metaparameter with the given numeric value.
- [convenience init(value: Double, identifier: String)](./phasenumbermetaparameterdefinition/init%28value,identifier%29.md)
  Creates a specification for a named metaparameter with the given numeric value.
- [init(value: Double, minimum: Double, maximum: Double)](./phasenumbermetaparameterdefinition/init%28value,minimum,maximum%29.md)
  Creates a specification for a metaparameter with the given numeric value and range.
- [convenience init(value: Double, minimum: Double, maximum: Double, identifier: String)](./phasenumbermetaparameterdefinition/init%28value,minimum,maximum,identifier%29.md)
  Creates a specification for a named metaparameter with the given numeric value and range.
### Reistricting the Value
- [var minimum: Double](./phasenumbermetaparameterdefinition/minimum.md)
  The lowest possible number for the value.
- [var maximum: Double](./phasenumbermetaparameterdefinition/maximum.md)
  The highest possible number for the value.

## Relationships

### Inherits From
- [PHASEMetaParameterDefinition](./phasemetaparameterdefinition.md)
### Inherited By
- [PHASEMappedMetaParameterDefinition](./phasemappedmetaparameterdefinition.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Linear Metaparameters
- [class PHASENumberMetaParameter](./phasenumbermetaparameter.md)
  A metaparameter defined by a number that can change over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasenumbermetaparameterdefinition)*