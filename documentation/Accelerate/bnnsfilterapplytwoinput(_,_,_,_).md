# BNNSFilterApplyTwoInput(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Applies a filter to a pair of inputs, writing the result to a specified output.

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
func BNNSFilterApplyTwoInput(_ filter: BNNSFilter?, _ inA: UnsafeRawPointer, _ inB: UnsafeRawPointer, _ out: UnsafeMutableRawPointer) -> Int32
```

```c
int BNNSFilterApplyTwoInput(BNNSFilter filter, const void *inA, const void *inB, void *out);
```

## Parameters

- `filter`: The filter to apply.
- `inA`: Pointer to the first input data.
- `inB`: Pointer to the second input data.
- `out`: Pointer to the output data.

## See Also

### Forward Propagation Functions
- [func BNNSFilterApply(BNNSFilter?, UnsafeRawPointer, UnsafeMutableRawPointer) -> Int32](./bnnsfilterapply%28_,_,_%29.md)
  Applies a filter to an input, writing the result to a specified output.
- [func BNNSFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int) -> Int32](./bnnsfilterapplybatch%28_,_,_,_,_,_%29.md)
  Applies a filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFilterApplyTwoInputBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int) -> Int32](./bnnsfilterapplytwoinputbatch%28_,_,_,_,_,_,_,_%29.md)
  Applies a filter to a set of input object pairs, writing the result to a set of output objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterapplytwoinput(_:_:_:_:))*