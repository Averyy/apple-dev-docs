# MLCArithmeticOperation.subtract

**Framework**: ML Compute  
**Kind**: case  
**Role**: Case

Calculates the element-wise difference between the inputs.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
case subtract
```

```c
MLCArithmeticOperationSubtract
```

## See Also

### Basic Operations
- [MLCArithmeticOperation.add](./add.md)
  Calculates the element-wise sum of the inputs.
- [MLCArithmeticOperation.multiply](./multiply.md)
  Calculates the element-wise product of the inputs.
- [MLCArithmeticOperation.multiplyNoNaN](./multiplynonan.md)
  Calculates the element-wise product of the inputs, and returns `0` when the result isn’t a number or infinity.
- [MLCArithmeticOperation.divide](./divide.md)
  Calculates the element-wise division of the inputs.
- [MLCArithmeticOperation.divideNoNaN](./dividenonan.md)
  Calculates the element-wise division of the inputs, and returns `0` if the denominator is `0`.
- [MLCArithmeticOperation.min](./min.md)
  Calculates the element-wise minimum of the inputs.
- [MLCArithmeticOperation.max](./max.md)
  Calculates the element-wise maximum the inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcarithmeticoperation/subtract)*