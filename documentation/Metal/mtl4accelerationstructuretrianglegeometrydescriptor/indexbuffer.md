# indexBuffer

**Framework**: Metal  
**Kind**: property

Sets an optional index buffer containing references to vertices in the `vertexBuffer`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var indexBuffer: MTL4BufferRange { get set }
```

#### Discussion

You can set this property to `0`, the default, to avoid specifying an index buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/indexbuffer)*