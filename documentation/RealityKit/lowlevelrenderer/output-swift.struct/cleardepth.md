# clearDepth

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The depth value to use when clearing the depth attachment at the start of a render pass.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var clearDepth: Double { get set }
```

#### Discussion

Corresponds to `MTLRenderPassDepthAttachmentDescriptor.clearDepth`.

## See Also

### Clearing and resolving
- [var clearColor: MTLClearColor](./clearcolor.md)
  The color to use when clearing the color attachment at the start of a render pass.
- [var depthResolveFilter: MTLMultisampleDepthResolveFilter](./depthresolvefilter.md)
  The filter to use when resolving the depth attachment at the end of a multisampled render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/output-swift.struct/cleardepth)*