# BNNSFilterApply(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Applies a filter to an input, writing the result to a specified output.

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
func BNNSFilterApply(_ filter: BNNSFilter?, _ in: UnsafeRawPointer, _ out: UnsafeMutableRawPointer) -> Int32
```

```c
int BNNSFilterApply(BNNSFilter filter, const void *in, void *out);
```

#### Return Value

Returns 0 on success, -1 on failure.

## Parameters

- `filter`: The filter to apply.
- `in`: Pointer to the input data.
- `out`: Pointer to the output data.

## See Also

### Forward Propagation Functions
- [func BNNSFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int) -> Int32](./bnnsfilterapplybatch%28_,_,_,_,_,_%29.md)
  Applies a filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFilterApplyTwoInput(BNNSFilter?, UnsafeRawPointer, UnsafeRawPointer, UnsafeMutableRawPointer) -> Int32](./bnnsfilterapplytwoinput%28_,_,_,_%29.md)
  Applies a filter to a pair of inputs, writing the result to a specified output.
- [func BNNSFilterApplyTwoInputBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int) -> Int32](./bnnsfilterapplytwoinputbatch%28_,_,_,_,_,_,_,_%29.md)
  Applies a filter to a set of input object pairs, writing the result to a set of output objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterapply(_:_:_:))*