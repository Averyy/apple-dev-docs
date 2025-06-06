# generateDilatedDepth(from:commandBuffer:)

**Framework**: ARKit  
**Kind**: method

Generates dilated depth at the resolution of the segmentation stencil.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func generateDilatedDepth(from frame: ARFrame, commandBuffer: any MTLCommandBuffer) -> any MTLTexture
```

#### Return Value

A dilated depth texture which consists of a single channel of type `float32`.

#### Discussion

You use the linear depth information this function provides when compositing a virtual object with the camera image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/armattegenerator/generatedilateddepth(from:commandbuffer:))*