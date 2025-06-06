# bnns_graph_free_all_fn_t

**Framework**: Accelerate  
**Kind**: typealias

The workspace and output deallocation function.

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
typealias bnns_graph_free_all_fn_t = (UnsafeMutableRawPointer?, Int) -> Void
```

#### Return Value

`0` on success, nonzero on failure.

#### Discussion

BNNS calls this function on the destruction of a graph context and should free all memory associated to the `user_memory_context`.

If you’ve supplied the same `user_memory_context` to both [`BNNSGraphContextSetWorkspaceAllocationCallback(_:_:_:_:_:)`](bnnsgraphcontextsetworkspaceallocationcallback(_:_:_:_:_:).md) and [`BNNSGraphContextSetOutputAllocationCallback(_:_:_:_:_:)`](bnnsgraphcontextsetoutputallocationcallback(_:_:_:_:_:).md), BNNS calls this function once, during [`BNNSGraphContextDestroy(_:)`](bnnsgraphcontextdestroy(_:).md).

## See Also

- [func BNNSGraphContextSetWorkspaceAllocationCallback(bnns_graph_context_t, bnns_graph_realloc_fn_t?, bnns_graph_free_all_fn_t?, Int, UnsafeMutableRawPointer?) -> Int32](bnnsgraphcontextsetworkspaceallocationcallback(_:_:_:_:_:).md)
  Sets the allocation and deallocation callbacks for internal workspace.
- [func BNNSGraphContextSetOutputAllocationCallback(bnns_graph_context_t, bnns_graph_realloc_fn_t?, bnns_graph_free_all_fn_t?, Int, UnsafeMutableRawPointer?) -> Int32](bnnsgraphcontextsetoutputallocationcallback(_:_:_:_:_:).md)
  Sets the allocation and deallocation callbacks for function outputs.
- [typealias bnns_graph_realloc_fn_t](bnns_graph_realloc_fn_t.md)
  The workspace and output allocation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns_graph_free_all_fn_t)*