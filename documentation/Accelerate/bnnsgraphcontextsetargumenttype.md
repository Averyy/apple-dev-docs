# BNNSGraphContextSetArgumentType(_:_:)

**Framework**: Accelerate  
**Kind**: func

Specifies the argument type for a graph context.

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
func BNNSGraphContextSetArgumentType(_ context: bnns_graph_context_t, _ argument_type: BNNSGraphArgumentType) -> Int32
```

#### Return Value

`0` on success, nonzero on failure.

#### Discussion

Some arguments require dynamic strides. In this case, set the graph context’s argument type to [`BNNSGraphArgumentTypeTensor`](bnnsgraphargumenttypetensor.md) and pass the arguments to [`BNNSGraphContextExecute(_:_:_:_:_:_:)`](bnnsgraphcontextexecute(_:_:_:_:_:_:).md) as [`BNNSTensor`](bnnstensor.md) structures.

The default argument type for a graph context is [`BNNSGraphArgumentTypePointer`](bnnsgraphargumenttypepointer.md).

## Parameters

- `context`: The graph context.
- `argument_type`: A constant that specifies the argument type.

## See Also

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
- [func BNNSGraphContextGetWorkspaceSize(bnns_graph_context_t, UnsafePointer<CChar>?) -> Int](bnnsgraphcontextgetworkspacesize(_:_:).md)
  Returns the minimum size, in bytes, of the workspace that graph context execution requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphcontextsetargumenttype(_:_:))*