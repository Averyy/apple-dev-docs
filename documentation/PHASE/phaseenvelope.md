# PHASEEnvelope

**Framework**: PHASE  
**Kind**: class

A collection of segments that connect to graph a complex curve over a linear input.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEEnvelope
```

#### Overview

In traditional audio uses, an  defines a complex graph that determines the volume of audio data over an input duration. PHASE uses envelopes in a similar way. Given a value on the envelope’s input axis, the [`evaluate(x:)`](phaseenvelope/evaluate(x:).md) function plots and returns the result on the output axis. The following are possible uses of this class:

- Sound event nodes, such as [`PHASEBlendNodeDefinition`](phaseblendnodedefinition.md), can shape their volume using an envelope; see [`addRange(envelope:subtree:)`](phaseblendnodedefinition/addrange(envelope:subtree:).md).
- Distance models shape sounds with a 3D position using an envelope; see [`PHASEEnvelopeDistanceModelParameters`](phaseenvelopedistancemodelparameters.md).
- An envelope can do more than shape audio. To gradually change an envelope’s input value over time, use the [`PHASEMappedMetaParameterDefinition`](phasemappedmetaparameterdefinition.md) class, which creates a function with a metaparameter value as input. An app can use the numeric result for any purpose. For example, the x-axis can be distance and the y-axis can be playback rate.

At runtime, PHASE determines whether a particular member of the [`segments`](phaseenvelope/segments.md) array slopes up or down along the domain depending on the envelope’s particular use case.

##### Create an Envelope and Shape Its Curve

To use an envelope in your app, define its shape by defining a series of segments. Each segment specifies a curve that collectively connect to form a graph. The following code creates an envelope with a single segment that’s shaped like the lettter 

The graph flexes at runtime depending on the source content on which the envelope operates. A [`PHASEEnvelope`](phaseenvelope.md) doesn’t constrain the [`evaluate(x:)`](phaseenvelope/evaluate(x:).md) function’s output to predertermined values. Instead, PHASE applies the envelope’s curves to the source content as a rate of change.

## Topics

### Creating an Envelope
- [init?(startPoint: simd_double2, segments: [PHASEEnvelopeSegment])](phaseenvelope/init(startpoint:segments:).md)
  Creates an envelope with a start point and segments.
### Inspecting the Envelope
- [func evaluate(x: Double) -> Double](phaseenvelope/evaluate(x:).md)
  Provides the height of the envelope for an input value.
- [var segments: [PHASEEnvelopeSegment]](phaseenvelope/segments.md)
  An array of the envelope’s segments.
- [var startPoint: simd_double2](phaseenvelope/startpoint.md)
  The starting point along the envelope’s duration.
### Bounding the Input
- [var domain: PHASENumericPair](phaseenvelope/domain.md)
  The range of the envelope’s possible input values.
- [var range: PHASENumericPair](phaseenvelope/range.md)
  The bounds of the output value.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASEEnvelopeSegment](phaseenvelopesegment.md)
  A curved portion of an envelope.
- [enum PHASECurveType](phasecurvetype.md)
  Options that apply a mathematical function to an input value.
- [class PHASENumericPair](phasenumericpair.md)
  An ordered pair that defines a bounding box for an envelope.
- [Playback Parameterization](playback-parameterization.md)
  Change the characteristics of in-flight audio by adjusting its properties at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseenvelope)*