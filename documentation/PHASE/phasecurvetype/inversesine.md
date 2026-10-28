# PHASECurveType.inverseSine

**Framework**: PHASE  
**Kind**: case  
**Role**: Case

An inverse sine curve.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
case inverseSine
```

```c
PHASECurveTypeInverseSine
```

## Discussion

The function `y` `=` `sin^-1(x)` shapes this curve. The inverse sine curve behaves like [`PHASECurveType.sine`](./sine.md), only rotated `90` degrees.

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
- [PHASECurveType.sine](./sine.md)
  A sine curve.
- [PHASECurveType.sigmoid](./sigmoid.md)
  A sigmoid curve.
- [PHASECurveType.inverseSigmoid](./inversesigmoid.md)
  An inverse sigmoid curve.
- [PHASECurveType.holdStartValue](./holdstartvalue.md)
  A curve that equals its start value for the entire duration.
- [PHASECurveType.jumpToEndValue](./jumptoendvalue.md)
  A curve that equals its end value for the entire duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasecurvetype/inversesine)*