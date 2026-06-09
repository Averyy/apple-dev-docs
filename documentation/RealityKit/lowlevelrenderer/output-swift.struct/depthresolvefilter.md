# depthResolveFilter

**Framework**: RealityKit  
**Kind**: property

The filter to use when resolving the depth attachment at the end of a multisampled render pass.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var depthResolveFilter: MTLMultisampleDepthResolveFilter { get set }
```

#### Discussion

Corresponds to `MTLRenderPassDepthAttachmentDescriptor.depthResolveFilter`.

## See Also

- [var clearColor: MTLClearColor](lowlevelrenderer/output-swift.struct/clearcolor.md)
  The color to use when clearing the color attachment at the start of a render pass.
- [var clearDepth: Double](lowlevelrenderer/output-swift.struct/cleardepth.md)
  The depth value to use when clearing the depth attachment at the start of a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/output-swift.struct/depthresolvefilter)*