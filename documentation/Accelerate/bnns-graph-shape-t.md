# bnns_graph_shape_t

**Framework**: Accelerate  
**Kind**: struct

The specification of the shape of an argument.

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
struct bnns_graph_shape_t
```

#### Overview

Use a [`bnns_graph_shape_t`](bnns_graph_shape_t.md) structure to pass the rank and dimensions of tensors to the [`BNNSGraphContextSetDynamicShapes(_:_:_:_:)`](bnnsgraphcontextsetdynamicshapes(_:_:_:_:).md) function.

## Topics

### Initializing a graph shape
- [init()](bnns_graph_shape_t/init.md)
  Creates an empty shape structure.
- [init(rank: Int, shape: UnsafeMutablePointer<UInt64>?)](bnns_graph_shape_t/init(rank:shape:).md)
  Creates a shape structure with the specified rank and dimensions.
### Specifying a shape’s properties
- [var rank: Int](bnns_graph_shape_t/rank.md)
  The rank of the shape.
- [var shape: UnsafeMutablePointer<UInt64>?](bnns_graph_shape_t/shape.md)
  An array of unsigned-integer elements that specify the size of the shape.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func BNNSGraphContextSetStreamingAdvanceCount(bnns_graph_context_t, Int) -> Int32](bnnsgraphcontextsetstreamingadvancecount(_:_:).md)
  Sets the streaming advancement amount for cases with dynamically shaped inputs.
- [func BNNSGraphContextSetArgumentType(bnns_graph_context_t, BNNSGraphArgumentType) -> Int32](bnnsgraphcontextsetargumenttype(_:_:).md)
  Specifies the argument type for a graph context.
- [struct BNNSGraphArgumentType](bnnsgraphargumenttype.md)
  Constants that specify the argument type for a graph context.
- [func BNNSGraphContextSetDynamicShapes(bnns_graph_context_t, UnsafePointer<CChar>?, Int, UnsafeMutablePointer<bnns_graph_shape_t>) -> Int32](bnnsgraphcontextsetdynamicshapes(_:_:_:_:).md)
  Specifies the dynamic shapes for a graph and, if possible, infers, the output shapes.
- [func BNNSGraphContextSetBatchSize(bnns_graph_context_t, UnsafePointer<CChar>?, UInt64) -> Int32](bnnsgraphcontextsetbatchsize(_:_:_:).md)
  Sets the batch size for a graph.
- [func BNNSGraphContextEnableNanAndInfChecks(bnns_graph_context_t, Bool)](bnnsgraphcontextenablenanandinfchecks(_:_:).md)
  Specifies that the context checks intermediate tensors for NaNs and infinities.
- [func BNNSGraphContextGetWorkspaceSize(bnns_graph_context_t, UnsafePointer<CChar>?) -> Int](bnnsgraphcontextgetworkspacesize(_:_:).md)
  Returns the minimum size, in bytes, of the workspace that graph context execution requires.
- [func BNNSGraphContextSetStreamingAdvanceCount(bnns_graph_context_t, Int) -> Int32](bnnsgraphcontextsetstreamingadvancecount(_:_:).md)
  Sets the streaming advancement amount for cases with dynamically shaped inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns_graph_shape_t)*