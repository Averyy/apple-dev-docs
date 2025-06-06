# PHASENumericPair

**Framework**: PHASE  
**Kind**: class

An ordered pair that defines a bounding box for an envelope.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASENumericPair
```

#### Overview

A [`PHASEEnvelope`](phaseenvelope.md) object uses this class to bound the value of its [`range`](phaseenvelope/range.md) and [`domain`](phaseenvelope/domain.md).

## Topics

### Creating a Numeric Pair
- [init(firstValue: Double, secondValue: Double)](phasenumericpair/init(firstvalue:secondvalue:).md)
  Creates a pair of numbers with the given values.
### Defining the Values
- [var first: Double](phasenumericpair/first.md)
  The first value in the pair.
- [var second: Double](phasenumericpair/second.md)
  The second value in the pair.

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
- [class PHASEEnvelopeSegment](phaseenvelopesegment.md)
  A curved portion of an envelope.
- [enum PHASECurveType](phasecurvetype.md)
  Options that apply a mathematical function to an input value.
- [Playback Parameterization](playback-parameterization.md)
  Change the characteristics of in-flight audio by adjusting its properties at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasenumericpair)*