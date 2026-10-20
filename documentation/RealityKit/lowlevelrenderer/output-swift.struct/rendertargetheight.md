# renderTargetHeight

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The height of the render target, in pixels.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var renderTargetHeight: Int { get set }
```

#### Discussion

Corresponds to `MTLRenderPassDescriptor.renderTargetHeight`.

## See Also

### Configuring render targets
- [var renderTargetWidth: Int](./rendertargetwidth.md)
  The width of the render target, in pixels.
- [var renderTargetArrayLength: Int](./rendertargetarraylength.md)
  The number of active array slices in the render target textures.
- [var threadgroupMemoryLength: Int](./threadgroupmemorylength.md)
  The per-tile size, in bytes, of the persistent threadgroup memory allocation, used when rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/output-swift.struct/rendertargetheight)*