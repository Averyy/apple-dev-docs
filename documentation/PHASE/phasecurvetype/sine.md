# PHASECurveType.sine

**Framework**: PHASE  
**Kind**: case  
**Role**: Case

A sine curve.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
case sine
```

```c
PHASECurveTypeSine
```

## Discussion

The function `y` `=` `sin(x)` shapes this curve. For a linear input along the `x`-axis, a sine curve gradually moves upward then downward in the `y`-direction, in a repeating fashion.

## See Also

### Types
- [PHASECurveType.linear](./linear.md)
  A curve that increases uniformly with its input.
- [PHASECurveType.squared](./squared.md)
  A curve that increases at a rate that squares its input.
- [PHASECurveType.inverseSquared](./inversesquared.md)
  A curve that increases at a rate of one divided by the input’s square.
- [PHASECurveType.cubed](./cubed.md)
  A curve that increases at a rate that cubes its input.
- [PHASECurveType.inverseCubed](./inversecubed.md)
  A curve that increases at a rate of one divided by the input’s cube.
- [PHASECurveType.inverseSine](./inversesine.md)
  An inverse sine curve.
- [PHASECurveType.sigmoid](./sigmoid.md)
  A sigmoid curve.
- [PHASECurveType.inverseSigmoid](./inversesigmoid.md)
  An inverse sigmoid curve.
- [PHASECurveType.holdStartValue](./holdstartvalue.md)
  A curve that equals its start value for the entire duration.
- [PHASECurveType.jumpToEndValue](./jumptoendvalue.md)
  A curve that equals its end value for the entire duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasecurvetype/sine)*