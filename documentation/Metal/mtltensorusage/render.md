# render

**Framework**: Metal  
**Kind**: property

A tensor context that applies to render encoders.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static var render: MTLTensorUsage { get }
```

#### Discussion

You can use tensors with this context in [`MTL4RenderCommandEncoder`](mtl4rendercommandencoder.md) or [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorusage/render)*