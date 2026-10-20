# init(alpha:i_desc:o_desc:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new Gram matrix layer parameters structure from the specified parameters.

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
init(alpha: Float, i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor)
```

## Parameters

- `alpha`: A value to scale the result.
- `i_desc`: The descriptor of the input.
- `o_desc`: The descriptor of the output.

## See Also

### Initializers
- [init()](./init%28%29.md)
  Returns a new Gram matrix layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersgram/init(alpha:i_desc:o_desc:))*