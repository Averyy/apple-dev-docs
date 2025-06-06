# bnns_graph_t

**Framework**: Accelerate  
**Kind**: struct

The compiled graph object.

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
struct bnns_graph_t
```

## Topics

### Initializing a graph
- [init()](bnns_graph_t/init.md)
  Creates an empty graph structure.
- [init(data: UnsafeMutableRawPointer?, size: Int)](bnns_graph_t/init(data:size:).md)
  Creates a graph structure from the specified opaque graph object.
### Instance properties
- [var data: UnsafeMutableRawPointer?](bnns_graph_t/data.md)
  A pointer to opaque graph object.
- [var size: Int](bnns_graph_t/size.md)
  The size, in bytes, of the opaque graph object.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func BNNSGraphCompileFromFile(UnsafePointer<CChar>, UnsafePointer<CChar>?, bnns_graph_compile_options_t) -> bnns_graph_t](bnnsgraphcompilefromfile(_:_:_:).md)
  Compiles a source mlmodelc file to a graph object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns_graph_t)*