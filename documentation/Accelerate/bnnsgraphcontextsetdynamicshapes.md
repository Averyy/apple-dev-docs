# BNNSGraphContextSetDynamicShapes(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Specifies the dynamic shapes for a graph and, if possible, infers, the output shapes.

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
func BNNSGraphContextSetDynamicShapes(_ context: bnns_graph_context_t, _ function: UnsafePointer<CChar>?, _ shapes_count: Int, _ shapes: UnsafeMutablePointer<bnns_graph_shape_t>) -> Int32
```

#### Return Value

- `0` on success if all tensor shapes were exactly determined. That is, the workspace size is exact.

#### Discussion

- `1` on success if one or more tensor shapes are merely bounds, but no tensor is unbounded. That is, the workspace size is bounded.
- `2` on success if one or more tensor shapes are unbounded and BNNS will allocate workspace memory during execution.
- A negative value indicates an error.

#### Discussion

Don’t call this function while existing calls to [`BNNSGraphContextExecute(_:_:_:_:_:_:)`](bnnsgraphcontextexecute(_:_:_:_:_:_:).md) are running.

For example, the following code sets the dynamic shapes for an example graph context, specifies the output shape, and updates the context’s required workspace size.

```swift
var inputShape: [UInt64] = [1024, 1, 1]
let rank = inputShape.count
var outputShape = [UInt64](repeating: 0, count: rank)

let result = outputShape.withUnsafeMutableBufferPointer { output in
    inputShape.withUnsafeMutableBufferPointer { input in
        
        var shapes = [
            bnns_graph_shape_t(rank: rank, shape: output.baseAddress!),
            bnns_graph_shape_t(rank:rank, shape: input.baseAddress!)
        ]
        
        return BNNSGraphContextSetDynamicShapes(context, nil,
                                                shapes.count, &shapes)
    }
}
    
// Prints "[1024, 1, 1]".
print(outputShape)
```

On return, the output shape contains the correct size for the input shape, and a subsequent call to [`BNNSGraphContextGetWorkspaceSize(_:_:)`](bnnsgraphcontextgetworkspacesize(_:_:).md) returns the correct workspace size.

## Parameters

- `context`: The graph context.
- `function`: The function. Specify as   if the graph only contains one function.
- `shapes_count`: The number of elements in the   array.
- `shapes`: On output, the function sets output shapes with a nonzero rank to the upper bounds of the expected output shape. If the function can’t deduce the output shape because it depends on the input data values, the value of   is zero.

## See Also

- [func BNNSGraphContextSetStreamingAdvanceCount(bnns_graph_context_t, Int) -> Int32](bnnsgraphcontextsetstreamingadvancecount(_:_:).md)
  Sets the streaming advancement amount for cases with dynamically shaped inputs.
- [func BNNSGraphContextSetArgumentType(bnns_graph_context_t, BNNSGraphArgumentType) -> Int32](bnnsgraphcontextsetargumenttype(_:_:).md)
  Specifies the argument type for a graph context.
- [struct BNNSGraphArgumentType](bnnsgraphargumenttype.md)
  Constants that specify the argument type for a graph context.
- [struct bnns_graph_shape_t](bnns_graph_shape_t.md)
  The specification of the shape of an argument.
- [func BNNSGraphContextSetBatchSize(bnns_graph_context_t, UnsafePointer<CChar>?, UInt64) -> Int32](bnnsgraphcontextsetbatchsize(_:_:_:).md)
  Sets the batch size for a graph.
- [func BNNSGraphContextEnableNanAndInfChecks(bnns_graph_context_t, Bool)](bnnsgraphcontextenablenanandinfchecks(_:_:).md)
  Specifies that the context checks intermediate tensors for NaNs and infinities.
- [func BNNSGraphContextGetWorkspaceSize(bnns_graph_context_t, UnsafePointer<CChar>?) -> Int](bnnsgraphcontextgetworkspacesize(_:_:).md)
  Returns the minimum size, in bytes, of the workspace that graph context execution requires.
- [func BNNSGraphContextSetStreamingAdvanceCount(bnns_graph_context_t, Int) -> Int32](bnnsgraphcontextsetstreamingadvancecount(_:_:).md)
  Sets the streaming advancement amount for cases with dynamically shaped inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphcontextsetdynamicshapes(_:_:_:_:))*