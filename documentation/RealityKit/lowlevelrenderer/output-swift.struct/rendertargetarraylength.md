# renderTargetArrayLength

**Framework**: RealityKit  
**Kind**: property

The number of active array slices in the render target textures.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var renderTargetArrayLength: Int { get set }
```

#### Discussion

Corresponds to `MTLRenderPassDescriptor.renderTargetArrayLength`. Set this to the size of the texture array when using multi-viewport rendering into texture slices.

## See Also

- [var renderTargetWidth: Int](lowlevelrenderer/output-swift.struct/rendertargetwidth.md)
  The width of the render target, in pixels.
- [var renderTargetHeight: Int](lowlevelrenderer/output-swift.struct/rendertargetheight.md)
  The height of the render target, in pixels.
- [var threadgroupMemoryLength: Int](lowlevelrenderer/output-swift.struct/threadgroupmemorylength.md)
  The per-tile size, in bytes, of the persistent threadgroup memory allocation, used when rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/output-swift.struct/rendertargetarraylength)*