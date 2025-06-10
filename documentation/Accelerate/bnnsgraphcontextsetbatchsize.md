# BNNSGraphContextSetBatchSize(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Sets the batch size for a graph.

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
func BNNSGraphContextSetBatchSize(_ context: bnns_graph_context_t, _ function: UnsafePointer<CChar>?, _ batch_size: UInt64) -> Int32
```

#### Return Value

`0` on success, nonzero on failure.

#### Discussion

This function provides a special case of [`BNNSGraphContextSetDynamicShapes(_:_:_:_:)`](bnnsgraphcontextsetdynamicshapes(_:_:_:_:).md) where the only dynamic size is the first index of the tensors and that size is equal for all tensors. This function provides a simpler API because you only need to pass the common first dimension as the `batch_size` parameter.

If your graph contains other dynamic strides, use [`BNNSGraphContextSetDynamicShapes(_:_:_:_:)`](bnnsgraphcontextsetdynamicshapes(_:_:_:_:).md) instead. This function doesn’t set dynamic strides.

Don’t call this function while existing calls to [`BNNSGraphContextExecute(_:_:_:_:_:_:)`](bnnsgraphcontextexecute(_:_:_:_:_:_:).md) are running.

## Parameters

- `context`: The graph context.
- `function`: The function. Specify as   if the graph only contains one function.
- `batch_size`: The batch size.

## See Also

- [func BNNSGraphContextSetStreamingAdvanceCount(bnns_graph_context_t, Int) -> Int32](bnnsgraphcontextsetstreamingadvancecount(_:_:).md)
  Sets the streaming advancement amount for cases with dynamically shaped inputs.
- [func BNNSGraphContextSetArgumentType(bnns_graph_context_t, BNNSGraphArgumentType) -> Int32](bnnsgraphcontextsetargumenttype(_:_:).md)
  Specifies the argument type for a graph context.
- [struct BNNSGraphArgumentType](bnnsgraphargumenttype.md)
  Constants that specify the argument type for a graph context.
- [func BNNSGraphContextSetDynamicShapes(bnns_graph_context_t, UnsafePointer<CChar>?, Int, UnsafeMutablePointer<bnns_graph_shape_t>) -> Int32](bnnsgraphcontextsetdynamicshapes(_:_:_:_:).md)
  Specifies the dynamic shapes for a graph and, if possible, infers, the output shapes.
- [struct bnns_graph_shape_t](bnns_graph_shape_t.md)
  The specification of the shape of an argument.
- [func BNNSGraphContextEnableNanAndInfChecks(bnns_graph_context_t, Bool)](bnnsgraphcontextenablenanandinfchecks(_:_:).md)
  Specifies that the context checks intermediate tensors for NaNs and infinities.
- [func BNNSGraphContextGetWorkspaceSize(bnns_graph_context_t, UnsafePointer<CChar>?) -> Int](bnnsgraphcontextgetworkspacesize(_:_:).md)
  Returns the minimum size, in bytes, of the workspace that graph context execution requires.
- [func BNNSGraphContextSetStreamingAdvanceCount(bnns_graph_context_t, Int) -> Int32](bnnsgraphcontextsetstreamingadvancecount(_:_:).md)
  Sets the streaming advancement amount for cases with dynamically shaped inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphcontextsetbatchsize(_:_:_:))*