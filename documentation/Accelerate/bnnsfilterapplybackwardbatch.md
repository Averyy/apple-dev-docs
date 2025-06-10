# BNNSFilterApplyBackwardBatch(_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a filter backward to generate input delta, weights delta and bias delta.

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
func BNNSFilterApplyBackwardBatch(_ filter: BNNSFilter?, _ batch_size: Int, _ in: UnsafeRawPointer?, _ in_stride: Int, _ in_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>?, _ in_delta_stride: Int, _ out: UnsafeRawPointer?, _ out_stride: Int, _ out_delta: UnsafePointer<BNNSNDArrayDescriptor>, _ out_delta_stride: Int, _ weights_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>?, _ bias_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>?) -> Int32
```

## Parameters

- `filter`: The filter to apply.
- `batch_size`: The number of input-output pairs.
- `in`: Pointer to input object.
- `in_stride`: Increment, in values, between input objects.
- `in_delta`: The descriptor of the input delta.
- `in_delta_stride`: Increment, in values, between input delta objects.
- `out`: Pointer to output object.
- `out_stride`: Increment, in values, between output objects.
- `out_delta`: The descriptor of the output delta.
- `out_delta_stride`: Increment, in values, between output delta objects.
- `weights_delta`: The descriptor of the weights delta.
- `bias_delta`: The descriptor of the bias delta.

## See Also

- [func BNNSFilterApplyBackwardTwoInputBatch(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<BNNSNDArrayDescriptor>?) -> Int32](bnnsfilterapplybackwardtwoinputbatch(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a filter backward to generate input deltas, weights delta and bias delta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:_:_:))*