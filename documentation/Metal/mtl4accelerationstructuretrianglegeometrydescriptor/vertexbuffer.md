# vertexBuffer

**Framework**: Metal  
**Kind**: property

Associates a vertex buffer containing triangle vertices.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var vertexBuffer: MTL4BufferRange { get set }
```

#### Discussion

You are responsible for ensuring that the format of all vertex positions match the [`vertexFormat`](mtl4accelerationstructuretrianglegeometrydescriptor/vertexformat.md) property, and that the buffer address for the buffer range is not zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/vertexbuffer)*