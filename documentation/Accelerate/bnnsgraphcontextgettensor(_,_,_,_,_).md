# BNNSGraphContextGetTensor(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Sets the properties of a tensor for the specified function argument.

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
func BNNSGraphContextGetTensor(_ context: bnns_graph_context_t, _ function: UnsafePointer<CChar>?, _ argument: UnsafePointer<CChar>, _ fill_known_dynamic_shapes: Bool, _ tensor: UnsafeMutablePointer<BNNSTensor>) -> Int32
```

```c
int BNNSGraphContextGetTensor(bnns_graph_context_t context, const char *function, const char *argument, bool fill_known_dynamic_shapes, BNNSTensor *tensor);
```

#### Return Value

`0` on success, nonzero on failure.

## Parameters

- `context`: The graph context.
- `function`: The function. Specify as `nil` if the graph only contains one function.
- `argument`: The name of the input or output argument.
- `fill_known_dynamic_shapes`: A Boolean value that specifies whether the function should replace any dynamic shapes for the next execution of the context. BNNS derives these shapes either from the default shapes in the source model, or from a preceding calls to [`BNNSGraphContextSetDynamicShapes(_:_:_:_:)`](./bnnsgraphcontextsetdynamicshapes%28_,_,_,_%29.md) or [`BNNSGraphContextSetBatchSize(_:_:_:)`](./bnnsgraphcontextsetbatchsize%28_,_,_%29.md). If BNNS is unable to derive the shapes, the function sets the dimensions to `-1`.
- `tensor`: The tensor. On output, all fields apart from [`data`](./bnnstensor/data.md) contain the properties for the specified function argument.

## See Also

### Specifying and querying a tensor’s properties
- [struct BNNSTensor](./bnnstensor.md)
  A structure that describes the shape, stride, data type, and, optionally, the memory location of an n-dimensional array.
- [func BNNSTensorGetAllocationSize(UnsafePointer<BNNSTensor>) -> Int](./bnnstensorgetallocationsize%28_%29.md)
  Returns the minimum allocation size, in bytes, of the specified tensor.
- [func BNNSGraphTensorFillStrides(bnns_graph_t, UnsafePointer<CChar>?, UnsafePointer<CChar>, UnsafeMutablePointer<BNNSTensor>) -> Int32](./bnnsgraphtensorfillstrides%28_,_,_,_%29.md)
  Sets the stride of the specifed tensor for compatibility with the given model’s input or output argument based on its current shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphcontextgettensor(_:_:_:_:_:))*