# indexBuffer

**Framework**: Metal  
**Kind**: property

Sets an optional index buffer containing references to vertices in the `vertexBuffer`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var indexBuffer: MTL4BufferRange { get set }
```

#### Discussion

You can set this property to `0`, the default, to avoid specifying an index buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/indexbuffer)*