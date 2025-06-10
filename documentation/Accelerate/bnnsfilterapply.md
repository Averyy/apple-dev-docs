# BNNSFilterApply(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a filter to an input, writing the result to a specified output.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func BNNSFilterApply(_ filter: BNNSFilter?, _ in: UnsafeRawPointer, _ out: UnsafeMutableRawPointer) -> Int32
```

#### Return Value

Returns 0 on success, -1 on failure.

## Parameters

- `filter`: The filter to apply.
- `in`: Pointer to the input data.
- `out`: Pointer to the output data.

## See Also

- [func BNNSFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int) -> Int32](bnnsfilterapplybatch(_:_:_:_:_:_:).md)
  Applies a filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFilterApplyTwoInput(BNNSFilter?, UnsafeRawPointer, UnsafeRawPointer, UnsafeMutableRawPointer) -> Int32](bnnsfilterapplytwoinput(_:_:_:_:).md)
  Applies a filter to a pair of inputs, writing the result to a specified output.
- [func BNNSFilterApplyTwoInputBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int) -> Int32](bnnsfilterapplytwoinputbatch(_:_:_:_:_:_:_:_:).md)
  Applies a filter to a set of input object pairs, writing the result to a set of output objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterapply(_:_:_:))*