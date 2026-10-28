# BNNSFilterApplyBatch(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Applies a filter to a set of input objects, writing the result to a set of output objects.

**Availability**:
- iOS 10.0+ - Deprecated in 18.0
- iPadOS 10.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.12+ - Deprecated in 15.0
- tvOS 10.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 3.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
func BNNSFilterApplyBatch(_ filter: BNNSFilter?, _ batch_size: Int, _ in: UnsafeRawPointer, _ in_stride: Int, _ out: UnsafeMutableRawPointer, _ out_stride: Int) -> Int32
```

```c
int BNNSFilterApplyBatch(BNNSFilter filter, size_t batch_size, const void *in, size_t in_stride, void *out, size_t out_stride);
```

## Return Value

## Parameters

- `filter`: The filter to apply.
- `batch_size`: The number of input-output pairs.
- `in`: Pointer to input object.
- `in_stride`: Increment, in values, between input objects.
- `out`: Pointer to output object.
- `out_stride`: Increment, in values, between output objects.

## See Also

### Forward Propagation Functions
- [func BNNSFilterApply(BNNSFilter?, UnsafeRawPointer, UnsafeMutableRawPointer) -> Int32](./bnnsfilterapply%28_,_,_%29.md)
  Applies a filter to an input, writing the result to a specified output.
- [func BNNSFilterApplyTwoInput(BNNSFilter?, UnsafeRawPointer, UnsafeRawPointer, UnsafeMutableRawPointer) -> Int32](./bnnsfilterapplytwoinput%28_,_,_,_%29.md)
  Applies a filter to a pair of inputs, writing the result to a specified output.
- [func BNNSFilterApplyTwoInputBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int) -> Int32](./bnnsfilterapplytwoinputbatch%28_,_,_,_,_,_,_,_%29.md)
  Applies a filter to a set of input object pairs, writing the result to a set of output objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterapplybatch(_:_:_:_:_:_:))*