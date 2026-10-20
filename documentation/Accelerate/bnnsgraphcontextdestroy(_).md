# BNNSGraphContextDestroy(_:)

**Framework**: Accelerate  
**Kind**: func

Destroys the specified graph context.

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
func BNNSGraphContextDestroy(_ context: bnns_graph_context_t)
```

## Parameters

- `context`: The graph context.

## See Also

- [struct bnns_graph_context_t](bnns_graph_context_t.md)
  An object that wraps a compiled graph object.
- [func BNNSGraphContextMake(bnns_graph_t) -> bnns_graph_context_t](bnnsgraphcontextmake(_:).md)
  Returns an allocated and initialized graph context from the specified graph.
- [func BNNSGraphContextMakeStreaming(bnns_graph_t, UnsafePointer<CChar>?, Int, UnsafePointer<BNNSTensor>?) -> bnns_graph_context_t](bnnsgraphcontextmakestreaming(_:_:_:_:).md)
  Returns an allocated and initialized graph context with streaming support from the specified graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphcontextdestroy(_:))*