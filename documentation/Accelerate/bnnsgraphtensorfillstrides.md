# BNNSGraphTensorFillStrides(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Sets the stride of the specifed tensor for compatibility with the given model’s input or output argument based on its current shape.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func BNNSGraphTensorFillStrides(_ graph: bnns_graph_t, _ function: UnsafePointer<CChar>?, _ argument: UnsafePointer<CChar>, _ tensor: UnsafeMutablePointer<BNNSTensor>) -> Int32
```

#### Return Value

`0` on success, nonzero on failure.

#### Discussion

Call this function to fill the strides of a buffer according to the specification of the compiled graph’s model.

This function requires that you specify the tensor’s sizes. That is, they aren’t less than zero.

## Parameters

- `graph`: The compiled graph object.
- `function`: The function. Specify as   if the graph only contains one function.
- `argument`: The name of the input or output argument.
- `tensor`: The tensor. On output, the first   elements contain the strides that BNNS requires.

## See Also

- [struct BNNSTensor](bnnstensor.md)
  A structure that describes the shape, stride, data type, and, optionally, the memory location of an n-dimensional array.
- [func BNNSTensorGetAllocationSize(UnsafePointer<BNNSTensor>) -> Int](bnnstensorgetallocationsize(_:).md)
  Returns the minimum allocation size, in bytes, of the specified tensor.
- [func BNNSGraphContextGetTensor(bnns_graph_context_t, UnsafePointer<CChar>?, UnsafePointer<CChar>, Bool, UnsafeMutablePointer<BNNSTensor>) -> Int32](bnnsgraphcontextgettensor(_:_:_:_:_:).md)
  Sets the properties of a tensor for the specified function argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphtensorfillstrides(_:_:_:_:))*