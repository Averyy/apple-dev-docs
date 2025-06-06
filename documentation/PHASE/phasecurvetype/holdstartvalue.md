# PHASECurveType.holdStartValue

**Framework**: PHASE  
**Kind**: case

A curve that equals its start value for the entire duration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
case holdStartValue
```

#### Discussion

Use this type for step function curves, such as when mapping a continuously varying input value to a discrete set of output values.

## See Also

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
- [PHASECurveType.jumpToEndValue](phasecurvetype/jumptoendvalue.md)
  A curve that equals its end value for the entire duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasecurvetype/holdstartvalue)*