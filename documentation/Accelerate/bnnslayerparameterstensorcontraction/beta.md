# beta

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

A value, that must be either 0.0 or 1.0, you use to scale the existing output before the operation adds it to the result.

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
var beta: Float
```

```c
float beta;
```

## See Also

### Instance Properties
- [var operation: UnsafePointer<CChar>](./operation.md)
  The string that describes the operation.
- [var alpha: Float](./alpha.md)
  Scaling that the operation applies to the result.
- [var iA_desc: BNNSNDArrayDescriptor](./ia_desc.md)
  The descriptor of input matrix *A*.
- [var iB_desc: BNNSNDArrayDescriptor](./ib_desc.md)
  The descriptor of input matrix *B*.
- [var o_desc: BNNSNDArrayDescriptor](./o_desc.md)
  The descriptor of the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterstensorcontraction/beta)*