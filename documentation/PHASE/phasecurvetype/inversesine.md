# PHASECurveType.inverseSine

**Framework**: PHASE  
**Kind**: case

An inverse sine curve.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case inverseSine
```

#### Discussion

The function `y` `=` `sin^-1(x)` shapes this curve. The inverse sine curve behaves like [`PHASECurveType.sine`](phasecurvetype/sine.md), only rotated `90` degrees.

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
- [PHASECurveType.sigmoid](phasecurvetype/sigmoid.md)
  A sigmoid curve.
- [PHASECurveType.inverseSigmoid](phasecurvetype/inversesigmoid.md)
  An inverse sigmoid curve.
- [PHASECurveType.holdStartValue](phasecurvetype/holdstartvalue.md)
  A curve that equals its start value for the entire duration.
- [PHASECurveType.jumpToEndValue](phasecurvetype/jumptoendvalue.md)
  A curve that equals its end value for the entire duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasecurvetype/inversesine)*