# encode(commandBuffer:)

**Framework**: MetalFX  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encode this spatial scaler work into a command buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 27.1+
- visionOS 26.0+

## Declaration

```swift
func encode(commandBuffer: any MTL4CommandBuffer)
```

```objc
- (void) encodeToCommandBuffer:(id<MTL4CommandBuffer>) commandBuffer;
```

## Parameters

- `commandBuffer`: A command buffer into which this spatial scaler encodes work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtl4fxspatialscaler/encode(commandbuffer:))*