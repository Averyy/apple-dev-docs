# PHASENumberMetaParameter

**Framework**: PHASE  
**Kind**: class  
**Role**: Class

A metaparameter defined by a number that can change over time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASENumberMetaParameter
```

```objc
@interface PHASENumberMetaParameter : PHASEMetaParameter
```

## Overview

This class contains a number that updates, like a “player speed” metaparameter that the app changes gradually from `0.0` to `1.0`.

To create an instance of this class, first create a [`PHASENumberMetaParameterDefinition`](./phasenumbermetaparameterdefinition.md), and either:

- Register it with the engine by calling [`registerGlobalMetaParameter(metaParameterDefinition:)`](./phaseassetregistry/registerglobalmetaparameter%28metaparameterdefinition%29.md), then access the instance of this class in the engine’s [`globalMetaParameters`](./phaseassetregistry/globalmetaparameters.md) dictionary.
- Pass it to the [`PHASEBlendNodeDefinition`](./phaseblendnodedefinition.md) initializer, [`init(blendMetaParameterDefinition:identifier:)`](./phaseblendnodedefinition/init%28blendmetaparameterdefinition,identifier%29.md), and then access the instance of this class in a sound event’s [`metaParameters`](./phasesoundevent/metaparameters.md) dictionary.
- Use it as the input value for a [`PHASEMappedMetaParameterDefinition`](./phasemappedmetaparameterdefinition.md) by passing it into the [`init(inputMetaParameterDefinition:envelope:)`](./phasemappedmetaparameterdefinition/init%28inputmetaparameterdefinition,envelope%29.md) initializer. Then, access the instance of this class using the mapped parameter’s [`inputMetaParameterDefinition`](./phasemappedmetaparameterdefinition/inputmetaparameterdefinition.md) property.

## Topics

### Inspecting Extremes
- [var minimum: Double](./phasenumbermetaparameter/minimum.md)
  The lowest possible number for the value.
- [var maximum: Double](./phasenumbermetaparameter/maximum.md)
  The highest possible number for the value.
### Interpolating the Value
- [func fade(value: Double, duration: TimeInterval)](./phasenumbermetaparameter/fade%28value,duration%29.md)
  Sets the value gradually over the given amount of time.

## Relationships

### Inherits From
- [PHASEMetaParameter](./phasemetaparameter.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Linear Metaparameters
- [class PHASENumberMetaParameterDefinition](./phasenumbermetaparameterdefinition.md)
  A specification for a metaparameter defined by a number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasenumbermetaparameter)*