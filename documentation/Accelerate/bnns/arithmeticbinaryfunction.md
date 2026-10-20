# BNNS.ArithmeticBinaryFunction

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Constants that describe binary arithmetic functions.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
enum ArithmeticBinaryFunction
```

## Topics

### Binary Arithmetic Functions
- [BNNS.ArithmeticBinaryFunction.add](./arithmeticbinaryfunction/add.md)
  An operation that calculates the element-wise sum of its two inputs.
- [BNNS.ArithmeticBinaryFunction.subtract](./arithmeticbinaryfunction/subtract.md)
  An operation that calculates the element-wise difference of its two inputs.
- [BNNS.ArithmeticBinaryFunction.divide](./arithmeticbinaryfunction/divide.md)
  An operation that calculates the element-wise division of its two inputs.
- [BNNS.ArithmeticBinaryFunction.divideNoNaN](./arithmeticbinaryfunction/dividenonan.md)
  An operation that calculates the element-wise division of its two inputs and returns zero if the second input is zero.
- [BNNS.ArithmeticBinaryFunction.multiply](./arithmeticbinaryfunction/multiply.md)
  An operation that calculates the element-wise product of its two inputs.
- [BNNS.ArithmeticBinaryFunction.multiplyNoNaN](./arithmeticbinaryfunction/multiplynonan.md)
  An operation that calculates the element-wise product of its two inputs and returns zero if the second input is zero, even if the first input is NaN or infinity.
- [BNNS.ArithmeticBinaryFunction.pow](./arithmeticbinaryfunction/pow.md)
  An operation that calculates the element-wise first input raised to the power of its second input.
- [BNNS.ArithmeticBinaryFunction.max](./arithmeticbinaryfunction/max.md)
  An operation that calculates the element-wise maximum of its two inputs.
- [BNNS.ArithmeticBinaryFunction.min](./arithmeticbinaryfunction/min.md)
  An operation that calculates the element-wise minimum of its two inputs.
### Enumeration Cases
- [BNNS.ArithmeticBinaryFunction.flooringDivide](./arithmeticbinaryfunction/flooringdivide.md)
- [BNNS.ArithmeticBinaryFunction.truncatingDivide](./arithmeticbinaryfunction/truncatingdivide.md)
- [BNNS.ArithmeticBinaryFunction.truncatingRemainder](./arithmeticbinaryfunction/truncatingremainder.md)

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/arithmeticbinaryfunction)*