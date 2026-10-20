# BNNSFilterApplyBackwardTwoInputBatch(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Applies a filter backward to generate input deltas, weights delta and bias delta.

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
func BNNSFilterApplyBackwardTwoInputBatch(_ filter: BNNSFilter?, _ batch_size: Int, _ inA: UnsafeRawPointer?, _ inA_stride: Int, _ inA_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>?, _ inA_delta_stride: Int, _ inB: UnsafeRawPointer?, _ inB_stride: Int, _ inB_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>?, _ inB_delta_stride: Int, _ out: UnsafeRawPointer?, _ out_stride: Int, _ out_delta: UnsafePointer<BNNSNDArrayDescriptor>, _ out_delta_stride: Int, _ weights_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>?, _ bias_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>?) -> Int32
```

```c
int BNNSFilterApplyBackwardTwoInputBatch(BNNSFilter filter, size_t batch_size, const void *inA, size_t inA_stride, BNNSNDArrayDescriptor *inA_delta, size_t inA_delta_stride, const void *inB, size_t inB_stride, BNNSNDArrayDescriptor *inB_delta, size_t inB_delta_stride, const void *out, size_t out_stride, const BNNSNDArrayDescriptor *out_delta, size_t out_delta_stride, BNNSNDArrayDescriptor *weights_delta, BNNSNDArrayDescriptor *bias_delta);
```

## Parameters

- `filter`: The filter to apply.
- `batch_size`: The number of input-output pairs.
- `inA`: Pointer to the first input data.
- `inA_stride`: Increment, in values, between first input objects.
- `inA_delta`: The descriptor of the first input delta.
- `inA_delta_stride`: Increment, in values, between first input delta objects.
- `inB`: Pointer to the second input data.
- `inB_stride`: Increment, in values, between second input objects.
- `inB_delta`: The descriptor of the second input delta.
- `inB_delta_stride`: Increment, in values, between second input delta objects.
- `out`: Pointer to the output data.
- `out_stride`: Increment, in values, between output objects.
- `out_delta`: The descriptor of the output delta.
- `out_delta_stride`: Increment, in values, between output delta objects.
- `weights_delta`: The descriptor of the weights delta.
- `bias_delta`: The descriptor of the bias delta.

## See Also

### Backpropagation Functions
- [func BNNSFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<BNNSNDArrayDescriptor>?) -> Int32](./bnnsfilterapplybackwardbatch%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies a filter backward to generate input delta, weights delta and bias delta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterapplybackwardtwoinputbatch(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:))*