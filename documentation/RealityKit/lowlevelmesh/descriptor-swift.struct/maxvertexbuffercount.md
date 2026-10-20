# maxVertexBufferCount

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property

The maximum number of separate buffers the system supports.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
static let maxVertexBufferCount: Int
```

#### Discussion

For optimal performance, most applications use one buffer.

## See Also

### Defining the descriptor’s limits
- [var vertexCapacity: Int](./vertexcapacity.md)
  The number of vertices to allocate space for.
- [var indexCapacity: Int](./indexcapacity.md)
  The number of indices to allocate space for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/descriptor-swift.struct/maxvertexbuffercount)*