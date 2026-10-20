# MPSCNNSubtract

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A subtraction operator.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNSubtract
```

```objc
@interface MPSCNNSubtract : MPSCNNArithmetic
```

## Topics

### Initializers
- [init(device: any MTLDevice)](./mpscnnsubtract/init%28device%29.md)

## Relationships

### Inherits From
- [MPSCNNArithmetic](./mpscnnarithmetic.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Arithmetic Layers
- [class MPSCNNAdd](./mpscnnadd.md)
  An addition operator.
- [class MPSCNNAddGradient](./mpscnnaddgradient.md)
  A gradient addition operator.
- [class MPSCNNSubtractGradient](./mpscnnsubtractgradient.md)
  A gradient subtraction operator.
- [class MPSCNNMultiply](./mpscnnmultiply.md)
  A multiply operator.
- [class MPSCNNMultiplyGradient](./mpscnnmultiplygradient.md)
  A gradient multiply operator.
- [class MPSCNNDivide](./mpscnndivide.md)
  A division operator.
- [class MPSCNNArithmetic](./mpscnnarithmetic.md)
  The base class for arithmetic operators.
- [class MPSCNNArithmeticGradient](./mpscnnarithmeticgradient.md)
  The base class for gradient arithmetic operators.
- [class MPSCNNArithmeticGradientState](./mpscnnarithmeticgradientstate.md)
  An object that stores the clamp mask used by gradient arithmetic operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnsubtract)*