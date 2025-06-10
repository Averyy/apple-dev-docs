# BNNSFilterApplyTwoInputBatch(_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a filter to a set of input object pairs, writing the result to a set of output objects.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func BNNSFilterApplyTwoInputBatch(_ filter: BNNSFilter?, _ batch_size: Int, _ inA: UnsafeRawPointer, _ inA_stride: Int, _ inB: UnsafeRawPointer, _ inB_stride: Int, _ out: UnsafeMutableRawPointer, _ out_stride: Int) -> Int32
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

- [func BNNSFilterApply(BNNSFilter?, UnsafeRawPointer, UnsafeMutableRawPointer) -> Int32](bnnsfilterapply(_:_:_:).md)
  Applies a filter to an input, writing the result to a specified output.
- [func BNNSFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int) -> Int32](bnnsfilterapplybatch(_:_:_:_:_:_:).md)
  Applies a filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFilterApplyTwoInput(BNNSFilter?, UnsafeRawPointer, UnsafeRawPointer, UnsafeMutableRawPointer) -> Int32](bnnsfilterapplytwoinput(_:_:_:_:).md)
  Applies a filter to a pair of inputs, writing the result to a specified output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterapplytwoinputbatch(_:_:_:_:_:_:_:_:))*