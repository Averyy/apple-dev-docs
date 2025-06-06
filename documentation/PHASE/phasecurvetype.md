# PHASECurveType

**Framework**: PHASE  
**Kind**: enum

Options that apply a mathematical function to an input value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum PHASECurveType
```

#### Overview

PHASE applies curves in several places across the framework:

- A [`PHASEEnvelopeSegment`](phaseenvelopesegment.md) object represents one curved portion of an envelope’s graph.
- The [`PHASEGroup`](phasegroup.md) class applies a curve type to its sounds by fading its volume with the [`fadeGain(gain:duration:curveType:)`](phasegroup/fadegain(gain:duration:curvetype:).md) function, and to its rate, with [`fadeRate(rate:duration:curveType:)`](phasegroup/faderate(rate:duration:curvetype:).md).
- Each [`PHASEGroupPresetSetting`](phasegrouppresetsetting.md) applies a curve to control a setting’s rate of change.

##### Apply a Curve As a Rate of Change

In most cases, PHASE applies curves to output a rate of change. For example, an  envelope segment’s [`curveType`](phaseenvelopesegment/curvetype.md) determines where along the segment’s domain the y-value changes more quickly. The following figure compares all the curves’ rate of change by plotting their input over the range `(0,0)` to `(1,1)`.

![A certesian graph plots all curve types for comparison. The graph encompases the first cartesian quadrant, where each curve begins at coordinate (0,0) and ends at coordinate (1,1). The linear curve plots in a straight line between the two coordinates. An arc that occupies the furthest area from the linear line to the upper left is the inverse cube curve. The next furthest arc from the linear line to the upper left is the inverse squared curve. And the third-furthest arc from the linear line to the upper left is the inverse sine curve. An arc that occupies the furthest area from the linear line to the lower right is the cube curve. The next furthest arc from the linear line to the lower right is the squared curve. And the third-furthest arc from the linear line to the lower right is the sine curve. The sigmoid and inverse sigmoid curves occupy the central area of the graph and center on top of the linear line. The sigmoid curve shapes like the letter S and begins by extending more quickly in the X direction. The inverse sigmoid curve shapes like an inverted letter S and begins by extending more quickly in the Y direction.](https://docs-assets.developer.apple.com/published/028d81d5ddeb5d8960e44a5222c95d85/media-3887371%402x.png)

## Topics

### Types
- [PHASECurveType.linear](phasecurvetype/linear.md)
  A curve that increases uniformly with its input.
- [PHASECurveType.squared](phasecurvetype/squared.md)
  A curve that increases at a rate that squares its input.
- [PHASECurveType.inverseSquared](phasecurvetype/inversesquared.md)
  A curve that increases at a rate of one divided by the input’s square.
- [PHASECurveType.cubed](phasecurvetype/cubed.md)
  A curve that increases at a rate that cubes its input.
- [PHASECurveType.inverseCubed](phasecurvetype/inversecubed.md)
  A curve that increases at a rate of one divided by the input’s cube.
- [PHASECurveType.sine](phasecurvetype/sine.md)
  A sine curve.
- [PHASECurveType.inverseSine](phasecurvetype/inversesine.md)
  An inverse sine curve.
- [PHASECurveType.sigmoid](phasecurvetype/sigmoid.md)
  A sigmoid curve.
- [PHASECurveType.inverseSigmoid](phasecurvetype/inversesigmoid.md)
  An inverse sigmoid curve.
- [PHASECurveType.holdStartValue](phasecurvetype/holdstartvalue.md)
  A curve that equals its start value for the entire duration.
- [PHASECurveType.jumpToEndValue](phasecurvetype/jumptoendvalue.md)
  A curve that equals its end value for the entire duration.
### Initializers
- [init?(rawValue: Int)](phasecurvetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class PHASEEnvelope](phaseenvelope.md)
  A collection of segments that connect to graph a complex curve over a linear input.
- [class PHASEEnvelopeSegment](phaseenvelopesegment.md)
  A curved portion of an envelope.
- [class PHASENumericPair](phasenumericpair.md)
  An ordered pair that defines a bounding box for an envelope.
- [Playback Parameterization](playback-parameterization.md)
  Change the characteristics of in-flight audio by adjusting its properties at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasecurvetype)*