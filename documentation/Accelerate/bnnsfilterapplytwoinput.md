# BNNSFilterApplyTwoInput(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a filter to a pair of inputs, writing the result to a specified output.

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
func BNNSFilterApplyTwoInput(_ filter: BNNSFilter?, _ inA: UnsafeRawPointer, _ inB: UnsafeRawPointer, _ out: UnsafeMutableRawPointer) -> Int32
```

## Parameters

- `filter`: The filter to apply.
- `inA`: Pointer to the first input data.
- `inB`: Pointer to the second input data.
- `out`: Pointer to the output data.

## See Also

- [func BNNSFilterApply(BNNSFilter?, UnsafeRawPointer, UnsafeMutableRawPointer) -> Int32](bnnsfilterapply(_:_:_:).md)
  Applies a filter to an input, writing the result to a specified output.
- [func BNNSFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int) -> Int32](bnnsfilterapplybatch(_:_:_:_:_:_:).md)
  Applies a filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFilterApplyTwoInputBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int) -> Int32](bnnsfilterapplytwoinputbatch(_:_:_:_:_:_:_:_:).md)
  Applies a filter to a set of input object pairs, writing the result to a set of output objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterapplytwoinput(_:_:_:_:))*