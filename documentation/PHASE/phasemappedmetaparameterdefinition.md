# PHASEMappedMetaParameterDefinition

**Framework**: PHASE  
**Kind**: class  
**Role**: Class

A metaparameter that graphs an input value on a set of mathematical curves.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEMappedMetaParameterDefinition
```

```objc
@interface PHASEMappedMetaParameterDefinition : PHASENumberMetaParameterDefinition
```

#### Overview

This class takes a metaparameter as input and plots its value on a curve defined by the [`envelope`](./phasemappedmetaparameterdefinition/envelope.md) property.

Whereas the envelope’s function in [`PHASEBlendNodeDefinition`](./phaseblendnodedefinition.md) and [`PHASEEnvelopeDistanceModelParameters`](./phaseenvelopedistancemodelparameters.md) takes time because the relevant audio starts as its input parameter, in the case of the envelope property for this class, the app has full control over the input metaparameter’s value.

## Topics

### Creating a Mapped Metaparameter
- [init(inputMetaParameterDefinition: PHASENumberMetaParameterDefinition, envelope: PHASEEnvelope)](./phasemappedmetaparameterdefinition/init%28inputmetaparameterdefinition,envelope%29.md)
  Creates a specification for a metaparameter that the app plots on a graph defined by the given set of curves.
- [convenience init(inputMetaParameterDefinition: PHASENumberMetaParameterDefinition, envelope: PHASEEnvelope, identifier: String)](./phasemappedmetaparameterdefinition/init%28inputmetaparameterdefinition,envelope,identifier%29.md)
  Creates a specification for a named metaparameter that the app plots on a graph defined by the given set of curves.
### Inspecting the Input Parameter
- [var inputMetaParameterDefinition: PHASENumberMetaParameterDefinition](./phasemappedmetaparameterdefinition/inputmetaparameterdefinition.md)
  A linear input value to plot on a curve.
### Inspecting the Envelope
- [var envelope: PHASEEnvelope](./phasemappedmetaparameterdefinition/envelope.md)
  A collection of line segments that curve and connect to form a graph.

## Relationships

### Inherits From
- [PHASENumberMetaParameterDefinition](./phasenumbermetaparameterdefinition.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemappedmetaparameterdefinition)*