# init(data:size:)

**Framework**: Accelerate  
**Kind**: init

Creates a graph context structure from the specified opaque graph context object.

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
init(data: UnsafeMutableRawPointer?, size: Int)
```

## Parameters

- `data`: A pointer to opaque graph context object.
- `size`: The size, in bytes, of the opaque graph context object.

## See Also

- [init()](bnns_graph_context_t/init.md)
  Creates an empty graph context structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns_graph_context_t/init(data:size:))*