# generateDilatedDepth(from:commandBuffer:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Generates dilated depth at the resolution of the segmentation stencil.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
func generateDilatedDepth(from frame: ARFrame, commandBuffer: any MTLCommandBuffer) -> any MTLTexture
```

```objc
- (id<MTLTexture>) generateDilatedDepthFromFrame:(ARFrame *) frame commandBuffer:(id<MTLCommandBuffer>) commandBuffer;
```

## Return Value

Dilated depth `MTLTexture` for the given `ARFrame` at the segmentation stencil resolution. The texture consists of a single channel and is of type `float16`.

## Discussion

You use the linear depth information this function provides when compositing a virtual object with the camera image. The reprojection of this depth to the caller’s scene space is carried out externally.

## Parameters

- `frame`: Current `ARFrame` containing camera image and estimated depth buffer. The caller is to ensure that a valid depth buffer is present.
- `commandBuffer`: Metal command buffer for encoding depth dilation operations. The command buffer is committed by the caller externally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/armattegenerator/generatedilateddepth(from:commandbuffer:))*