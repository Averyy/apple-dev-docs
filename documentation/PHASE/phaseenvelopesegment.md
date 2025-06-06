# PHASEEnvelopeSegment

**Framework**: PHASE  
**Kind**: class

A curved portion of an envelope.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEEnvelopeSegment
```

#### Overview

This class specifies a curve that determines the _y-_value rate of change over a particular portion of an envelope’s graph. For example, the difference between a [`PHASECurveType.cubed`](phasecurvetype/cubed.md) segment and an [`PHASECurveType.inverseCubed`](phasecurvetype/inversecubed.md) segment is that they share opposite rates of change; where the cubed curve’s  value changes fastest in the segment’s domain, the inverse-cubed curve changes slowest, and vice versa.

## Topics

### Creating a Segment
- [init(endPoint: simd_double2, curveType: PHASECurveType)](phaseenvelopesegment/init(endpoint:curvetype:).md)
  Creates a curved portion of an envelope.
### Shaping a Segment
- [var curveType: PHASECurveType](phaseenvelopesegment/curvetype.md)
  A curve along the envelope that shapes the segment.
- [var endPoint: simd_double2](phaseenvelopesegment/endpoint.md)
  A point that identifies the end of the segment along the envelope.

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

- [class PHASEEnvelope](phaseenvelope.md)
  A collection of segments that connect to graph a complex curve over a linear input.
- [enum PHASECurveType](phasecurvetype.md)
  Options that apply a mathematical function to an input value.
- [class PHASENumericPair](phasenumericpair.md)
  An ordered pair that defines a bounding box for an envelope.
- [Playback Parameterization](playback-parameterization.md)
  Change the characteristics of in-flight audio by adjusting its properties at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseenvelopesegment)*