# envelope

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, strong, readonly) PHASEEnvelope * envelope;
```

#### Discussion

The line segments collectively plot an output value for the [`inputMetaParameterDefinition`](./inputmetaparameterdefinition.md) property.

To plot the input, call [`evaluate(x:)`](../phaseenvelope/evaluate%28x%29.md), passing in the input metaparameter’s [`value`](../phasemetaparameter/value.md).

To gradually change the input over time, call [`fade(value:duration:)`](../phasenumbermetaparameter/fade%28value,duration%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemappedmetaparameterdefinition/envelope)*