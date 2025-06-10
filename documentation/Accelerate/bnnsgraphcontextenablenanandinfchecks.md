# BNNSGraphContextEnableNanAndInfChecks(_:_:)

**Framework**: Accelerate  
**Kind**: func

Specifies that the context checks intermediate tensors for NaNs and infinities.

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
func BNNSGraphContextEnableNanAndInfChecks(_ context: bnns_graph_context_t, _ enable_check_for_nans_inf: Bool)
```

#### Discussion

Don’t enable this option for production code.

## Parameters

- `context`: The graph context.
- `enable_check_for_nans_inf`: If  , specifies that the context checks intermediate tensors for NaNs and infinities.

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
- [func BNNSGraphContextSetBatchSize(bnns_graph_context_t, UnsafePointer<CChar>?, UInt64) -> Int32](bnnsgraphcontextsetbatchsize(_:_:_:).md)
  Sets the batch size for a graph.
- [func BNNSGraphContextGetWorkspaceSize(bnns_graph_context_t, UnsafePointer<CChar>?) -> Int](bnnsgraphcontextgetworkspacesize(_:_:).md)
  Returns the minimum size, in bytes, of the workspace that graph context execution requires.
- [func BNNSGraphContextSetStreamingAdvanceCount(bnns_graph_context_t, Int) -> Int32](bnnsgraphcontextsetstreamingadvancecount(_:_:).md)
  Sets the streaming advancement amount for cases with dynamically shaped inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphcontextenablenanandinfchecks(_:_:))*