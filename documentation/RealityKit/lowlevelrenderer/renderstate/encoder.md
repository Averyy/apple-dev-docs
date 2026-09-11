# encoder

**Framework**: RealityKit  
**Kind**: property

The underlying Metal render command encoder for this render pass.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var encoder: any MTLRenderCommandEncoder { get }
```

#### Discussion

You can use this encoder to set additional render state or issue custom draw calls between calls to `render(meshInstancesArrayIndex:meshInstanceIndex:)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/renderstate/encoder)*