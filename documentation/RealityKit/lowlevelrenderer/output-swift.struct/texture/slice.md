# slice

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The slice of the texture to use. Corresponds to `MTLRenderPassAttachmentDescriptor.slice`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var slice: Int { get set }
```

## See Also

### Addressing the texture
- [var level: Int](./level.md)
  The mipmap level of the texture to use. Corresponds to `MTLRenderPassAttachmentDescriptor.level`.
- [var depthPlane: Int](./depthplane.md)
  The depth plane of the texture to use. Corresponds to `MTLRenderPassAttachmentDescriptor.depthPlane`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/output-swift.struct/texture/slice)*