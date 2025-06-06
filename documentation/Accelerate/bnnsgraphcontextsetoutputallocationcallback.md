# BNNSGraphContextSetOutputAllocationCallback(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Sets the allocation and deallocation callbacks for function outputs.

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
func BNNSGraphContextSetOutputAllocationCallback(_ context: bnns_graph_context_t, _ realloc: bnns_graph_realloc_fn_t?, _ free: bnns_graph_free_all_fn_t?, _ user_memory_context_size: Int, _ user_memory_context: UnsafeMutableRawPointer?) -> Int32
```

#### Return Value

`0` on success, nonzero on failure.

#### Discussion

If BNNS can’t bound the required output size prior to execution — for example, if the tensor sizes depend on input data — it allocates outputs during execution. Use this function to override the default memory allocation mechanisms.

If you pass the same `user_memory_context` to [`BNNSGraphContextSetWorkspaceAllocationCallback(_:_:_:_:_:)`](bnnsgraphcontextsetworkspaceallocationcallback(_:_:_:_:_:).md) and [`BNNSGraphContextSetOutputAllocationCallback(_:_:_:_:_:)`](bnnsgraphcontextsetoutputallocationcallback(_:_:_:_:_:).md), BNNS only calls the `free` function once.

## Parameters

- `context`: The graph context.
- `realloc`: The memory allocation and reallocation function. If you pass   for this parameter, you must also set   for the   parameter. In this case, graph execution uses the default BNNS allocation mechanism.
- `free`: The memory allocation and reallocation function. If you pass   for this parameter, you must also set   for the   parameter. In this case, graph execution uses the default BNNS allocation mechanism.
- `user_memory_context_size`: The size, in bytes,  .
- `user_memory_context`: A pointer that that BNNS passes unmodified in all calls to   and  .

## See Also

- [func BNNSGraphContextSetWorkspaceAllocationCallback(bnns_graph_context_t, bnns_graph_realloc_fn_t?, bnns_graph_free_all_fn_t?, Int, UnsafeMutableRawPointer?) -> Int32](bnnsgraphcontextsetworkspaceallocationcallback(_:_:_:_:_:).md)
  Sets the allocation and deallocation callbacks for internal workspace.
- [typealias bnns_graph_realloc_fn_t](bnns_graph_realloc_fn_t.md)
  The workspace and output allocation function.
- [typealias bnns_graph_free_all_fn_t](bnns_graph_free_all_fn_t.md)
  The workspace and output deallocation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphcontextsetoutputallocationcallback(_:_:_:_:_:))*