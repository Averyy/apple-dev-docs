# BNNSGraphContextSetArgumentType(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

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

```c
int BNNSGraphContextSetArgumentType(bnns_graph_context_t context, BNNSGraphArgumentType argument_type);
```

#### Return Value

`0` on success, nonzero on failure.

#### Discussion

Some arguments require dynamic strides. In this case, set the graph context’s argument type to [`BNNSGraphArgumentTypeTensor`](./bnnsgraphargumenttypetensor.md) and pass the arguments to [`BNNSGraphContextExecute(_:_:_:_:_:_:)`](./bnnsgraphcontextexecute%28_,_,_,_,_,_%29.md) as [`BNNSTensor`](./bnnstensor.md) structures.

The default argument type for a graph context is [`BNNSGraphArgumentTypePointer`](./bnnsgraphargumenttypepointer.md).

## Parameters

- `context`: The graph context.
- `argument_type`: A constant that specifies the argument type.

## See Also

### Specifying and querying a context’s properties
- [func BNNSGraphContextSetStreamingAdvanceCount(bnns_graph_context_t, Int) -> Int32](./bnnsgraphcontextsetstreamingadvancecount%28_,_%29.md)
  Sets the streaming advancement amount for cases with dynamically shaped inputs.
- [struct BNNSGraphArgumentType](./bnnsgraphargumenttype.md)
  Constants that specify the argument type for a graph context.
- [func BNNSGraphContextSetDynamicShapes(bnns_graph_context_t, UnsafePointer<CChar>?, Int, UnsafeMutablePointer<bnns_graph_shape_t>) -> Int32](./bnnsgraphcontextsetdynamicshapes%28_,_,_,_%29.md)
  Specifies the dynamic shapes for a graph and, if possible, infers, the output shapes.
- [struct bnns_graph_shape_t](./bnns_graph_shape_t.md)
  The specification of the shape of an argument.
- [func BNNSGraphContextSetBatchSize(bnns_graph_context_t, UnsafePointer<CChar>?, UInt64) -> Int32](./bnnsgraphcontextsetbatchsize%28_,_,_%29.md)
  Sets the batch size for a graph.
- [func BNNSGraphContextEnableNanAndInfChecks(bnns_graph_context_t, Bool)](./bnnsgraphcontextenablenanandinfchecks%28_,_%29.md)
  Specifies that the context checks intermediate tensors for NaNs and infinities.
- [func BNNSGraphContextGetWorkspaceSize(bnns_graph_context_t, UnsafePointer<CChar>?) -> Int](./bnnsgraphcontextgetworkspacesize%28_,_%29.md)
  Returns the minimum size, in bytes, of the workspace that graph context execution requires.
- [func BNNSGraphContextSetStreamingAdvanceCount(bnns_graph_context_t, Int) -> Int32](./bnnsgraphcontextsetstreamingadvancecount%28_,_%29.md)
  Sets the streaming advancement amount for cases with dynamically shaped inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphcontextsetargumenttype(_:_:))*