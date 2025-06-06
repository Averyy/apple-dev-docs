# bnns_graph_context_t

**Framework**: Accelerate  
**Kind**: struct

An object that wraps a compiled graph object.

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
struct bnns_graph_context_t
```

#### Overview

The [`bnns_graph_context_t`](bnns_graph_context_t.md) object wraps a [`bnns_graph_t`](bnns_graph_t.md) instance and adds mutable data storage. BNNS requires mutability to support dynamic shapes and other execution objects.

You must ensure that the underlying [`bnns_graph_t`](bnns_graph_t.md) instance remains valid throughout the lifetime of the context.

## Topics

### Initializing a context
- [init()](bnns_graph_context_t/init.md)
  Creates an empty graph context structure.
- [init(data: UnsafeMutableRawPointer?, size: Int)](bnns_graph_context_t/init(data:size:).md)
  Creates a graph context structure from the specified opaque graph context object.
### Specifying a context’s properties
- [var data: UnsafeMutableRawPointer?](bnns_graph_context_t/data.md)
  A pointer to the opaque graph context object.
- [var size: Int](bnns_graph_context_t/size.md)
  The size, in bytes, of the opaque graph context object.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func BNNSGraphContextMake(bnns_graph_t) -> bnns_graph_context_t](bnnsgraphcontextmake(_:).md)
  Returns an allocated and initialized graph context from the specified graph.
- [func BNNSGraphContextMakeStreaming(bnns_graph_t, UnsafePointer<CChar>?, Int, UnsafePointer<BNNSTensor>?) -> bnns_graph_context_t](bnnsgraphcontextmakestreaming(_:_:_:_:).md)
  Returns an allocated and initialized graph context with streaming support from the specified graph.
- [func BNNSGraphContextDestroy(bnns_graph_context_t)](bnnsgraphcontextdestroy(_:).md)
  Destroys the specified graph context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns_graph_context_t)*