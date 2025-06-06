# MLCArithmeticOperation.multiplyNoNaN

**Framework**: ML Compute  
**Kind**: case

Calculates the element-wise product of the inputs, and returns `0` when the result isn’t a number or infinity.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+

## Declaration

```swift
case multiplyNoNaN
```

#### Discussion

Returns `0` if `y` in `x * y` is zero, even if `x` isn’t a number (`NaN)` or infinity (`INF)`.

## See Also

- [MLCArithmeticOperation.add](mlcarithmeticoperation/add.md)
  Calculates the element-wise sum of the inputs.
- [MLCArithmeticOperation.subtract](mlcarithmeticoperation/subtract.md)
  Calculates the element-wise difference between the inputs.
- [MLCArithmeticOperation.multiply](mlcarithmeticoperation/multiply.md)
  Calculates the element-wise product of the inputs.
- [MLCArithmeticOperation.divide](mlcarithmeticoperation/divide.md)
  Calculates the element-wise division of the inputs.
- [MLCArithmeticOperation.divideNoNaN](mlcarithmeticoperation/dividenonan.md)
  Calculates the element-wise division of the inputs, and returns `0` if the denominator is `0`.
- [MLCArithmeticOperation.min](mlcarithmeticoperation/min.md)
  Calculates the element-wise minimum of the inputs.
- [MLCArithmeticOperation.max](mlcarithmeticoperation/max.md)
  Calculates the element-wise maximum the inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcarithmeticoperation/multiplynonan)*