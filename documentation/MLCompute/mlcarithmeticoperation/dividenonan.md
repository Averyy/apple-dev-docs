# MLCArithmeticOperation.divideNoNaN

**Framework**: ML Compute  
**Kind**: case

Calculates the element-wise division of the inputs, and returns `0` if the denominator is `0`.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+

## Declaration

```swift
case divideNoNaN
```

#### Discussion

Returns `0` if the denominator is `0`.

## See Also

- [MLCArithmeticOperation.add](mlcarithmeticoperation/add.md)
  Calculates the element-wise sum of the inputs.
- [MLCArithmeticOperation.subtract](mlcarithmeticoperation/subtract.md)
  Calculates the element-wise difference between the inputs.
- [MLCArithmeticOperation.multiply](mlcarithmeticoperation/multiply.md)
  Calculates the element-wise product of the inputs.
- [MLCArithmeticOperation.multiplyNoNaN](mlcarithmeticoperation/multiplynonan.md)
  Calculates the element-wise product of the inputs, and returns `0` when the result isn’t a number or infinity.
- [MLCArithmeticOperation.divide](mlcarithmeticoperation/divide.md)
  Calculates the element-wise division of the inputs.
- [MLCArithmeticOperation.min](mlcarithmeticoperation/min.md)
  Calculates the element-wise minimum of the inputs.
- [MLCArithmeticOperation.max](mlcarithmeticoperation/max.md)
  Calculates the element-wise maximum the inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcarithmeticoperation/dividenonan)*