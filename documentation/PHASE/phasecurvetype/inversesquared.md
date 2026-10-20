# PHASECurveType.inverseSquared

**Framework**: PHASE  
**Kind**: case  
**Role**: Case

A curve that increases at a rate of one divided by the input’s square.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
case inverseSquared
```

```c
PHASECurveTypeInverseSquared
```

#### Discussion

The function `y` `=` `1` `/` `x^2` shapes this curve.

## See Also

### Types
- [PHASECurveType.linear](./linear.md)
  A curve that increases uniformly with its input.
- [PHASECurveType.squared](./squared.md)
  A curve that increases at a rate that squares its input.
- [PHASECurveType.cubed](./cubed.md)
  A curve that increases at a rate that cubes its input.
- [PHASECurveType.inverseCubed](./inversecubed.md)
  A curve that increases at a rate of one divided by the input’s cube.
- [PHASECurveType.sine](./sine.md)
  A sine curve.
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

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasecurvetype/inversesquared)*