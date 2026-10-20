# BNNSGraphContextMake(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns an allocated and initialized graph context from the specified graph.

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
func BNNSGraphContextMake(_ graph: bnns_graph_t) -> bnns_graph_context_t
```

```c
bnns_graph_context_t BNNSGraphContextMake(const bnns_graph_t graph);
```

#### Return Value

A compiled graph context object. If the operation fails, the graph object’s [`data`](./bnns_graph_context_t/data.md) property is `nil`.

#### Discussion

To prevent memory leaks, call [`BNNSGraphContextDestroy(_:)`](./bnnsgraphcontextdestroy%28_%29.md) when you’re finished using the graph context.

## Parameters

- `graph`: The compiled graph object.

## See Also

### Creating and destroying a context
- [struct bnns_graph_context_t](./bnns_graph_context_t.md)
  An object that wraps a compiled graph object.
- [func BNNSGraphContextMakeStreaming(bnns_graph_t, UnsafePointer<CChar>?, Int, UnsafePointer<BNNSTensor>?) -> bnns_graph_context_t](./bnnsgraphcontextmakestreaming%28_,_,_,_%29.md)
  Returns an allocated and initialized graph context with streaming support from the specified graph.
- [func BNNSGraphContextDestroy(bnns_graph_context_t)](./bnnsgraphcontextdestroy%28_%29.md)
  Destroys the specified graph context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphcontextmake(_:))*