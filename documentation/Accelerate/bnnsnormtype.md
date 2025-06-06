# BNNSNormType

**Framework**: Accelerate  
**Kind**: struct

Constants that describe norm types.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSNormType
```

## Topics

### Constants
- [init(UInt32)](bnnsnormtype/init(_:).md)
  Creates a new instance with the specified raw value.
- [init(rawValue: UInt32)](bnnsnormtype/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [var rawValue: UInt32](bnnsnormtype/rawvalue.md)
  The corresponding value of the raw type.
- [var BNNSL2Norm: BNNSNormType](bnnsl2norm.md)
  A constant that represents the L2 norm.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static func computeNorm(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axes: [Int]?) throws](bnns/computenorm(input:output:axes:).md)
  Computes the Euclidean norm and writes the result to the output tensor.
- [static func computeNormBackward(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axes: [Int]?, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor) throws](bnns/computenormbackward(input:output:axes:outputgradient:generatinginputgradient:).md)
  Backpropogates gradients for the compute norm function.
- [func BNNSComputeNorm(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, BNNSNormType, UInt32) -> Int32](bnnscomputenorm(_:_:_:_:).md)
  Computes the specified norm over an entire tensor or the specified axes.
- [func BNNSComputeNormBackward(UnsafeRawPointer, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafeRawPointer, UnsafePointer<BNNSNDArrayDescriptor>, BNNSNormType, UInt32) -> Int32](bnnscomputenormbackward(_:_:_:_:_:_:).md)
  Backpropogates gradients for the compute norm function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsnormtype)*