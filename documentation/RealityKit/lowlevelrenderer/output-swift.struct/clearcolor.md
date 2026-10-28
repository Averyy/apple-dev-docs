# clearColor

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The color to use when clearing the color attachment at the start of a render pass.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var clearColor: MTLClearColor { get set }
```

## Discussion

Corresponds to `MTLRenderPassColorAttachmentDescriptor.clearColor`.

## See Also

### Clearing and resolving
- [var clearDepth: Double](./cleardepth.md)
  The depth value to use when clearing the depth attachment at the start of a render pass.
- [var depthResolveFilter: MTLMultisampleDepthResolveFilter](./depthresolvefilter.md)
  The filter to use when resolving the depth attachment at the end of a multisampled render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/output-swift.struct/clearcolor)*