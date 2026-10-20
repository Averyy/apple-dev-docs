# BNNSNormType

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Constants that describe norm types.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct BNNSNormType
```

```c
typedef enum { ... } BNNSNormType;
```

## Topics

### Constants
- [init(UInt32)](./bnnsnormtype/init%28_%29.md)
  Creates a new instance with the specified raw value.
- [init(rawValue: UInt32)](./bnnsnormtype/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.
- [var rawValue: UInt32](./bnnsnormtype/rawvalue.md)
  The corresponding value of the raw type.
- [var BNNSL2Norm: BNNSNormType](./bnnsl2norm.md)
  A constant that represents the L2 norm.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Compute norm functions
- [static func computeNorm(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axes: [Int]?) throws](./bnns/computenorm%28input,output,axes%29.md)
  Computes the Euclidean norm and writes the result to the output tensor.
- [static func computeNormBackward(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axes: [Int]?, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor) throws](./bnns/computenormbackward%28input,output,axes,outputgradient,generatinginputgradient%29.md)
  Backpropogates gradients for the compute norm function.
- [func BNNSComputeNorm(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, BNNSNormType, UInt32) -> Int32](./bnnscomputenorm%28_,_,_,_%29.md)
  Computes the specified norm over an entire tensor or the specified axes.
- [func BNNSComputeNormBackward(UnsafeRawPointer, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafeRawPointer, UnsafePointer<BNNSNDArrayDescriptor>, BNNSNormType, UInt32) -> Int32](./bnnscomputenormbackward%28_,_,_,_,_,_%29.md)
  Backpropogates gradients for the compute norm function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsnormtype)*