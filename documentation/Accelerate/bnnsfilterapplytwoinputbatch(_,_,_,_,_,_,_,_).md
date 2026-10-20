# BNNSFilterApplyTwoInputBatch(_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Applies a filter to a set of input object pairs, writing the result to a set of output objects.

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
func BNNSFilterApplyTwoInputBatch(_ filter: BNNSFilter?, _ batch_size: Int, _ inA: UnsafeRawPointer, _ inA_stride: Int, _ inB: UnsafeRawPointer, _ inB_stride: Int, _ out: UnsafeMutableRawPointer, _ out_stride: Int) -> Int32
```

```c
int BNNSFilterApplyTwoInputBatch(BNNSFilter filter, size_t batch_size, const void *inA, size_t inA_stride, const void *inB, size_t inB_stride, void *out, size_t out_stride);
```

## Parameters

- `filter`: The filter to apply.
- `batch_size`: The number of input-output pairs.
- `inA`: Pointer to the first input data.
- `inA_stride`: Increment, in values, between first input objects.
- `inB`: Pointer to the second input data.
- `inB_stride`: Increment, in values, between second input objects.
- `out`: Pointer to the output data.
- `out_stride`: Increment, in values, between output objects.

## See Also

### Forward Propagation Functions
- [func BNNSFilterApply(BNNSFilter?, UnsafeRawPointer, UnsafeMutableRawPointer) -> Int32](./bnnsfilterapply%28_,_,_%29.md)
  Applies a filter to an input, writing the result to a specified output.
- [func BNNSFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int) -> Int32](./bnnsfilterapplybatch%28_,_,_,_,_,_%29.md)
  Applies a filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFilterApplyTwoInput(BNNSFilter?, UnsafeRawPointer, UnsafeRawPointer, UnsafeMutableRawPointer) -> Int32](./bnnsfilterapplytwoinput%28_,_,_,_%29.md)
  Applies a filter to a pair of inputs, writing the result to a specified output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterapplytwoinputbatch(_:_:_:_:_:_:_:_:))*