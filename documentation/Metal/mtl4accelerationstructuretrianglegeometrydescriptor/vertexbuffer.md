# vertexBuffer

**Framework**: Metal  
**Kind**: property

Associates a vertex buffer containing triangle vertices.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var vertexBuffer: MTL4BufferRange { get set }
```

#### Discussion

You are responsible for ensuring that the format of all vertex positions match the [`vertexFormat`](mtl4accelerationstructuretrianglegeometrydescriptor/vertexformat.md) property, and that the buffer address for the buffer range is not zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/vertexbuffer)*