# envelope

**Framework**: PHASE  
**Kind**: property

A collection of line segments that curve and connect to form a graph.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var envelope: PHASEEnvelope { get }
```

#### Discussion

The line segments collectively plot an output value for the [`inputMetaParameterDefinition`](phasemappedmetaparameterdefinition/inputmetaparameterdefinition.md) property.

To plot the input, call [`evaluate(x:)`](phaseenvelope/evaluate(x:).md), passing in the input metaparameter’s [`value`](phasemetaparameter/value.md).

To gradually change the input over time, call [`fade(value:duration:)`](phasenumbermetaparameter/fade(value:duration:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemappedmetaparameterdefinition/envelope)*