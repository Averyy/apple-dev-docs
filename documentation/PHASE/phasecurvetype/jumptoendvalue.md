# PHASECurveType.jumpToEndValue

**Framework**: PHASE  
**Kind**: case  
**Role**: Case

A curve that equals its end value for the entire duration.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
case jumpToEndValue
```

```c
PHASECurveTypeJumpToEndValue
```

## Discussion

Use this type for step function curves, such as when mapping a continuously varying input value to a discrete set of output values.

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
- [PHASECurveType.inverseSine](./inversesine.md)
  An inverse sine curve.
- [PHASECurveType.sigmoid](./sigmoid.md)
  A sigmoid curve.
- [PHASECurveType.inverseSigmoid](./inversesigmoid.md)
  An inverse sigmoid curve.
- [PHASECurveType.holdStartValue](./holdstartvalue.md)
  A curve that equals its start value for the entire duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasecurvetype/jumptoendvalue)*