# threadgroupMemoryLength

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The per-tile size, in bytes, of the persistent threadgroup memory allocation, used when rendering.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var threadgroupMemoryLength: Int { get set }
```

## Discussion

Corresponds to `MTLRenderCommandEncoder.threadgroupMemoryLength`.

## See Also

### Configuring render targets
- [var renderTargetWidth: Int](./rendertargetwidth.md)
  The width of the render target, in pixels.
- [var renderTargetHeight: Int](./rendertargetheight.md)
  The height of the render target, in pixels.
- [var renderTargetArrayLength: Int](./rendertargetarraylength.md)
  The number of active array slices in the render target textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/output-swift.struct/threadgroupmemorylength)*