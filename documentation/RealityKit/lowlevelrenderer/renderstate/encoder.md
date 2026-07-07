# encoder

**Framework**: RealityKit  
**Kind**: property

The underlying Metal render command encoder for this render pass.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var encoder: any MTLRenderCommandEncoder { get }
```

#### Discussion

You can use this encoder to set additional render state or issue custom draw calls between calls to `render(meshInstancesArrayIndex:meshInstanceIndex:)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/renderstate/encoder)*