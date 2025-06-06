# PHASECurveType.sine

**Framework**: PHASE  
**Kind**: case

A sine curve.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
case sine
```

#### Discussion

The function `y` `=` `sin(x)` shapes this curve. For a linear input along the `x`-axis, a sine curve gradually moves upward then downward in the `y`-direction, in a repeating fashion.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasecurvetype/sine)*