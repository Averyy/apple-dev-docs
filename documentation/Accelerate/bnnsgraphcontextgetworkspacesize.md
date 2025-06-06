# BNNSGraphContextGetWorkspaceSize(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns the minimum size, in bytes, of the workspace that graph context execution requires.

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
func BNNSGraphContextGetWorkspaceSize(_ context: bnns_graph_context_t, _ function: UnsafePointer<CChar>?) -> Int
```

#### Return Value

The minimum size, in bytes, for the workspace, or `SIZE_T_MAX` if the query fails.

#### Discussion

Call this function to obtain the minimum size of the workspace that the BNNSGraphContextExecute function requires. If you call either [`BNNSGraphContextSetBatchSize(_:_:_:)`](bnnsgraphcontextsetbatchsize(_:_:_:).md) or [`BNNSGraphContextSetDynamicShapes(_:_:_:_:)`](bnnsgraphcontextsetdynamicshapes(_:_:_:_:).md), call this function afterwards to obtain the new workspace size.

Note that the workspace size may not be proportional with the dynamic size. That is, smaller input and output tensors may require a larger workspace.

## Parameters

- `context`: The graph context.
- `function`: The function. Specify as   if the graph only contains one function.

## See Also

- [func BNNSGraphContextSetArgumentType(bnns_graph_context_t, BNNSGraphArgumentType) -> Int32](bnnsgraphcontextsetargumenttype(_:_:).md)
  Specifies the argument type for a graph context.
- [struct BNNSGraphArgumentType](bnnsgraphargumenttype.md)
  Constants that specify the argument type for a graph context.
- [func BNNSGraphContextSetDynamicShapes(bnns_graph_context_t, UnsafePointer<CChar>?, Int, UnsafeMutablePointer<bnns_graph_shape_t>) -> Int32](bnnsgraphcontextsetdynamicshapes(_:_:_:_:).md)
  Specifies the dynamic shapes for a graph and, if possible, infers, the output shapes.
- [struct bnns_graph_shape_t](bnns_graph_shape_t.md)
  The specification of the shape of an argument.
- [func BNNSGraphContextSetBatchSize(bnns_graph_context_t, UnsafePointer<CChar>?, UInt64) -> Int32](bnnsgraphcontextsetbatchsize(_:_:_:).md)
  Sets the batch size for a graph.
- [func BNNSGraphContextEnableNanAndInfChecks(bnns_graph_context_t, Bool)](bnnsgraphcontextenablenanandinfchecks(_:_:).md)
  Specifies that the context checks intermediate tensors for NaNs and infinities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphcontextgetworkspacesize(_:_:))*