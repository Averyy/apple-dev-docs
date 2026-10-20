# BNNSGraphContextDestroy(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

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

```c
void BNNSGraphContextDestroy(bnns_graph_context_t context);
```

## Parameters

- `context`: The graph context.

## See Also

### Creating and destroying a context
- [struct bnns_graph_context_t](./bnns_graph_context_t.md)
  An object that wraps a compiled graph object.
- [func BNNSGraphContextMake(bnns_graph_t) -> bnns_graph_context_t](./bnnsgraphcontextmake%28_%29.md)
  Returns an allocated and initialized graph context from the specified graph.
- [func BNNSGraphContextMakeStreaming(bnns_graph_t, UnsafePointer<CChar>?, Int, UnsafePointer<BNNSTensor>?) -> bnns_graph_context_t](./bnnsgraphcontextmakestreaming%28_,_,_,_%29.md)
  Returns an allocated and initialized graph context with streaming support from the specified graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphcontextdestroy(_:))*