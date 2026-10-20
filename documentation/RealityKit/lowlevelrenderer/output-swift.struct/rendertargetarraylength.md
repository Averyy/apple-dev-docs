# renderTargetArrayLength

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The number of active array slices in the render target textures.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var renderTargetArrayLength: Int { get set }
```

#### Discussion

Corresponds to `MTLRenderPassDescriptor.renderTargetArrayLength`. Set this to the size of the texture array when using multi-viewport rendering into texture slices.

## See Also

### Configuring render targets
- [var renderTargetWidth: Int](./rendertargetwidth.md)
  The width of the render target, in pixels.
- [var renderTargetHeight: Int](./rendertargetheight.md)
  The height of the render target, in pixels.
- [var threadgroupMemoryLength: Int](./threadgroupmemorylength.md)
  The per-tile size, in bytes, of the persistent threadgroup memory allocation, used when rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/output-swift.struct/rendertargetarraylength)*