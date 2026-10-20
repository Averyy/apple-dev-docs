# init(arithmetic_function:arithmetic_function_fields:activation:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new arithmetic layer parameters structure.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
init(arithmetic_function: BNNSArithmeticFunction, arithmetic_function_fields: UnsafeMutableRawPointer, activation: BNNSActivation)
```

## Parameters

- `arithmetic_function`: The arithmetic function.
- `arithmetic_function_fields`: A pointer to an arithmetic function field structure.
- `activation`: The activation function that the layer applies to the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersarithmetic/init(arithmetic_function:arithmetic_function_fields:activation:))*