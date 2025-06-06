# PHASENumberMetaParameter

**Framework**: PHASE  
**Kind**: class

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

#### Overview

This class contains a number that updates, like a “player speed” metaparameter that the app changes gradually from `0.0` to `1.0`.

To create an instance of this class, first create a [`PHASENumberMetaParameterDefinition`](phasenumbermetaparameterdefinition.md), and either:

- Register it with the engine by calling [`registerGlobalMetaParameter(metaParameterDefinition:)`](phaseassetregistry/registerglobalmetaparameter(metaparameterdefinition:).md), then access the instance of this class in the engine’s [`globalMetaParameters`](phaseassetregistry/globalmetaparameters.md) dictionary.
- Pass it to the [`PHASEBlendNodeDefinition`](phaseblendnodedefinition.md) initializer, [`init(blendMetaParameterDefinition:identifier:)`](phaseblendnodedefinition/init(blendmetaparameterdefinition:identifier:).md), and then access the instance of this class in a sound event’s [`metaParameters`](phasesoundevent/metaparameters.md) dictionary.
- Use it as the input value for a [`PHASEMappedMetaParameterDefinition`](phasemappedmetaparameterdefinition.md) by passing it into the [`init(inputMetaParameterDefinition:envelope:)`](phasemappedmetaparameterdefinition/init(inputmetaparameterdefinition:envelope:).md) initializer. Then, access the instance of this class using the mapped parameter’s [`inputMetaParameterDefinition`](phasemappedmetaparameterdefinition/inputmetaparameterdefinition.md) property.

## Topics

### Inspecting Extremes
- [var minimum: Double](phasenumbermetaparameter/minimum.md)
  The lowest possible number for the value.
- [var maximum: Double](phasenumbermetaparameter/maximum.md)
  The highest possible number for the value.
### Interpolating the Value
- [func fade(value: Double, duration: TimeInterval)](phasenumbermetaparameter/fade(value:duration:).md)
  Sets the value gradually over the given amount of time.

## Relationships

### Inherits From
- [PHASEMetaParameter](phasemetaparameter.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASENumberMetaParameterDefinition](phasenumbermetaparameterdefinition.md)
  A specification for a metaparameter defined by a number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasenumbermetaparameter)*