# renderTargetHeight

**Framework**: RealityKit  
**Kind**: property

The height of the render target, in pixels.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var renderTargetHeight: Int { get set }
```

#### Discussion

Corresponds to `MTLRenderPassDescriptor.renderTargetHeight`.

## See Also

- [var renderTargetWidth: Int](lowlevelrenderer/output-swift.struct/rendertargetwidth.md)
  The width of the render target, in pixels.
- [var renderTargetArrayLength: Int](lowlevelrenderer/output-swift.struct/rendertargetarraylength.md)
  The number of active array slices in the render target textures.
- [var threadgroupMemoryLength: Int](lowlevelrenderer/output-swift.struct/threadgroupmemorylength.md)
  The per-tile size, in bytes, of the persistent threadgroup memory allocation, used when rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/output-swift.struct/rendertargetheight)*